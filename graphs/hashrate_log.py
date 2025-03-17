import matplotlib.pyplot as plt

# Data
hash_count = [10, 100, 1000, 10000, 100000, 200000, 400000, 600000, 800000, 1000000]
cpu_runtime = [
    1.119999999,
    2.39000001,
    2.429999995,
    16.98,
    275.01,
    331.28,
    707.85,
    1162.27,
    1331.04,
    1759.59,
]
gpu_runtime = [
    12.08,
    2.850000012,
    3.5,
    10.13,
    80.76999999,
    140.84,
    362.52,
    521.15,
    877.37,
    1072.99,
]
cpu_hash_sec = [
    11233.2669,
    45709.56519,
    416408.321,
    596415.2329,
    431390.8949,
    637110.5511,
    620243.5489,
    534811.967,
    625904.3511,
    596855.224,
]
gpu_hash_sec = [
    994.6492711,
    35223.41517,
    286830.2957,
    994788.7486,
    1276573.653,
    1436967.043,
    1267058.314,
    1292021.192,
    938425.1268,
    949165.7124,
]

# Create figure and axes
fig, axs = plt.subplots(1, 1, figsize=(10, 8))  # Adjusted figure size
# Plot hash rate comparison
axs.plot(hash_count, cpu_hash_sec, marker="o", linestyle="-", label="CPU Hashes/Sec")
axs.plot(hash_count, gpu_hash_sec, marker="s", linestyle="-", label="GPU Hashes/Sec")
axs.set_xscale("log")
axs.set_yscale("log")
axs.set_xlabel("Hash Count (log scale)", fontsize=20)
axs.set_ylabel("Hashes per Second (log scale)", fontsize=20)
axs.set_title("CPU vs GPU Hash Rate (Averages of 10 runs)", fontsize=22)
axs.legend(fontsize=20)
axs.tick_params(axis="both", labelsize=20)
axs.grid(True, which="both", linestyle="--", linewidth=0.5)

# Add subtitle (adjusted for conciseness)
fig.suptitle(
    "Hash Rate Comparison for CPU and GPU across Different Hash Counts", fontsize=24
)

axs.xaxis.offsetText.set_fontsize(20)
axs.yaxis.offsetText.set_fontsize(20)

# Show the plot
plt.tight_layout()
plt.show()
