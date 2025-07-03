---
categories: ai
cover: /img/blur-background-1680x1050-spectrum-electromagnetic-4k-901-1.jpg
date: 2025-07-02
description: Complete guide to exploratory data analysis (EDA) on ZIM shipping stock
  using Python, Yahoo Finance API, pandas, and data visualization. Learn stock market
  analysis techniques.
image: /img/blur-background-1680x1050-spectrum-electromagnetic-4k-901-1.jpg
keywords: EDA, exploratory data analysis, ZIM stock, Yahoo Finance, Python, pandas,
  stock market analysis, data visualization, yfinance, financial data
layout: post
organiser: Royfactory
tags: ai eda data-analysis pandas finance stock-market zim yfinance datavisualization
  python
title: 'EDA Tutorial: Analyzing ZIM Stock Data from Yahoo Finance'
toc: true
---

# EDA Tutorial: Analyzing ZIM Stock Data from Yahoo Finance

In this tutorial, we'll perform **exploratory data analysis (EDA)** using real-time stock data from **Yahoo Finance**. Our target is **ZIM Integrated Shipping Services Ltd. (Ticker: ZIM)**.

We’ll use the Python `yfinance` package to pull data directly, making the process repeatable and easy to update.

---

## 1. Install yfinance

First, install the `yfinance` package if you haven't already:

```bash
pip install yfinance
````

---

## 2. Load ZIM Stock Data from Yahoo Finance

```python
import yfinance as yf
import pandas as pd

# Download last 2 years of ZIM stock data
df = yf.download("ZIM", start="2023-01-01", end="2025-01-01")
df = df.reset_index()
df.head()
```

### ✅ Sample Columns:

| Date | Open | High | Low | Close | Adj Close | Volume |
| ---- | ---- | ---- | --- | ----- | --------- | ------ |

---

## 3. Basic Info and Cleaning

```python
df.info()
df.describe()
df.isnull().sum()
```

Make sure the `Date` column is in datetime format (usually it is by default from yfinance):

```python
df['Date'] = pd.to_datetime(df['Date'])
```

---

## 4. Visualize Closing Price

```python
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(12,6))
sns.lineplot(x='Date', y='Close', data=df)
plt.title("ZIM Closing Price Over Time")
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.show()
```

---

## 5. Volume Trend

```python
sns.lineplot(x='Date', y='Volume', data=df)
plt.title("ZIM Trading Volume Over Time")
plt.show()
```

This helps identify high-activity periods which might relate to earnings, dividends, or news events.

---

## 6. Monthly Average Price

```python
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

monthly_avg = df.groupby(['Year', 'Month'])['Close'].mean().reset_index()
monthly_avg['Date'] = pd.to_datetime(monthly_avg['Year'].astype(str) + '-' + monthly_avg['Month'].astype(str))

sns.lineplot(x='Date', y='Close', data=monthly_avg)
plt.title("Monthly Average Closing Price of ZIM")
plt.show()
```

---

## 7. Correlation Heatmap

```python
sns.heatmap(df[['Open', 'High', 'Low', 'Close', 'Volume']].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Between Stock Features")
plt.show()
```

---

## 8. Summary Insights

* ZIM stock shows **high volatility** with steep peaks and drops.
* Trading volume often spikes alongside price shifts.
* Price-related columns (Open, High, Low, Close) show **strong correlations**, which matters when building predictive models.

---

## Conclusion

In this tutorial, we explored ZIM stock data from **Yahoo Finance** using `yfinance` and performed a basic EDA using Pandas, Seaborn, and Matplotlib.

The same approach works for any other stock — just change the ticker symbol in `yf.download("TICKER")`.

Stay tuned for upcoming EDA tutorials using **real estate** and **e-commerce log** data!

---

## Recommended Titles

* "ZIM Stock EDA: Pulling Data from Yahoo Finance with Python"
* "How to Analyze Stock Data in Python (ZIM Case Study)"
* "From Yahoo to Insight: ZIM Stock EDA with yfinance"