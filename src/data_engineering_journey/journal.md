# Learning journal

## Day 0 — Sep 27
Built: Python + uv + VS Code setup, first functions, imports between files, first GitHub repo
Broke: Restricted Mode, main() not being called
Enjoyed (1–10): 6 
Bored (1–10): 1
Hours: ~ 2 hours 

## Day 1 — Sep 28 (Mon)
Built: Watched Missing Semester lecture 1 (The Shell), 33 of 48 min. Practised navigating with cd, ls, pwd.
Broke: cd ./Users failed because ./ means "inside the current folder". open vs code failed because spaces split it into two names.
Learned: Absolute paths (start with /) vs relative paths. On Linux, hardware appears as files in /sys (LEDs, brightness), like memory-mapped registers.
Decided: Build quietly for the first few weeks, post later. Pause the AWS Cloud Practitioner course until Week 4.
Enjoyed (1–10): 3
Bored (1–10): 7 
Hours: 3

## Day 2 — Sep 29 (Tue)
Built: Learn Git Branching, levels 1–4 (commits, branches, merge, rebase). Finished the rest of the shell lecture.
Broke: Started out guessing; checked out a commit instead of a branch; used git branch (creates only) instead of git checkout -b (creates and switches).
Learned: Commits are snapshots, branches are sticky notes, HEAD is "you are here". Merge joins two lines; rebase replays work into a straight line.
Enjoyed (1–10): 10 
challenging (1-10): 7 
Bored (1–10): 2
Hours: 3

## Day 3 — Sep 30 (Wed)
Built: Weather script Step 1. Fetched live Limerick weather from the Open-Meteo API with requests (status 200).
Broke: NameError from a typo (parmas vs params). Learned to read errors from the bottom line up.
Learned: JSON comes back as dictionaries and lists. The data is in UTC, not Irish time.
Decided: Signature project theme is transport: a Limerick bus reliability tracker using NTA open data.
Enjoyed (1–10): 8
challenging (1-10): 4
Hours: 2 

## Day 4 — Oct 1
Built: Weather script Step 2. Pulled 48 hours of Limerick weather and summarised it: warmest, coldest, average temperature, total rain. Turned columns into rows with zip, filtered rainy hours with an if inside the loop, and filtered yesterday's data by date with startswith.
Broke: The rain check printed nothing because the if was outside the loop. Learned that indentation decides what belongs to the loop (Python's version of { } in C).
Learned: The API gives columns, zip gives rows. Timestamps are in UTC, not Irish time. Filtering by a condition is the same idea as WHERE in SQL.
Decided: Stop mass-applying; apply only to roles that fit, embedded only with a referral. Build strong evidence and solid basics. Check visa options this week.
Enjoyed (1–10): 8 — it was genuinely fun
Challenging (1-10): 8
Hours: 2 
## Day 5 — Oct 3 (Sat)
Built: Fixed the timezone (timezone: Europe/Dublin), so times now match Irish clock time. Built weather_v2.py: turned the hourly data into a Polars DataFrame (48 rows × 3 columns), converted time text to real datetimes, calculated the average with .mean(), filtered rainy hours with .filter(), and saved the table as a Parquet file in data/raw/2026-10-03. Found 6 rainy hours yesterday afternoon, with a 5.8 mm downpour at 16:00.
Broke: Nothing in the code. The block was in my head: a "you're not ready, understand everything first" voice right before starting Part 2.
Learned: My first full ETL pipeline: Extract (API) → Transform (table + types) → Load (Parquet). What requests.get, status codes, params=... and the nested JSON keys mean. Understanding comes AFTER doing, not before.
Noticed: My "not ready / too hard midway" pattern showed up live. I named it, panicked a bit, took a break, came back and did it anyway. Bringing this to my therapist.
Enjoyed (1–10):3
Zoned out (1–10): 8
Hours:~ 2 hours 
## Day 6 — Oct 4 (Sun, travelling to Wicklow)
Built: explore.py. Loaded my saved weather table back from the Parquet file (no internet needed) with pl.read_parquet, then sorted it with .sort().
Broke: df.sort(...) on its own line didn't change anything. Learned that sort/filter return a NEW table, so I need print(df.sort(...)) or df = df.sort(...).
Learned: Coldest hour was 8am on 3 Oct (7.1°C), just after sunrise, not midnight. How rain is measured (tipping-bucket gauge = pulse counter, like GPIO interrupts). Read a row as a sentence: check the column names first.
Ideas: Touch-based emotion sensing while scrolling (affective computing), flipped to help the user take a break. Links to my haptics MSc.
Enjoyed (1–10): 10 on 10
Hours: 1 hour 

## Day 7 — Oct 5 (Mon)
Built: sql_play.py. First SQL queries with DuckDB directly on my Parquet file: rainy hours (6 rows), warm hours >15°C (11 rows, written by me), sorted hottest first.
Learned: SELECT, FROM, WHERE, ORDER BY ... DESC. Same question three ways: Python if, Polars .filter(), SQL WHERE. Polars prints "shape" automatically (rows, columns). .str.to_datetime() turns text into a real date-time; Python's str() does the opposite.
Broke: Ran the wrong file and wondered why my print didn't show. The terminal only shows output from the file I run.
Enjoyed (1–10): 8
Hours: 1 hour 