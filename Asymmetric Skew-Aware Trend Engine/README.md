## 📈 Asymmetric Skew-Aware Trend Engine

## 📌 Strategy Rationale

**The Asymmetric Skew-Aware Trend Engine is designed for swing trading applications (currently applied to the Hang Seng Index Futures), integrating multi-layered momentum signals with volatility and skew-adjusted capital scaling.**

⭐️ **Key Highlight:**
#### *Strategy Advantage*
#### What distinguishes this strategy is not just its signal quality, but its dynamic adaptability. Rather than relying on rigid thresholds, the system continuously reevaluates market conditions to decide whether the current environment is statistically suitable for signal activation. This reverses the common approach: instead of forcing trades into static templates, the strategy listens to the market and only acts when the structural context aligns with its core logic.

*This README was automatically generated as part of a real-time strategy monitoring and reporting system. (Real-time strategy starts from March 2024 utill now)*

## 📌 Strategy Attributes

- **Strategy Name: Asymmetric Skew-Aware Trend Engine**  
- **Asset : Hang Seng Index Futures (HSI)**  
- **Type : Multi-factor Momentum with Volatility Structure Model**  
- **Rolling Frequency : 15-minute bars**  
- **Typical Holding Time : 0.5 to 2 days**
- **Strategy Time in Market (%) : 18.40%**   
- **Backtested Period : From June 2001 to June 2025** *(To evaluate whether the strategy can remain robust under all-weather market conditions.)*

⭐️ **Key Highlight:**
#### *Why Full-History Backtesting?*
#### (1) *The strategy is tested over the full historical dataset to capture a wide range of market regimes and ensure its resilience under different volatility, correlation, and macro cycles.*
#### (2) *The system incorporates a rolling logic core, allowing continuous internal adaptation without the need for manual parameter tuning—this reinforces the “all-weather” thesis.*

## 📌 Strategy Overview

This table provides a comprehensive summary of the trading strategy based on live and backtested data, covering both long and short trades. **Note:** **Just wanna mentioned here, the numbers presented here desire to reflect the real and true performance without any manipulation.**

Key performance metrics include :

- ✅ **Win Rate (%) : 72.71% with consistent returns across 1,396 trades.**
- ✅ **Annual Return: 31.08%**
- ✅ **Sharpe Ratio : 1.25 (From June 2001 to June 2025 -> 24 years backtested sharpe ratio)**
- Profit Factor : 1.66
- Maximum Drawdown : -10.49%

## 📌 Strategy Performance Report (Backtested Period : From May 2002 to June 2025)

This repository summarizes the performance of a trading strategy applied to Hang Seng Index Futures (HSI), highlighting core performance metrics, risk statistics, and trade breakdown.

### 📊 Annual Performance (HKD-Based)
This section outlines the annual performance of the strategy from 2002 to 2025, measured in HKD.


| Year | Profit (HK$) | Return (%) | Gross Profit | Gross Loss | Number of Trades | Win Rate (%) |
|------|--------------|------------|---------------|-------------|------------------|---------------|
| 2025 | -92,797      | -1.12%     | 300,353       | -393,150    | 30               | 63.33         |
| 2024 | 378,148      | 4.78%      | 1,192,278.5   | -814,130.5  | 92               | 68.48         |
| 2023 | 70,573.5     | 0.90%      | 898,273.5     | -827,700    | 85               | 67.06         |
| 2022 | 448,084.5    | 6.07%      | 1,479,206.5   | -1,031,122  | 105              | 77.14         |
| 2021 | -99,018      | -1.32%     | 680,632       | -779,650    | 49               | 61.22         |
| 2020 | 461,336      | 6.57%      | 1,083,986     | -622,650    | 64               | 70.31         |
| 2019 | 217,738.5    | 3.20%      | 814,988.5     | -597,250    | 58               | 58.62         |
| 2018 | 616,633.5    | 9.96%      | 1,419,033.5   | -802,400    | 76               | 76.32         |
| 2017 | 545,103      | 9.66%      | 632,403       | -87,300     | 42               | 80.95         |
| 2016 | 215,948      | 3.98%      | 685,048       | -469,100    | 65               | 69.23         |
| 2015 | 712,136      | 15.10%     | 1,280,386     | -568,250    | 75               | 77.33         |
| 2014 | 206,935      | 4.59%      | 471,585       | -264,650    | 43               | 69.77         |
| 2013 | 406,493.5    | 9.91%      | 572,755.5     | -166,262    | 41               | 78.05         |
| 2012 | 93,719       | 2.34%      | 667,619       | -573,900    | 61               | 63.93         |
| 2011 | 605,044      | 17.77%     | 998,448       | -393,404    | 64               | 75.00         |
| 2010 | 390,697.5    | 12.96%     | 795,043.5     | -404,346    | 56               | 75.00         |
| 2009 | 81,664       | 2.78%      | 782,413       | -700,749    | 67               | 73.13         |
| 2008 | 636,231.5    | 27.71%     | 1,059,442     | -423,210.5  | 64               | 78.13         |
| 2007 | 778,847.5    | 51.33%     | 1,036,661.5   | -257,814    | 68               | 83.82         |
| 2006 | 100,237      | 7.07%      | 220,437       | -120,200    | 27               | 70.37         |
| 2005 | 56,728.5     | 4.17%      | 104,878.5     | -48,150     | 17               | 64.71         |
| 2004 | 30,852.5     | 2.32%      | 276,162.5     | -245,310    | 42               | 69.05         |
| 2003 | 176,169      | 15.28%     | 423,363.5     | -247,194.5  | 69               | 73.91         |
| 2002 | 153,234.5    | 15.32%     | 294,494.5     | -141,260    | 41               | 85.37         |
---

