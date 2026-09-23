# Day 3 — Python Log Analyzer

## What I built

I built a small Python terminal application that reads an application log file and turns it into a useful summary.

The program reads `logs/app.log` one line at a time and reports:

- Total requests
- Counts for log levels: `INFO`, `WARNING`, and `ERROR`
- Counts for HTTP status codes: `200`, `404`, and `500`
- How often each route was requested
- The most requested route
- Invalid log lines that were skipped safely

Example output from the sample data:

```text
{'INFO': 6, 'WARNING': 2, 'ERROR': 2}
{'200': 6, '404': 2, '500': 2}
{'/products': 4, '/login': 2, '/profile': 1, '/checkout': 1, '/orders': 1, '/unknown-page': 1}
Most requested route: /products
Request count: 4
Total requests: 10
```

## Why I built it

Real applications create logs while they run. Logs record normal events, unusual situations, and failures.

```text
Application writes logs
        ↓
app.log stores those events
        ↓
Log Analyzer reads the file
        ↓
Developer sees what is normal, suspicious, or broken
```

This project taught me the difference between an application that **writes logs** and a tool that **reads and analyzes logs**.

For example:

- `INFO` means a normal event happened.
- `WARNING` means something unusual happened but the application could continue.
- `ERROR` means an action failed.
- `200` usually means a successful request.
- `404` means the requested route was not found.
- `500` means the server failed while handling a request.

## Log format

Each line in `logs/app.log` follows this format:

```text
date time log-level HTTP-method route status-code
```

Example:

```text
2026-09-23 09:04:10 ERROR POST /checkout 500
```

This means a request to the `/checkout` route failed with a server error.

## Project structure

```text
Day3-Python_log_Analyizer/
├── app/
│   └── main.py
└── logs/
    └── app.log
```

## How it works

1. Python opens the log file in read mode.
2. It reads the file one line at a time.
3. It splits each line into separate pieces.
4. It extracts the log level, route, and status code from those pieces.
5. Dictionaries keep a running count of each value.
6. The program finds the route with the highest request count.
7. Invalid lines are skipped so the program does not crash.

```text
Raw log line
        ↓
Split into a list
        ↓
Extract useful fields
        ↓
Count fields in dictionaries
        ↓
Print a summary report
```

## What I wrote myself

I implemented and ran the project myself, including:

- Creating the project folders and log file
- Reading the file with `pathlib.Path` and a `with open(...)` block
- Looping through the log lines
- Splitting each line into fields
- Extracting values by their list positions
- Creating dictionaries for log levels, status codes, and routes
- Updating the dictionaries while the file was read
- Counting total requests
- Finding the most requested route
- Running the program, reading its output, and correcting errors

## Help I used from Codex

I used Codex as a mentor and debugger, not as a one-click project generator.

Codex helped me:

- Define the project goal and the sample log format
- Understand what logs are used for in real applications
- Understand the difference between a log producer and a log analyzer
- Debug a `FileNotFoundError` caused by running the program from the wrong folder
- Learn why `split()` is useful for parsing a line of text
- Understand list indexes for date, time, level, method, route, and status code
- Learn why dictionaries are useful for labeled counts
- Understand why route, status, and log-level counts should be separate dictionaries
- Understand why `max(..., key=...)` is needed to find the route with the highest count
- Add defensive handling for invalid or blank log lines

## What this project taught me

### Python skills

- File paths with `Path`
- File reading with `open()` and `with`
- Loops
- Strings and `split()`
- Lists and list indexes
- Dictionaries
- Conditions
- Counting values
- `max()` with dictionary values
- Defensive programming with `continue`

### Engineering skills

- How application logs help developers diagnose problems
- How to convert raw text into structured data
- How to turn many individual events into a useful report
- Why an application should continue safely when one input line is malformed
- How to debug a relative-path error by checking the folder where the program runs

## How to run

From the Day 3 project folder:

```bash
python app/main.py
```

Make sure the `logs/app.log` file exists relative to that project folder.

## Next improvement ideas

- Print the dictionaries as a cleaner, labeled report
- Count HTTP methods such as `GET` and `POST`
- Count errors by route
- Save the report to a text file
- Accept the log-file path from the user
- Use Python's `logging` module in a separate application to create real logs

## Key takeaway

This project is a small version of a real engineering workflow:

```text
Application events → logs → analysis → informed debugging decisions
```

I now understand that logs are not just random text. They are evidence of what an application did, what users requested, and where problems happened.
