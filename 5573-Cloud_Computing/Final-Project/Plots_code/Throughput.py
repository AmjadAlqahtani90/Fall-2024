import re
import matplotlib.pyplot as plt
import pandas as pd

# Function to parse YCSB output for throughput
def parse_ycsb_output(filename):
    metrics = {"Throughput": None}
    with open(filename, 'r') as file:
        for line in file:
            # Extract throughput
            if line.startswith("[OVERALL]") and "Throughput(ops/sec)" in line:
                metrics["Throughput"] = float(line.split(",")[-1].strip())
    return metrics

# Files corresponding to each workload
workload_files = {
    "Workload A": "outputWorkloadA.txt",
    "Workload B": "outputWorkloadB.txt",
    "Workload C": "outputWorkloadC.txt",
    "Workload D": "outputWorkloadD.txt",
    "Workload E": "outputWorkloadE.txt",
    "Workload F": "outputWorkloadF.txt"
}

# Parse data from all workloads
workload_data = []
for workload, filename in workload_files.items():
    data = parse_ycsb_output(filename)
    data["Workload"] = workload
    workload_data.append(data)

# Convert to DataFrame
df = pd.DataFrame(workload_data)

# Visualization: Throughput
plt.figure(figsize=(10, 6))
plt.bar(df["Workload"], df["Throughput"], color='skyblue', alpha=0.8)

# Customize the chart
plt.title("Throughput (ops/sec) by Workload", fontsize=16)
plt.ylabel("Throughput (ops/sec)", fontsize=14)
plt.xlabel("Workload", fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.tight_layout()

# Show the plot
plt.show()
