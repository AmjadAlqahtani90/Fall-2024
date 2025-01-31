import matplotlib.pyplot as plt
import pandas as pd

# Function to parse YCSB output
def parse_ycsb_output(filename):
    metrics = {
        "Workload": None,
        "Throughput(ops/sec)": None,
        "Avg_Read_Latency_ms": None, "Read_95th_Latency_ms": None,
        "Avg_Update_Latency_ms": None, "Update_95th_Latency_ms": None,
        "Avg_Cleanup_Latency_ms": None, "Cleanup_95th_Latency_ms": None,
        "Avg_Insert_Latency_ms": None, "Insert_95th_Latency_ms": None,
        "Avg_Scan_Latency_ms": None, "Scan_95th_Latency_ms": None,
        "Insert_Failures": 0, "Avg_Insert_Fail_Latency_ms": None, "Insert_Fail_95th_Latency_ms": None
    }
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                # Throughput
                if line.startswith("[OVERALL]") and "Throughput(ops/sec)" in line:
                    metrics["Throughput(ops/sec)"] = float(line.split(",")[-1].strip())
                
                # Read latencies
                if line.startswith("[READ]"):
                    if "AverageLatency(us)" in line:
                        metrics["Avg_Read_Latency_ms"] = float(line.split(",")[2].strip()) / 1000
                    if "95thPercentileLatency(us)" in line:
                        metrics["Read_95th_Latency_ms"] = float(line.split(",")[2].strip()) / 1000
                
                # Update latencies
                if line.startswith("[UPDATE]"):
                    if "AverageLatency(us)" in line:
                        metrics["Avg_Update_Latency_ms"] = float(line.split(",")[2].strip()) / 1000
                    if "95thPercentileLatency(us)" in line:
                        metrics["Update_95th_Latency_ms"] = float(line.split(",")[2].strip()) / 1000
                
                # Cleanup latencies
                if line.startswith("[CLEANUP]"):
                    if "AverageLatency(us)" in line:
                        metrics["Avg_Cleanup_Latency_ms"] = float(line.split(",")[2].strip()) / 1000
                    if "95thPercentileLatency(us)" in line:
                        metrics["Cleanup_95th_Latency_ms"] = float(line.split(",")[2].strip()) / 1000
                
                # Insert latencies
                if line.startswith("[INSERT]"):
                    if "AverageLatency(us)" in line:
                        metrics["Avg_Insert_Latency_ms"] = float(line.split(",")[2].strip()) / 1000
                    if "95thPercentileLatency(us)" in line:
                        metrics["Insert_95th_Latency_ms"] = float(line.split(",")[2].strip()) / 1000

                if line.startswith("[INSERT-FAILED]"):
                    if "Operations" in line:
                        # Extract the numeric value after "Operations"
                        parts = line.split(",")
                        print(parts)
                        if len(parts) > 2 and parts[2].strip().isdigit():
                            metrics["Insert_Failures"] += int(parts[2].strip())
                    if "AverageLatency(us)" in line:
                        metrics["Avg_Insert_Fail_Latency_ms"] = float(line.split(",")[2].strip()) / 1000
                    if "95thPercentileLatency(us)" in line:
                        metrics["Insert_Fail_95th_Latency_ms"] = float(line.split(",")[2].strip()) / 1000

                # Scan latencies
                if line.startswith("[SCAN]"):
                    if "AverageLatency(us)" in line:
                        metrics["Avg_Scan_Latency_ms"] = float(line.split(",")[2].strip()) / 1000
                    if "95thPercentileLatency(us)" in line:
                        metrics["Scan_95th_Latency_ms"] = float(line.split(",")[2].strip()) / 1000
    except FileNotFoundError:
        print(f"File {filename} not found.")
    
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
    try:
        data = parse_ycsb_output(filename)
        data["Workload"] = workload
        workload_data.append(data)
    except Exception as e:
        print(f"Error processing {workload}: {e}")

# Convert to DataFrame and handle missing values
df = pd.DataFrame(workload_data).fillna(0)

# Visualization
plt.figure(figsize=(20, 10))
x = range(len(df))

# Bar width and labels for all metrics
bar_width = 0.08
metrics = [
    ("Avg_Read_Latency_ms", "Read Avg Latency (ms)", "green"),
    ("Read_95th_Latency_ms", "Read 95th Latency (ms)", "blue"),
    ("Avg_Update_Latency_ms", "Update Avg Latency (ms)", "orange"),
    ("Update_95th_Latency_ms", "Update 95th Latency (ms)", "red"),
    ("Avg_Insert_Latency_ms", "Insert Avg Latency (ms)", "purple"),
    ("Insert_95th_Latency_ms", "Insert 95th Latency (ms)", "cyan"),
    ("Avg_Scan_Latency_ms", "Scan Avg Latency (ms)", "brown"),
    ("Scan_95th_Latency_ms", "Scan 95th Latency (ms)", "pink"),
    ("Avg_Insert_Fail_Latency_ms", "Insert Fail Avg Latency (ms)", "grey"),
    ("Insert_Fail_95th_Latency_ms", "Insert Fail 95th Latency (ms)", "black"),
]

# Plot metrics
for i, (column, label, color) in enumerate(metrics):
    plt.bar(
        [p + i * bar_width for p in x],
        df[column],
        width=bar_width,
        label=label,
        alpha=0.7,
        color=color,
    )

# Customize the chart
plt.title("YCSB Latencies and Metrics by Workload", fontsize=18)
plt.ylabel("Latency (ms)", fontsize=14)
plt.xlabel("Workloads", fontsize=14)
plt.xticks([p + bar_width * (len(metrics) / 2) for p in x], df["Workload"], rotation=45, fontsize=12)
plt.legend(fontsize=12)
plt.tight_layout()

# Show the plot
plt.show()
