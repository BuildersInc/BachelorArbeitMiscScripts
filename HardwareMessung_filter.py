import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

SCRIPT_PATH = Path(__file__).parent
FILE = SCRIPT_PATH / "data" / "digital.csv"

df = pd.read_csv(FILE, sep=",", decimal=".", encoding="utf-8")
df.columns = [col.strip() for col in df.columns]

target_rows = df[
    (df["B ALARM[0]"] == 1) &
    (df["A Alarm[0]"] == 1) &
    (df["A SIG OUT"] == 1)
]

results = []

for i, row in target_rows.iterrows():
    signal_time = row["Time [s]"]
    prev_candidates = df.loc[:i - 1]
    valid_prev = prev_candidates[
        (prev_candidates["B ALARM[0]"] == 1) &
        (prev_candidates["A Alarm[0]"] == 0) &
        (prev_candidates["A SIG OUT"] == 0)
    ]

    if not valid_prev.empty:
        prev_time = valid_prev.iloc[-1]["Time [s]"]
        time_diff = signal_time - prev_time
        results.append({
            "All Signals 1 Time [s]": signal_time,
            "Previous B-Only Time [s]": prev_time,
            "Time Difference [s]": time_diff
        })

result_df = pd.DataFrame(results)

# ----------- IQR-Filterung -----------
Q1 = result_df["Time Difference [s]"].quantile(0.25)
Q3 = result_df["Time Difference [s]"].quantile(0.75)
IQR = Q3 - Q1

lower_iqr = Q1 - 1.5 * IQR
upper_iqr = Q3 + 1.5 * IQR

# ----------- Zusätzliche harte Filtergrenzen (optional) -----------
MIN_US = 10     # minimal erlaubte Differenz in µs
MAX_US = 100    # maximal erlaubte Differenz in µs

filtered_df = result_df[
    (result_df["Time Difference [s]"] * 1e6 >= MIN_US) &
    (result_df["Time Difference [s]"] * 1e6 <= MAX_US)
]

# ----------- Statistik auf gefilterten Daten -----------
max_diff = filtered_df["Time Difference [s]"].max()
min_diff = filtered_df["Time Difference [s]"].min()
avg_diff = filtered_df["Time Difference [s]"].mean()

print("--- Gefilterte Zeitdifferenzen ---")
print(filtered_df)

print("--- Statistiken (ohne Ausreißer) ---")
print(f"Maximum Time Difference: {max_diff:.9f} s ({max_diff * 1e6:.9f} µs)")
print(f"Minimum Time Difference: {min_diff:.9f} s ({min_diff * 1e6:.9f} µs)")
print(f"Average Time Difference: {avg_diff:.9f} s ({avg_diff * 1e6:.9f} µs)")

latex_string = f"& {min_diff * 1e6:.5f} µs & {max_diff * 1e6:.5f} µs & {avg_diff * 1e6:.5f} µs \\\\"
latex_string = latex_string.replace(".", r"{,}")
print(latex_string)

# ----------- Plot -----------
center = 35
half_range = 35  # in µs
ymin = center - half_range
ymax = center + half_range

plt.figure(figsize=(10, 5))
plt.scatter(
    filtered_df["All Signals 1 Time [s]"],
    filtered_df["Time Difference [s]"] * 1e6,
    color="orange",
)
plt.gca().axes.get_xaxis().set_visible(False)
plt.ylabel("µs", fontsize=16)
plt.ylim(ymin, ymax)
plt.grid(True)
plt.xticks(fontsize=14)
plt.legend()
plt.tight_layout()
plt.show()
