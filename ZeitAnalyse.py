from pathlib import Path
from datetime import datetime, timedelta
import matplotlib
matplotlib.use('TkAgg')  # Use an interactive backend if available
import matplotlib.pyplot as plt

import pandas as pd

SCRIPT_PATH = Path(__file__).parent

FILE = SCRIPT_PATH / "data" / "digital.csv"
# FILE = SCRIPT_PATH / "MessungsDaten" / "MessungenHTTP" / "digital.csv"

data_frame = pd.read_csv(FILE, sep=",", decimal=".", encoding="utf-8")
print(data_frame)
times = []
master = slave = False
time_master = time_slave = None


for index, row in data_frame.iterrows():
    if row["Slave"] == 1 and index > 0:
        prev_row = data_frame.iloc[index - 1]
        if prev_row["Master"] == 1:
            time_master = float(prev_row["Time [s]"])
            time_slave = float(row["Time [s]"])
            times.append(timedelta(seconds=(time_slave - time_master)))


average_time = sum(times, datetime.min - datetime.min) / len(times)
print(f"Average time difference: {average_time.microseconds}")
print(f"Max time difference: {max(times).microseconds}")
print(f"Min time difference: {min(times).microseconds}")
print(f"Number of measurements: {len(times)}")


print(f"Average time difference: {average_time}")
print(f"Max time difference: {max(times)}")
print(f"Min time difference: {min(times)}")
print(f"Number of measurements: {len(times)}")

# for i in range(1, 31):
    # total_ns = times[i].total_seconds() * 1e9
    # print(f"{int(total_ns)} ns")
# time_deltas_us = [td.microseconds / 1000 for td in times]
# time_deltas_us = [td.microseconds for td in times]
# plt.figure(figsize=(10, 5))
# plt.plot(range(len(time_deltas_us)), time_deltas_us, marker='o', linestyle='None')
# plt.xlabel('Number of Packet')
# plt.ylabel('Time Delta (us)')
# plt.title('Time Delta with UDP')
# plt.grid(True)
# plt.show()
from decimal import Decimal
times_ns = []

for index, row in data_frame.iterrows():
    if row["Slave"] == 1 and index > 0:
        prev_row = data_frame.iloc[index - 1]
        if prev_row["Master"] == 1:
            time_master = Decimal(str(prev_row["Time [s]"]))
            time_slave = Decimal(str(row["Time [s]"]))
            delta_ns = int((time_slave - time_master) * Decimal('1e9'))
            times_ns.append(delta_ns)
for i in range(1+30, 31+30):
    us = times_ns[i] / 1_000  # convert nanoseconds to microseconds
    print(f"{str(f'{us:.2f}').replace('.', ',')}")
