import matplotlib.pyplot as plt

# Data
hash_count = [100000, 200000, 400000, 600000, 800000, 1000000]
cpu_runtime = [
    275.01,
    331.28,
    707.85,
    1162.27,
    1331.04,
    1759.59,
]
gpu_runtime = [
    80.76999999,
    140.84,
    362.52,
    521.15,
    877.37,
    1072.99,
]
cpu_hash_sec = [
    431390.8949,
    637110.5511,
    620243.5489,
    534811.967,
    625904.3511,
    596855.224,
]
gpu_hash_sec = [
    1276573.653,
    1436967.043,
    1267058.314,
    1292021.192,
    938425.1268,
    949165.7124,
]

# Create figure and axes
fig, axs = plt.subplots(2, 1, figsize=(10, 10))

# Plot runtime comparison
axs[0].plot(hash_count, cpu_runtime, marker="o", linestyle="-", label="CPU Runtime")
axs[0].plot(hash_count, gpu_runtime, marker="s", linestyle="-", label="GPU Runtime")
axs[0].set_xlabel("Hash Count")
axs[0].set_ylabel("Runtime (Milliseconds)")
axs[0].set_title("CPU vs GPU Runtime")
axs[0].legend()
axs[0].grid(True, which="both", linestyle="--", linewidth=0.5)

# Plot hash rate comparison
axs[1].plot(hash_count, cpu_hash_sec, marker="o", linestyle="-", label="CPU Hashes/Sec")
axs[1].plot(hash_count, gpu_hash_sec, marker="s", linestyle="-", label="GPU Hashes/Sec")
axs[1].set_xlabel("Hash Count")
axs[1].set_ylabel("Hashes per Second")
axs[1].set_title("CPU vs GPU Hash Rate")
axs[1].legend()
axs[1].grid(True, which="both", linestyle="--", linewidth=0.5)

# Add subtitle
fig.suptitle(
    "Performance Comparison of Hashing between CPU and GPU with Hash Counts from $10^5$ to $10^6$",
    fontsize=16,
)


# Show the plot
plt.tight_layout()
plt.show()
