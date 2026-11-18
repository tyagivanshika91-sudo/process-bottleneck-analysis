
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

DATA = Path("data/raw/orders.csv")
OUT = Path("outputs")

def main():
    OUT.mkdir(exist_ok=True)

    df = pd.read_csv(DATA)

    stages = [
        "processing_hours",
        "packaging_hours",
        "shipping_hours",
        "delivery_hours"
    ]

    stage_summary = pd.DataFrame({
        "process_stage": stages,
        "average_hours": [df[col].mean() for col in stages],
        "median_hours": [df[col].median() for col in stages]
    }).sort_values("average_hours", ascending=False)

    late_percentage = (df["delivery_status"] == "Late").mean() * 100

    region_summary = df.groupby("region").agg(
        total_orders=("order_id", "count"),
        avg_delivery_hours=("total_delivery_hours", "mean"),
        late_orders=("delivery_status", lambda x: (x == "Late").sum())
    ).reset_index()

    region_summary["late_percentage"] = (
        region_summary["late_orders"] / region_summary["total_orders"] * 100
    )

    stage_summary.to_csv(OUT / "stage_analysis.csv", index=False)
    region_summary.to_csv(OUT / "region_analysis.csv", index=False)

    bottleneck = stage_summary.iloc[0]["process_stage"]

    plt.figure(figsize=(9, 5))
    plt.bar(stage_summary["process_stage"], stage_summary["average_hours"])
    plt.title("Average Time by Order Process Stage")
    plt.xlabel("Process Stage")
    plt.ylabel("Average Time (Hours)")
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.savefig(OUT / "process_bottleneck.png")
    plt.close()

    plt.figure(figsize=(8, 5))
    plt.bar(region_summary["region"], region_summary["late_percentage"])
    plt.title("Late Delivery Percentage by Region")
    plt.xlabel("Region")
    plt.ylabel("Late Orders (%)")
    plt.tight_layout()
    plt.savefig(OUT / "regional_delay.png")
    plt.close()

    print("PROCESS BOTTLENECK ANALYSIS")
    print("---------------------------")
    print("Total orders:", len(df))
    print("Late deliveries:", (df["delivery_status"] == "Late").sum())
    print("Late delivery percentage:", round(late_percentage, 2), "%")
    print("Main bottleneck:", bottleneck)
    print("\nStage analysis:")
    print(stage_summary.round(2).to_string(index=False))
    print("\nRegion analysis:")
    print(region_summary.round(2).to_string(index=False))
    print("\nReports saved in outputs folder.")

if __name__ == "__main__":
    main()
