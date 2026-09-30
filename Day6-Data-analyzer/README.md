# AI Data Analyzer

A small Python tool that reads a sales CSV, computes real statistics with **pandas**, then hands those stats to **Gemini** so it can answer plain-language questions about the data.

> Part of my 70-Day AI Engineering Roadmap — Day 5/6 project.

## What it does

1. Loads a sales dataset (`Date`, `Product`, `Region`, `Sales`) with pandas
2. Computes real stats — overall sales summary, average sales by region, total sales by product
3. Turns those stats into a plain-text summary
4. Sends that summary + your question to Gemini, which answers in natural language

The idea: pandas handles the **exact math** (never trust an LLM to do arithmetic on raw numbers), and the LLM handles **interpretation** — explaining what the numbers mean.

## Tech stack

- Python 3
- [pandas](https://pandas.pydata.org/) — data loading & analysis
- [google-genai](https://ai.google.dev/) — Gemini API
- python-dotenv — environment variable management

## Project structure

```
├── main.py         # loads data, computes stats, builds summary, asks Gemini
├── ai_service.py   # Gemini client setup + analyze_data() function
├── data.csv         # sample sales dataset
├── .env              # GEMINI_API_KEY (not committed)
└── requirements.txt
```

## Setup

1. Clone the repo and create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # on Windows: .venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install pandas google-genai python-dotenv
   ```

3. Create a `.env` file in the project root:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

4. Add your own CSV as `data.csv`, or use the sample one included, with columns:
   ```
   Date, Product, Region, Sales
   ```

## Usage

```bash
python main.py
```

The script will print the computed stats, then prompt you:

```
Whats Your Question? :
```

Type a question about the data (e.g. *"Which region is underperforming and why might that be?"*) and Gemini will respond based on the computed summary.

## Example output

```
DataSet has 30 rows

overAll Sales Stats:
count      30.000000
mean     1190.333333
std       266.088958
min       760.000000
...

average Sales By region:
Region
East     1120.000000
North    1242.500000
South    1168.750000
West     1225.714286

Total Sales by Product:
Product
Widget A    12360
Widget B    10960
Widget C    12390
```

## What I learned building this

- pandas basics: `read_csv`, `.head()`, `.info()`, `.describe()`, `.isnull().sum()`
- `groupby()` for splitting data into categories and aggregating (`.mean()`, `.sum()`)
- Why you compute stats with pandas instead of letting an LLM guess at numbers
- Passing structured data to an LLM as a text summary, since it can't read a DataFrame directly

## Roadmap

This is Day 5 of my [70-Day AI Engineering Roadmap](#) — building one small AI-powered tool per day to practice Python, pandas, and working with LLM APIs.
