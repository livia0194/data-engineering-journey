import requests
import polars as pl
from datetime import date
from pathlib import Path

URL = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 52.66,
    "longitude": -8.63,
    "hourly": "temperature_2m,precipitation",
    "past_days": 1,
    "forecast_days": 1,
    "timezone": "Europe/Dublin",
}


def main():
    response = requests.get(URL, params=params)
    response.raise_for_status()
    data = response.json()

    # 1. Build a table from the hourly data
    df = pl.DataFrame(data["hourly"])
    df = df.with_columns(pl.col("time").str.to_datetime())
    print("data frame",df)

    # 2. Same questions as before, the DataFrame way
    print(df.select(pl.col("temperature_2m").mean()))
    print(df.filter(pl.col("precipitation") > 0))
    print(df.filter(pl.col("temperature_2m")>15))

    # 3. Save it to a file
    out_dir = Path("data/raw") / str(date.today())
    out_dir.mkdir(parents=True, exist_ok=True)
    df.write_parquet(out_dir / "weather.parquet")
    print("Saved to", out_dir)
    

if __name__ == "__main__":
    main()