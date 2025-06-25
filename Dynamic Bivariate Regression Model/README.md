## 📈 Dynamic Bivariate Regression Regime-Switching Trading Strategy

## 📌 Strategy Rationale

**The  Dynamic Bivariate Regression Strategy is a Regime-Switching and hybrid model (Combining Trend-Following and Statistical Mean-Reversion) designed for the Taiwan Index Futures (TXF) market. It dynamically adjusts its entry and exit logic based on the autocorrelation structure of regression residuals between actual market prices and a predicted regression line.**

This regime-adaptive structure allows the strategy to benefit from both trend-following  and statistical mean-reversion regimes based on regression residuals and confidence intervals, improving robustness across different market conditions.

⭐️ **Key Highlight:**
#### *Strategy Advantage*
#### What distinguishes this strategy is not just its signal quality, but its dynamic adaptability. Rather than relying on rigid thresholds, the system continuously reevaluates market conditions to decide whether the current environment is statistically suitable for signal activation. This reverses the common approach: instead of forcing trades into static templates, the strategy listens to the market and only acts when the structural context aligns with its core logic.

*This README was automatically generated as part of a real-time strategy monitoring and reporting system. (The strategy has been live traded from March 2024 through the present.)*

## 📌 Strategy Attributes

- **Strategy Name: Dynamic Bivariate Regression Strategy**  
- **Asset : Taiwan Index Futures (TXF)**  
- **Type : Statistical Forecasting Model (Combining Trend-Following and Statistical Mean-Reversion)**  
- **Rolling Frequency : 30-minute bars**
- **Max Contracts Size : 5**     
- **Typical Holding Time : 2 to 3 days**
- **Strategy Time in Market (%)  : 50.36%**
- **Backtested Period : From June 2001 to June 2025** *(To evaluate whether the strategy can remain robust under all-weather market conditions.)*

⭐️ **Key Highlight:**
#### *Why Full-History Backtesting?*
#### (1) *The strategy is tested over the full historical dataset to capture a wide range of market regimes and ensure its resilience under different volatility, correlation, and macrocycles.*
#### (2) *The system incorporates a rolling logic core, allowing continuous internal adaptation without manual parameter tuning—this reinforces the “all-weather” thesis.*

## 📌 Strategy Overview

This table provides a comprehensive summary of the trading strategy based on live and backtested data, covering both long and short trades.

Key performance metrics include :

🌟 **Note:** **wanna mention here that the numbers presented here desire to reflect real and true performance without manipulation.**
- ✅ **Annual Return** : 29.54%
- ✅ **Profit Factor** : 1.48
- **Sharpe Ratio** : 1.0537 **(From June 2001 to June 2025 -> 24 years backtested sharpe ratio)**
- **Maximum Drawdown** : -20.52%
- **Win Rate (%)**: 56.41%

### 📌 Strategy Performance Report (Backtested Period : From June 2001 to June 2025)

This repository summarizes the performance of a trading strategy applied to Taiwan Index Futures (TXF), highlighting core performance metrics, risk statistics, and trade breakdown.

### 📊 Annual Performance (TWD-Based)

