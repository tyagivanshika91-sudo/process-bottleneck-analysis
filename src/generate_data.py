
from pathlib import Path
import pandas as pd
import numpy as np

OUTPUT = Path("data/raw/orders.csv")

def main():
    np.random.seed(42)
    n = 1000

    order_date = pd.date_range(
        start="2026-01-01",
        periods=n,
        freq="h"
    )

    processing = np.random.randint(1, 13, n)
    packaging = np.random.randint(1, 9, n)
    shipping = np.random.randint(8, 49, n)
    delivery = np.random.randint(4, 25, n)

    total_hours = processing + packaging + shipping + delivery

    df = pd.DataFrame({
        "order_id": range(1001, 1001 + n),
        "order_date": order_date,
        "region": np.random.choice(
            ["North", "South", "East", "West"], n
        ),
        "order_value": np.random.randint(300, 10001, n),
        "processing_hours": processing,
        "packaging_hours": packaging,
        "shipping_hours": shipping,
        "delivery_hours": delivery,
        "total_delivery_hours": total_hours,
        "delivery_status": np.where(
            total_hours > 65, "Late", "On Time"
        )
    })

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT, index=False)

    print("Synthetic order dataset created successfully!")
    print("Total orders:", len(df))
    print("Saved at:", OUTPUT)
    print(df.head())

if __name__ == "__main__":
    main()
