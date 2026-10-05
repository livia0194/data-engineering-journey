import duckdb

result = duckdb.sql("""
    SELECT time, temperature_2m, precipitation
    FROM 'data/raw/2026-10-03/weather.parquet'
    WHERE temperature_2m >15
    ORDER BY temperature_2m DESC
""")

print(result)