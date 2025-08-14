import matplotlib.pyplot as plt
import random
import numpy as np
import matplotlib.ticker as mtick
# Software Simple Senden Big
zeiten_simple = [
    332.21, 295.61, 273.19, 271.19, 87.98, 303.922, 266.27, 306.03, 97.89, 318.13,
    318.13, 97.18, 194.51, 319.06, 208.17, 87.87, 122.07, 283.09, 162.41, 86.18,
    204.75, 271.98, 124.31, 221.04, 95.2, 274.33, 169.11, 306.79, 178.19, 327.83,
    149.77
]
# Software Simple Senden Small
# zeiten_simple = [
#     113.46, 113.45, 150.26, 113.46, 91.99, 142.83, 145.49, 116.63, 121.65, 174.17,
#     124.09, 81.0, 177.85, 155.12, 86.24, 161.04, 179.39, 83.36, 111.63, 171.93,
#     149.75, 164.79, 132.28, 167.73, 168.86, 162.97, 160.17, 121.63, 163.12, 105.67,
#     91.89
# ]

# # # Software Simpel Senden No
# zeiten_simple = [
#     78.62, 78.62, 83.02, 78.71, 78.54, 78.64, 81.85, 78.6, 78.57, 78.69,
#     78.32, 77.83, 77.83, 78.77, 78.87, 79.16, 84.9, 78.31, 80.52, 78.87,
#     83.76, 78.37, 82.6, 78.71, 78.36, 82.17, 80.84, 81.62, 78.32, 78.96,
#     83.45
# ]

# # Software Complex Big
zeiten_complex = [
    340.15, 267.39, 354.83, 114.52, 318.93, 206.37, 314.41, 229.89, 350.77,
    164.89, 287.62, 203.07, 128.01, 209.15, 228.37, 287.07, 283.82, 239.73,
    100.6, 136.71, 170.85, 236.73, 269.15, 135.07, 200.4, 361.65, 278.25,
    264.6, 261.9, 124.41, 205.62
]

# # Software Complex Small
# zeiten_complex = [
#     189.78, 145.0, 115.24, 189.05, 189.05, 93.51, 120.49, 124.23, 185.48, 156.26,
#     124.21, 177.18, 116.04, 138.6, 112.53, 174.53, 169.75, 187.89, 103.54, 112.0,
#     103.66, 127.45, 113.37, 112.0, 100.07, 100.79, 100.79, 100.63, 126.08, 192.73,
#     152.24
# ]

# # Software Complex No
# zeiten_complex = [
#     86.05, 86.15, 85.8, 85.59, 85.78, 89.97, 86.02, 85.58, 86.04, 88.42,
#     86.52, 86.1, 85.1, 88.55, 85.07, 86.35, 86.57, 85.48, 85.98, 86.36,
#     85.5, 86.16, 86.31, 85.86, 90.49, 86.03, 85.81, 86.07, 85.57, 86.16,
#     88.21
# ]

# # Hardware Senden Big
# zahlen_hardware_BIG = [
#     10.91, 10.9, 10.91, 10.91, 10.86, 10.91, 10.91, 10.9,
#     10.92, 10.9, 10.89, 10.9, 10.91, 10.9, 10.9, 10.91,
#     10.9, 10.91, 10.91, 10.9, 10.9, 10.89, 10.91, 10.9,
#     10.9, 10.91, 10.91, 10.9, 10.9, 10.91, 10.9
# ]

# # Hardware Senden Small
# zahlen_hardware_SMALL = [
#     10.9, 10.9, 10.89, 10.9, 10.9, 10.9, 10.91, 10.89,
#     10.9, 10.9, 10.9, 10.91, 10.91, 10.9, 10.9, 10.9,
#     10.91, 10.92, 10.91, 10.9, 10.9, 10.91, 10.9, 10.91,
#     10.9, 10.9, 10.9, 10.9, 10.9, 10.9, 10.91
# ]

# # Hardware Senden No Traffic
# zahlen_hardware_No = [
#     10.9, 10.9, 10.89, 10.9, 10.9, 10.9, 10.91, 10.89,
#     10.9, 10.9, 10.9, 10.91, 10.91, 10.9, 10.9, 10.9,
#     10.91, 10.92, 10.91, 10.9, 10.9, 10.91, 10.9, 10.91,
#     10.9, 10.9, 10.9, 10.9, 10.9, 10.9, 10.91
# ]

# random.shuffle(zahlen_hardware_No)

# # Software Recv Simpel
# zeiten_simple = [
#     597.78, 676.47, 632.99, 647.48, 630.85, 608.85, 658.23, 585.15, 613.76, 625.96,
#     611.39, 630.4, 668.44, 629.3, 544.23, 616.23, 599.3, 661.53, 656.98, 597.53,
#     669.04, 616.75, 545.87, 592.93, 618.4, 658.85, 607.42, 637.57, 656.69, 667.19,
#     623.16
# ]

# # # Software Recv Complex
# zeiten_complex = [
#     591.23, 612.87, 688.53, 613.27, 619.61, 680.4, 612.43, 643.02, 649.62, 634.02,
#     661.99, 645.28, 630.15, 588.56, 617.09, 679.02, 647.44, 593.21, 616.65, 627.114,
#     588.6, 645.03, 619.16, 640.49, 608.31, 595.46, 630.14, 620.85, 614.5, 634.68,
#     595.23
# ]

