# 🚢 ComexIntel: Strategic & Automated Import Market Analysis

📊 View Interactive Dashboard here: [Dashboard](https://app.powerbi.com/view?r=eyJrIjoiNDkwYTcyMzYtY2VlYi00NGYzLTkyMDUtNWZmMDNjNGZjNWQ2IiwidCI6IjM5OTYyZjgwLTkyMTItNGIxZi04Yjk1LWU3OTYyYzRhY2IzMCIsImMiOjR9)

## 📌 Project Overview

ComexIntel is an *end-to-end* analytical solution designed to process, clean, and visualize customs import data for the food market (specifically focusing on the Allulose market for this initial iteration) in Mexico (January - April 2026).

This project replaces static Excel analyses with an **automated Python data pipeline** and an **interactive Power BI dashboard**, enabling the real-time identification of price trends, market volume, and key competitor strategies.

## 🎯 Business Problem

Manual analysis of import reports (via platforms like DataSur) is error-prone, leads to duplicate records, and consumes excessive operational time. Furthermore, data dispersion makes it difficult to quickly answer strategic questions such as:

* Who are the main players importing a specific product?
* Is the market paying an intermediary "premium" for logistics?
* How does the average market price (USD/kg) fluctuate against volume variations?

## ⚙️ Architecture & Data Flow

The data lifecycle consists of three phases:

1. **Extraction (Raw Data):** Monthly `.xlsx` files containing records at the customs declaration level.
2. **ETL Pipeline (Python / Pandas):**
* The script `02_pipeline_comexintel.py` consolidates source files from the raw data folder.
* Transforms and normalizes data types (dates, numerical variables).
* Generates unit metrics (Price USD/KG).
* Applies business rules for **deduplication** using the `NRO DOCUMENTO` as the primary key.
* ⚠️ **Technical Note on Scalability:** This Python pipeline was strictly designed for the tabular schema exported by the DataSur platform. While the solution can be scaled to analyze any other imported product or market, the input files must adhere to this specific column structure and format to parse correctly.


3. **Visualization (Power BI):** Consumes the processed dataset using a simple star schema and applies DAX functions for dynamic KPI calculation.

## 📊 Dashboard & Key Findings

The dashboard features bookmark navigation, collapsible dynamic filters, and conditional formatting based on price profitability ranges.

### 💡 Key Insights:

* **Market Volatility & Anomaly (March - April)**: A strong fluctuation was identified in Q1. While March recorded the highest price peak ($2.80 USD/kg) alongside the lowest volume, April drastically broke the trend with a massive jump in volume (exceeding 546,000 kg) and a downward price correction ($2.34 USD/kg). This suggests preventive panic buying in previous months or an aggressive entry of low-cost inventory in April.
* **Asian Dominance**: Geographical analysis reveals absolute reliance on the Eastern market. 66.67% of import transactions (32 records) come directly from China, establishing it as the main supplier, leaving the United States in a strategic second place with 31.25%.
* **Transaction Concentration**: The market is heavily led by two key players ("Importer 2" and "Importer 5"), who top the operational frequency with 7 transactions each during the period. The ranking's conditional formatting highlights efficiency gaps between primary importers and those with lower volumes.

**Price Efficiency (Conditional Formatting):**
Bar colors evaluate the average price per kg of the product:

* **Green:** Price is ≤ $2.20 USD/kg
* **Orange:** Price is ≥ $2.20 and < $2.70 USD/kg
* **Red:** Price is ≥ $2.70 USD/kg

## 🚀 Execution Instructions

To replicate this transformation pipeline in a local environment:

1. Clone this repository.
2. Ensure you have the required dependencies installed: `pip install pandas openpyxl`
3. Place your monthly reports in the `data/raw/` folder.
4. Run the pipeline from your terminal:
```bash
python scripts/02_pipeline_comexintel.py

```
