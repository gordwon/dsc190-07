import pandas as pd
from pathlib import Path

df = pd.read_csv("data/clean/events.csv", dtype={"timestamp": str})
df["date"] = df["timestamp"].str[:10]

Path("data/transformed").mkdir(parents=True, exist_ok=True)
df.to_csv("data/transformed/events.csv", index=False)
