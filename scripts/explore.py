import polars as pl

df = pl.read_parquet("data/raw/2026-10-03/weather.parquet")
print(df.sort("temperature_2m"))
print(df.sort("temperature_2m", descending=True))