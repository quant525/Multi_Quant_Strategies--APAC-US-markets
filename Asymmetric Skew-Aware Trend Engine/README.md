# 📈 Asymmetric Skew-Aware Trend Engine

## 📌 Strategy Rationale

**The Asymmetric Skew-Aware Trend Engine Strategy is a swing trading model applied to the Hang Seng Index Futures, integrating multi-layered momentum signals with volatility and skew-adjusted capital scaling.**

⭐️ **Key Highlight:**
#### *Strategy Advantage*
#### What distinguishes this strategy is not just its signal quality, but its dynamic adaptability. Rather than relying on rigid thresholds, the system continuously reevaluates market conditions to decide whether the current environment is statistically suitable for signal activation. This reverses the common approach: instead of forcing trades into static templates, the strategy listens to the market and only acts when the structural context aligns with its core logic.

*This README was automatically generated as part of a real-time strategy monitoring and reporting system. (Real-time strategy starts from March 2024 utill now)*

## 📌 Strategy Attributes

- **Strategy Name: Asymmetric Skew-Aware Trend Engine**  
- **Asset : Hang Seng Index Futures (HSI)**  
- **Type : Multi-factor Momentum with Volatility Structure Filtering**  
- **Rolling Frequency : 15-minute bars**  
- **Typical Holding Time : 2 to 3 days**
- **Backtested Period : From June 2001 to June 2025** *(In order to test if the strategy can survive under All-weather conditions)*

⭐️ **Key Highlight:**
#### *Why Full-History Backtesting?*
#### (1) *The strategy is tested over the full historical dataset to capture a wide range of market regimes and ensure its resilience under different volatility, correlation, and macro cycles.*
#### (2) *The system incorporates a rolling logic core, allowing continuous internal adaptation without the need for manual parameter tuning—this reinforces the “all-weather” thesis.*

## 📌 Strategy Overview

This table provides a comprehensive summary of the trading strategy based on live and backtested data, covering both long and short trades.

Key performance metrics include :

🌟 **Important Note:** **Just wanna mentioned here, the numbers presented here desire to reflect the real and true performance without any manipulation.**
- **Sharpe Ratio : 1.25 (From June 2001 to June 2025 -> 24 years backtested sharpe ratio)**
- **Annual Return** : 31.08%
- **Maximum Drawdown** : -10.49%
- **Profit Factor** : 1.66 
- **Win Rate (%)**: 72.71%

## 📌 Strategy Performance Report (Backtested Period : From June 2001 to June 2025)

This repository summarizes the performance of a trading strategy applied to Hang Seng Index Futures (HSI), highlighting core performance metrics, risk statistics, and trade breakdown.

## 📊 Performance Ratios

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
## ⏱️ Time Analysis

| Metric                           | Value                         |
|----------------------------------|-------------------------------|
| Trading Period                   | 23 Years, 2 Months, 14 Days   |
| Strategy Active Period           | 4 Years, 3 Months             |
| Longest Flat Period              | 2 Months, 16 Days             |
| Max Profit Date                  | 2015/08/21                    |
| Max Drawdown Date                | 2021/02/22                    |
---
## 📈 NAV (Since June 2001)


---
## 📈 Equity Curve (Since June 2001)


## 📌 Notes

- No strategy source code is included in this repository.
- Performance matrix updated from MultiCharts outputs.
_Last updated: 2025-06-24_
