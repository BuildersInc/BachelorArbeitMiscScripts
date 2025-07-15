import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt


SCRIPT_PATH = Path(__file__).parent

FILE = SCRIPT_PATH / "data" / "digital.csv"

df = pd.read_csv(FILE, sep=",", decimal=".", encoding="utf-8")
df.columns = [col.strip() for col in df.columns]

target_rows = df[
    (df["B ALARM[0]"] == 1) &
    (df["A ALARM[0]"] == 1) &
    (df["A SIG OUT"] == 1)
]

results = []

for i, row in target_rows.iterrows():
    signal_time = row["Time [s]"]

    prev_candidates = df.loc[:i - 1]
    valid_prev = prev_candidates[
        (prev_candidates["B ALARM[0]"] == 1) &
        (prev_candidates["A ALARM[0]"] == 0) &
        (prev_candidates["A SIG OUT"] == 0)
    ]

    if not valid_prev.empty:
        prev_row = valid_prev.iloc[-1]
        prev_time = prev_row["Time [s]"]
        time_diff = signal_time - prev_time

        results.append({
            "All Signals 1 Time [s]": signal_time,
            "Previous B-Only Time [s]": prev_time,
            "Time Difference [s]": time_diff
        })

result_df = pd.DataFrame(results)

print(result_df)

# Filter using IQR

Q1 = result_df["Time Difference [s]"].quantile(0.25)
Q3 = result_df["Time Difference [s]"].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

filtered_df = result_df[
    (result_df["Time Difference [s]"] >= lower_bound) &
    (result_df["Time Difference [s]"] <= upper_bound)
]

max_diff = result_df["Time Difference [s]"].max()
min_diff = result_df["Time Difference [s]"].min()
avg_diff = result_df["Time Difference [s]"].mean()

print("--- Gefilterte Zeitdifferenzen ---")
print(filtered_df)

print("--- Statistiken (ohne Ausreißer) ---")
print(f"Maximum Time Difference: {max_diff:.9f} s ({max_diff * 1_000_000:.9f} µs)")
print(f"Minimum Time Difference: {min_diff:.9f} s ({min_diff * 1_000_000:.9f} µs)")
print(f"Average Time Difference: {avg_diff:.9f} s ({avg_diff * 1_000_000:.9f} µs)")


latex_string = f"& {min_diff * 1_000_000:.5f} µs & {max_diff * 1_000_000:.5f} µs & {avg_diff * 1_000_000:.5f} µs \\\\"
latex_string = latex_string.replace(".", r"{,}")
print(latex_string)

center = 35
half_range = 20  # in µs
ymin = center - half_range
ymax = center + half_range

plt.figure(figsize=(10, 5))
plt.scatter(
    result_df["All Signals 1 Time [s]"],
    result_df["Time Difference [s]"] * 1e6,
    color="orange",
    # label="All Events (Unfiltered)"
)
plt.gca().axes.get_xaxis().set_visible(False)

# plt.title("Latenz Messung 1.1", fontsize=18)
plt.ylabel("µs", fontsize=16)
plt.ylim(ymin, ymax)  # Setze y-Achsen-Bereich mit 35 µs in der Mitte
plt.grid(True)
plt.xticks(fontsize=14)
plt.legend()
plt.tight_layout()
plt.show()
