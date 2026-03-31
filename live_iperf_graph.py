import json
import matplotlib.pyplot as plt

# === PATH TO YOUR JSON FILE ===
JSON_FILE = r"C:\Users\shrey\Desktop\iperf_output.json"

# Load the JSON
with open(JSON_FILE, "r") as f:
    data = json.load(f)

times = []
throughput = []

# iperf3 stores per-interval data in "intervals"
intervals = data.get("intervals", [])

for i, interval in enumerate(intervals, start=1):
    # Each interval has a "sum" section
    sumdata = interval.get("sum", {})
    bps = sumdata.get("bits_per_second", None)
    if bps is not None:
        times.append(i)                         # interval number = seconds
        throughput.append(bps / 1e6)           # convert to Mbps

# ---- Plotting ----
plt.figure(figsize=(9,4))
plt.plot(times, throughput, marker='o')
plt.xlabel("Time (seconds)")
plt.ylabel("Throughput (Mbps)")
plt.title("iperf3 Throughput vs Time")
plt.grid(True)
plt.tight_layout()
plt.show()
