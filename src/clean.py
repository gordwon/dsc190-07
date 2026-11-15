import pandas as pd
from pathlib import Path

VALID_TYPES = {"click", "view", "login", "scroll", "purchase"}

df = pd.read_csv("data/raw/events.csv", dtype=str)
df = df.apply(lambda c: c.str.strip()).replace("", pd.NA)

# Parse the two timestamp styles explicitly
iso = pd.to_datetime(df["timestamp"], format="ISO8601", errors="coerce")
slash = pd.to_datetime(df["timestamp"], format="%m/%d/%Y %H:%M:%S", errors="coerce")
df["timestamp"] = iso.fillna(slash)

df["duration_seconds"] = pd.to_numeric(df["duration_seconds"], errors="coerce")

df = df.dropna()
df = df[df["event_type"].isin(VALID_TYPES)]
df = df[df["duration_seconds"] > 0]

df["duration_seconds"] = df["duration_seconds"].astype(int)
df["timestamp"] = df["timestamp"].dt.strftime("%Y-%m-%dT%H:%M:%S")

Path("data/clean").mkdir(parents=True, exist_ok=True)
df.to_csv("data/clean/events.csv", index=False)
