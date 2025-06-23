# 📈 Dynamic Bivariate Regression Trading Strategy
 
This strategy is based on a Dynamic Bivariate Regression Model that captures evolving relationships between two market variables, using rolling 30-minute intervals to forecast short-term directional movement on the Taiwan Index Futures.

*This README was automatically generated as part of a real-time strategy monitoring and reporting system. (Real-time strategy starts from March 2024 utill now)*

## 📌 Strategy Attributes

- **Strategy Name:** Dynamic Bivariate Regression Strategy  
- **Asset:** Taiwan Index Futures (TXF)  
- **Type:** Statistical Forecasting Model  
- **Rolling Frequency:** 30-minute bars  
- **Typical Holding Time:** 2 to 3 days
- **Backtested Period:** From June 2001 to June 2025 *(In order to test if the strategy can survive under All-weather conditions)*

⭐️ **Key Highlight:**
**The reason why I didn't consider In sample/Out Sample type of test is to prove that the strategy is itself enough robust without changing any parameters throughout the whole dataset.**

## 📌 Strategy Overview

This table provides a comprehensive summary of the trading strategy based on live and backtested data, covering both long and short trades.

Key performance metrics include :

🌟 **Important Note:** **Just wanna mentioned here, the numbers presented here desire to reflect the real and true performance without any manipulation.**
- **Sharpe Ratio** : 1.0537 **(From June 2001 to June 2025 -> 24 years backtested sharpe ratio)**
- **CAGR (Annualized Return)** : 29.54%
- **Maximum Drawdown** : -20.52%
- **Profit Factor** : 1.48
- **Win Rate (%)**: 56.41%

## 📌 Strategy Performance Report (Backtested Period : From June 2001 to June 2025)

This repository summarizes the performance of a trading strategy applied to Taiwan Index Futures (TXF), highlighting core performance metrics, risk statistics, and trade breakdown.

### 📊 Performance Ratios

| Metric Description                                                                 | Value         |
|------------------------------------------------------------------------------------|---------------|
| **Upside Potential Ratio**                                                        | 61.8100       |
| **Sharpe Ratio**                                                                  | 0.3042        |
| **Annualized Sharpe Ratio**                                                       | 1.0537        |
| **Sortino Ratio**                                                                 | 0.3582        |
| **Fouse Ratio**                                                                   | 0.0068        |
| **Calmar Ratio**                                                                  | 0.0232        |
| **Sterling Ratio**                                                                | 0.0020        |
---
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
### 📊 Core Metrics

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