### 📊 Performance Ratios

| Ratio                            | Value       |
|----------------------------------|-------------|
| Upside Potential Ratio           | 126.45      |
| Annual Sharpe Ratio              | 1.25        |
| Sortino Ratio                    | 0.64        |
| Calmar Ratio                     | 0.05        |
| Sterling Ratio                   | 0.002       |
---
### 📊 Profitability Ratios

| Metric                             | All Trades   | Long Trades  | Short Trades  |
|-----------------------------------|--------------|--------------|---------------|
| Profit Factor                 | 1.66        | 1.67        | 1.64        |
| Adjusted Profit Factor        | 1.53        | 1.50        | 1.44        |
| Specific Profit Factor        | 1.86 | 1.56 | 2.39 |
| Max Position Size             | 5 | 5 | 5 |
| Slippage Paid                 | 449,000 | 313,100 | 135,900 |
| Commission Paid               | 0 | 0 | 0 |
| Unrealized PnL                | n/a | n/a | n/a |


### 📊 Annual and Monthly Return Metrics

| Metric                            | All Trades      | Long Trades     | Short Trades    |
|----------------------------------|------------------|------------------|------------------|
| **Annual Return (%)**            | 31.08%           | 15.76%           | 15.32%           |
| **Monthly Return (%)**           | 2.59%            | 1.31%            | 1.28%            |
| **Buy & Hold Return**            | 1,026,457.75     | 1,026,457.75     | 1,088,326.13     |
| **Average Monthly Return**       | 25,865.97        | -                | -                |
| **Monthly Return Std Dev**       | 74,902.94        | -                | -                |

### 📊 Risk Metrics
| Metric                                 | All Trades     | Long Trades   | Short Trades  |
|----------------------------------------|----------------|---------------|---------------|
| **Maximum Strategy Drawdown**          | -443,650       | -447,305      | -476,383.5    |
| **Max Strategy Drawdown (%)**          | -10.49%        | -10.30%       | -20.21%       |
| **Maximum Closed Trade Drawdown**      | -427,300       | -433,705      | -394,956      |
| **Max Closed Trade Drawdown (%)**      | -8.94%         | -10.01%       | -16.39%       |
---
### 📊 Trade Summary

- **Total Number of Trades:** 1396  
  - Long: 775  
  - Short: 621  
- **Win Rate:**  
  - All: 72.71%  
  - Long: 68.77%  
  - Short: 77.62%
---
### 📊 Return-to-Drawdown Ratios

| Metric | Value |
|--------|-------|
| Net Profit / Max Drawdown (%) | **4911.71%** |
| Net Profit / Max Trade Drawdown (%) | **4925.16%** |
| Net Profit / Max Strategy Drawdown (%) | **1620.81%** |
| Specific Net Profit / Max Drawdown (%) | **3839.67%** |
| Specific Net Profit / Max Trade Drawdown (%) | **3850.19%** |
| Specific Net Profit / Max Strategy Drawdown (%) | **1267.05%** |
| Adjusted Net Profit / Max Drawdown (%) | **4137.79%** |
| Adjusted Net Profit / Max Trade Drawdown (%) | **4149.13%** |
| Adjusted Net Profit / Max Strategy Drawdown (%) | **1365.43%** |
---
### 📊 General Performance Metrics

| Metric                 | All Trades       | Long              | Short             |
|:----------------------|-----------------:|------------------:|------------------:|
| Net Profit            | 7,190,739.5      | 3,645,400.5       | 3,545,339         |
| Gross Profit          | 18,163,542       | 9,089,353.5       | 9,074,188.5       |
| Gross Loss            | -10,972,802.5    | -5,443,953        | -5,528,849.5      |
| Adjusted Net Profit   | 6,057,724.974    | 2,901,746.344     | 2,661,374.115     |
| Adjusted Gross Profit | 17,593,420.37    | 8,695,649.897     | 8,660,870.54      |
| Adjusted Gross Loss   | -11,535,695.39   | -5,793,903.553    | -5,999,496.424    |
| Selective Net Profit  | 5,621,281        | 2,353,907.5       | 3,267,373.5       |
| Selective Gross Profit| 12,149,743       | 6,539,568.5       | 5,610,174.5       |
| Selective Gross Loss  | -6,528,462       | -4,185,661        | -2,342,801        |
| Capital Required      | 427,300          | 433,705           | 394,956           |
| Account Return (%)    | 1,682.83         | 840.53            | 897.65            |
| Initial Capital Return| 719.07           | 364.54            | 354.53            |
---
### ⏱️ Time Analysis

| Metric                           | Value                         |
|----------------------------------|-------------------------------|
| Trading Period                   | 23 Years, 2 Months, 14 Days   |
| Strategy Time in Market (%)      | 18.40%                        |
| Longest Flat Period              | 2 Months, 16 Days             |
| Max Profit Date                  | 2015/08/21                    |
| Max Drawdown Date                | 2021/02/22                    |
---
## 📈 NAV (Since June 2001)


---
## 📈 Equity Curve (Since June 2001)


#### 📌 Notes

- *No strategy source code is included in this repository.*
- *Performance matrix updated from MultiCharts outputs. Profits are in TWD.*
_Last updated: 2025-06-24_
---

© Strategy rationale remains proprietary.