# Hardware Recv
zahlen_hardware_BIG = [
    8.6, 8.22, 9.23, 9.58, 8.72, 9.96, 9.38, 10.57,
    8.6, 9.26, 8.93, 10.37, 8.42, 8.6, 8.22, 8.37,
    8.22, 10.32, 11.41, 8.6, 11.31, 11.23, 10.26,
    8.6, 9.87, 10.14, 11.02, 8.91, 9.45, 10.78, 11.25
]


# Hardware Gesamt P2P
# zahlen_p2p = [
#     16.64, 17.72, 18.32, 16.67, 16.45, 17.15, 16.62, 16.67,
#     17.83, 16.37, 16.2, 16.88, 16.43, 17.23, 16.51, 16.43,
#     18.46, 16.72, 17.71, 17.89, 18.3, 17.52, 17.39, 17.87,
#     17.28, 17.49, 17.14, 16.2, 17.47, 17.9
# ]

# # Hardware Gesamt Switch
# zahlen_switch = [
#     25.26, 24.95, 25.16, 24.11, 23.81, 23.68, 24.15, 24.75,
#     25.1, 25.61, 24.63, 25.1, 24.22, 24.25, 25.09, 24.53,
#     25.12, 24.6, 25.28, 24.03, 24.12, 24.39, 24.07, 24.24,
#     25.05, 23.66, 23.64, 23.93, 23.8, 24.14
# ]

# # Software Gesamt P2P
zahlen_p2p = [
    688.46, 765.9, 709.2, 742.03, 721.58, 755.17, 763.23, 722.99,
    767.5, 716.72, 672.02, 716.63, 792.91, 768.47, 710.34, 709.66,
    672.18, 706.51, 709.8, 725.57, 733.18, 721.89, 710.89, 721.87,
    682.33, 732.23, 735.15, 719.26, 725.95, 685.41
]

# Software Gesamt Switch
zahlen_switch = [
    696.81, 698.33, 807.64, 696.81, 717.18, 691.81, 773.81, 765.61,
    696.81, 809.74, 700.31, 772.78, 696.65, 709.22, 744.62, 737.01,
    698.7, 743.05, 781.07, 779.19, 774.42, 735.8, 740.01, 770.01,
    779.39, 803.41, 771.38, 743.05, 813.51, 773.69
]

# x = list(range(1, len(zahlen_hardware_BIG)+1))

# # Plotten
# plt.figure(figsize=(10, 6))
# plt.scatter(x, zahlen_hardware_BIG, color='blue', label="Hardware")
# # plt.scatter(x, zahlen_hardware_BIG, color='blue', label="Hardware MaxFrame Traffic")
# # plt.scatter(x, zahlen_hardware_SMALL, color='orange', label="Hardware MinFrame Traffic", marker='s')
# # plt.scatter(x, zahlen_hardware_No, color='green', label="Hardware No Traffic", marker='x')


# # plt.title("")

# plt.xlabel("Ereignis Nummer", fontsize=22)
# plt.ylabel("Latenzzeit [μs]", fontsize=22)

# plt.grid(True)
# plt.tight_layout()
# plt.legend(loc='lower right', fontsize=14)
# plt.show()


x = list(range(1, len(zahlen_p2p) + 1))
# x = list(range(1, len(zeiten_simple) + 1))

plt.figure(figsize=(10, 6))
plt.scatter(x, zahlen_p2p, color='blue', label="Punkt zu Punkt", marker='o')
# plt.scatter(x, zeiten_simple, color='blue', label="Einfacher Alarm", marker='o')

plt.scatter(x, zahlen_switch, color='orange', label="Sternverbindung", marker='s')
# plt.scatter(x, zeiten_complex, color='orange', label="Komplexer Alarm", marker='s')

plt.xlabel("Ereignis Nummer", fontsize=18)
plt.ylabel("Latenzzeit [μs]", fontsize=18)
plt.grid(True)

# y-Achse so setzen, dass beide Datensätze gut sichtbar sind
min_y = min(min(zahlen_p2p), min(zahlen_switch))
# min_y = min(min(zeiten_simple), min(zeiten_complex))
max_y = max(max(zahlen_p2p), max(zahlen_switch))
# max_y = max(max(zeiten_simple), max(zeiten_complex))
plt.ylim(min_y * 0.95, max_y * 1.05)

plt.tight_layout()
plt.legend(loc='upper right', fontsize=14)
plt.show()



step = 50

array_1 = zahlen_p2p
# array_1 = zeiten_simple

array_2 = zahlen_switch

# array_2 = zeiten_complex
# Gemeinsame min und max Werte
all_values = array_1 + array_2
min_val = int(np.floor(min(all_values) / step) * step)
max_val = int(np.ceil(max(all_values) / step) * step)

bins = np.arange(min_val, max_val + step, step)

# Histogramm-Daten berechnen
counts_p2p, _ = np.histogram(array_1, bins=bins)
counts_switch, _ = np.histogram(array_2, bins=bins)

# Y-Positionen der Balken (einen pro Bin)
y_pos = np.arange(len(counts_p2p))

bar_height = 0.4

plt.barh(y_pos - bar_height/2, counts_p2p, height=bar_height, label='Punkt zu Punkt', edgecolor='black')
plt.barh(y_pos + bar_height/2, counts_switch, height=bar_height, label='Sternverbindung', edgecolor='black')

plt.yticks(y_pos, [f"{b}-{b+step-1}" for b in bins[:-1]])
plt.xlabel("Häufigkeit", fontsize=22)
plt.ylabel("Latenzbereich [us]", fontsize=22)

plt.legend(loc='upper right', fontsize=14)
ax = plt.gca()
ax.xaxis.set_major_formatter(mtick.FormatStrFormatter('%d'))

plt.show()