|   Year |       Net Profit |   Profit (%) |    Gross Profit |       Gross Loss |   Num Trades |   Win Rate (%) |
|-------:|-----------------:|-------------:|----------------:|-----------------:|-------------:|---------------:|
|   2025 |  877100          |     5.70386  |      2.7928e+06 |      -1.9157e+06 |           42 |        54.7619 |
|   2024 |       2.2691e+06 |    17.3105   |      5.1801e+06 |      -2.911e+06  |           85 |        58.8235 |
|   2023 |  297600          |     2.32308  |      2.0824e+06 |      -1.7848e+06 |           86 |        52.3256 |
|   2022 |       1.4209e+06 |    12.4753   |      2.7146e+06 |      -1.2937e+06 |           77 |        64.9351 |
|   2021 |  195800          |     1.74917  |      2.4745e+06 |      -2.2787e+06 |           64 |        53.125  |
|   2020 |       1.8727e+06 |    20.0908   |      2.9823e+06 |      -1.1096e+06 |           88 |        64.7727 |
|   2019 |  413200          |     4.63853  |      1.152e+06  | -738800          |           74 |        59.4595 |
|   2018 |  123400          |     1.40473  |      1.2206e+06 |      -1.0972e+06 |           69 |        55.0725 |
|   2017 |   89200          |     1.02583  | 724900          | -635700          |           80 |        53.75   |
|   2016 |  614400          |     7.60302  |      1.1992e+06 | -584800          |           69 |        55.0725 |
|   2015 |  580500          |     7.73948  |      1.3134e+06 | -732900          |           88 |        62.5    |
|   2014 |  281400          |     3.89799  | 762400          | -481000          |           58 |        51.7241 |
|   2013 |  375600          |     5.48842  | 927300          | -551700          |           69 |        55.0725 |
|   2012 |  173200          |     2.59658  | 960500          | -787300          |           72 |        58.3333 |
|   2011 |  115300          |     1.75896  |      1.7801e+06 |      -1.6648e+06 |          101 |        52.4752 |
|   2010 |  265100          |     4.21469  |      1.4006e+06 |      -1.1355e+06 |           82 |        57.3171 |
|   2009 |       1.2357e+06 |    24.449    |      2.3247e+06 |      -1.089e+06  |           89 |        57.3034 |
|   2008 |  773600          |    18.0722   |      2.1942e+06 |      -1.4206e+06 |           96 |        60.4167 |
|   2007 |   31200          |     0.734221 |      1.4995e+06 |      -1.4683e+06 |           83 |        56.6265 |
|   2006 |  648900          |    18.0225   |      1.1521e+06 | -503200          |           75 |        57.3333 |
|   2005 |  436900          |    13.8102   | 927500          | -490600          |           93 |        56.9892 |
|   2004 | -128000          |    -3.88869  |      1.835e+06  |      -1.963e+06  |          108 |        53.7037 |
|   2003 |  189600          |     6.11219  |      1.1294e+06 | -939800          |           90 |        54.4444 |
|   2002 |  451500          |    17.0345   |      1.9072e+06 |      -1.4557e+06 |          124 |        53.2258 |
|   2001 |  650500          |    32.525    |      1.2688e+06 | -618300          |           68 |        52.9412 |

### 📊 Performance Ratios

| Metric Description                                                                 | Value         |
|------------------------------------------------------------------------------------|---------------|
| **Upside Potential Ratio**                                                        | 61.8100       |
| **Annual Sharpe Ratio**                                                       | 1.0537        |
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
## 🕒 Time Analysis

| Metric                                | Value                             |
|---------------------------------------|------------------------------------|
| Trading Period                        | 24 Yrs, 1 Mth, 21 Dys              |
| Percentage of Time in Market (%)      | 50.36439971                        |
| Longest Flat (No Position) Period     | 1 Mth, 19 Dys, 1 Hr, 30 Mins       |
| Date of Maximum Profit                | 2024/11/29                         |
| Date of Maximum Loss                  | 2025/2/3                           |
---
## 📈 NAV (Since June 2001)

![NAV_Dynamic Bivariate Regression Model](https://github.com/user-attachments/assets/71c4f968-4615-4fcf-8514-9f48c271443d)
---
## 📈 Equity Curve (Since June 2001)

![EquityCurve_Dynamic Bivariate Regression Model](https://github.com/user-attachments/assets/20feb853-ac5f-4681-8eef-bd6b5db079e2)

#### 🔄 Data Source
Data is exported from MultiCharts in CSV format.
#### 📁 Files
- `data/pos_TXFstrategyA.csv`: Full position export  
- `data/recent_1345_positions.csv`: Latest 13:45 positions  
- `images/position_plot_english_fixed.png`: Position time series plot  
- `scripts/update_position.py`: Python script for plotting and extraction
#### 📌 Notes
- *No strategy source code is included in this repository.*
- *Performance matrix updated from MultiCharts outputs. Profits are in TWD.*
_Last updated: 2025-06-24_
---

© Strategy rationale remains proprietary.
