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
- **Sharpe Ratio** : 1.0537 **(From June 2001 to June 2025 -> 24 years backtested sharpe ratio)**
- **Annual Return** : 29.54%
- **Maximum Drawdown** : -20.52%
- **Profit Factor** : 1.48
- **Win Rate (%)**: 56.41%

## 📌 Strategy Performance Report (Backtested Period : From June 2001 to June 2025)

This repository summarizes the performance of a trading strategy applied to Hang Seng Index Futures (HSI), highlighting core performance metrics, risk statistics, and trade breakdown.

## 📊 Performance Ratios

| Ratio                            | Value       |
|----------------------------------|-------------|
| Upside Potential Ratio           | 126.45      |
| Sharpe Ratio                     | 0.36        |
| Annualized Sharpe Ratio          | 1.25        |
| Sortino Ratio                    | 0.64        |
| Calmar Ratio                     | 0.05        |
| Sterling Ratio                   | 0.002       |
---
### 📊 Profitability Ratios

| Metric                             | All Trades   | Long Trades  | Short Trades  |
|-----------------------------------|--------------|--------------|---------------|
| Profit Factor                 | 1.66        | 1.67        | 1.64        |
| Adjusted Profit Factor        | 1.53        | 1.50        | 1.44        |


| Annual Return (%)             | 31.08       | 15.76       | 15.32       |
| Monthly Return (%)            | 2.59        | 1.31        | 1.28        |



| Net Profit / Max Drawdown (%)    | 4911.71     |
| Adj. Net Profit / Max Strategy DD | 1365.43     |

---
## ⚙️ Strategy Performance Summary

| Metric                         | All Trades  | Long Only   | Short Only  |
|--------------------------------|-------------|-------------|-------------|
| Net Profit (NTD)              | 7,190,739.5 | 3,645,400.5 | 3,545,339   |
| Gross Profit                  | 18,163,542  | 9,089,353.5 | 9,074,188.5 |
| Gross Loss                    | -10,972,802.5 | -5,443,953 | -5,528,849.5 |
| Adjusted Net Profit           | 6,057,724.97 | 2,901,746.34 | 2,661,374.12 |

| Win Rate (%)                  | 72.71       | 68.77       | 77.62       |
| Total Trades                  | 1396        | 775         | 621         |

| Max Drawdown (%)              | -10.49      | -10.30      | -20.21      |
| Max Strategy Drawdown (NTD)   | -443,650    | -447,305    | -476,383.5  |


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

## 📈 Key Ratios

| Metric | Value |
|--------|-------|
| Max Drawdown Efficiency (Net/Drawdown %) | 4911.71% |
| Adjusted Net Profit / Max Strategy Drawdown % | 1365.43% |
| Specific Profit Factor | 1.86 |
| Adjusted Profit Factor | 1.53 |
| Capital Required | 427,300 |
| ROI on Account Size | 1,682.83% |
| Slippage Paid | 449,000 |
| Commission Paid | 0 |

---



> ⚙️ This performance is based on MultiCharts live position logs from 2001 to 2025, updated daily via GitHub Actions.

### 📊 Profitability Ratios

| Metric                             | All Trades   | Long Trades  | Short Trades  |
|-----------------------------------|--------------|--------------|---------------|
| **Profit Factor**                 | 1.48         | 1.63         | 1.34          |
| **Adjusted Profit Factor**        | 1.39         | 1.49         | 1.22          |
| **Specific Profit Factor**        | 1.55         | 1.59         | 1.50          |
| **Max Contracts Held**            | 5            | 3            | 5             |
| **Slippage Paid**                 | 767,000      | 331,500      | 435,500       |
| **Commission Paid**               | 0            | 0            | 0             |
| **Unrealized P&L**                | 32,800       | n/a          | 32,800        |

### 📊 Annual and Monthly Return Metrics

| Metric                             | Value        |
|-----------------------------------|--------------|
| **Annualized Return (%)**         | 29.54        |
| **Monthly Return (%)**            | 2.46         |
| **Average Monthly Return ($)**    | 49,323.18    |
| **Standard Deviation of Monthly Returns** | 165,705.49 |
| **Buy-and-Hold Return ($)**       | 6,762,849.05 |
---
### 📊 Risk Metrics

| Metric                             | All Trades   | Long Trades  | Short Trades  |
|-----------------------------------|--------------|--------------|---------------|
| **Max Strategy Drawdown**         | -2,136,700   | -1,187,800   | -1,282,500    |
| **Max Strategy Drawdown (%)**     | -20.52%      | -31.71%      | -16.56%       |
| **Max Closed Trade Loss**         | -1,799,100   | -1,093,100   | -885,500      |
| **Max Closed Trade Loss (%)**     | -18.68%      | -29.52%      | -14.85%       |
| **Return After Drawdown**         | 6.66         | 7.67         | 3.99          |
---
### 📊 Trade Summary

- **Total Number of Trades:** 2,005  
  - Long: 1,006  
  - Short: 999  
- **Win Rate:**  
  - All: 56.41%  
  - Long: 57.16%  
  - Short: 55.66%
---
### 📊 Return-to-Drawdown Ratios

| Ratio Description                                                                                  | Value         |
|----------------------------------------------------------------------------------------------------|---------------|
| Net Profit / Max Loss (%)                                                                          | 2875.96       |
| Net Profit / Max Closed Trade Drawdown (%)                                                         | 2276.91       |
| Net Profit / Max Strategy Drawdown (%)                                                             | 665.59        |
| Specific Net Profit / Max Loss (%)                                                                 | 2013.93       |
| Specific Net Profit / Max Closed Trade Drawdown (%)                                                | 1594.44       |
| Specific Net Profit / Max Strategy Drawdown (%)                                                    | 466.09        |
| Adjusted Net Profit / Max Loss (%)                                                                 | 2410.26       |
| Adjusted Net Profit / Max Closed Trade Drawdown (%)                                                | 1908.22       |
| Adjusted Net Profit / Max Strategy Drawdown (%)                                                    | 557.81        |
---

### 📊 General Performance Metrics

| Metric                             | All Trades   | Long Trades  | Short Trades  |
|-----------------------------------|--------------|--------------|---------------|
| **Net Profit**                    | 14,221,600   | 9,107,900    | 5,113,700     |
| **Gross Profit**                  | 43,736,400   | 23,487,800   | 20,248,600    |
| **Gross Loss**                    | -29,514,800  | -14,379,900  | -15,134,900   |
| **Net Profit (Adjusted)**         | 11,918,720.73| 7,434,122.92 | 3,531,794.59  |
| **Gross Profit (Adjusted)**       | 42,435,895.89| 22,508,291.03| 19,389,868.08 |
| **Gross Loss (Adjusted)**         | -30,517,175.16| -15,074,168.11| -15,858,073.50|
| **Specific Net Profit**           | 9,958,900    | 5,579,500    | 4,379,400     |
| **Specific Gross Profit**         | 28,141,100   | 14,992,700   | 13,148,400    |
| **Specific Gross Loss**           | -18,182,200  | -9,413,200   | -8,769,000    |
| **Required Capital**              | 1,799,100    | 1,093,100    | 885,500       |
| **Account Return (%)**            | 790.48%      | 833.22%      | 577.49%       |
| **Return on Initial Capital (%)** | 711.08%      | 455.39%      | 255.69%       |

---
## 📈 NAV (Since June 2001)

![NAV_Dynamic Bivariate Regression Model](https://github.com/user-attachments/assets/71c4f968-4615-4fcf-8514-9f48c271443d)
---
## 📈 Equity Curve (Since June 2001)

![EquityCurve_Dynamic Bivariate Regression Model](https://github.com/user-attachments/assets/20feb853-ac5f-4681-8eef-bd6b5db079e2)

## 📋 Recent Daily Positions at 13:45

This table shows the position size for each day at exactly 13:45.

Data is available in: `data/recent_1345_positions.csv`

## 🔄 Data Source

Data is exported from MultiCharts in CSV format.

## 📁 Files

- `data/pos_TXFstrategyA.csv`: Full position export  
- `data/recent_1345_positions.csv`: Latest 13:45 positions  
- `images/position_plot_english_fixed.png`: Position time series plot  
- `scripts/update_position.py`: Python script for plotting and extraction  
