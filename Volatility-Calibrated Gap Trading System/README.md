## 📈 Volatility-Calibrated Gap Trading System

### 📌 Strategy Rationale

**The Volatility-Calibrated Gap Trading System is a gap-sensitive intraday trading model for Hang Seng Index Futures, integrating dual-mode logic for gap reversion and gap breakout. Combined multi-timeframe momentum filters, day/week structural context, and volatility-based entry adaptation to optimize signal quality and trading frequency across the session.**

*This README was automatically generated as part of a real-time strategy monitoring and reporting system. (Real-time strategy starts from March 2024 utill now)*

### 📌 Strategy Attributes

- **Strategy Name: Volatility-Calibrated Gap Trading System**  
- **Asset : Hang Seng Index Futures (HSI)**  
- **Type : Quantitative Intraday Strategy**  
- **Rolling Frequency : 5-minute bars**  
- **Holding Time : Intraday**
- **Strategy Time in Market (%) : 5.06%** 
- **Backtested Period : From July 2001 to June 2025** *(To evaluate whether the strategy can remain robust under all-weather market conditions.)*

⭐️ **Key Highlight:**
#### *Why Full-History Backtesting?*
#### (1) *The strategy is tested over the full historical dataset to capture a wide range of market regimes and ensure its resilience under different volatility, correlation, and macro cycles.*
#### (2) *The system incorporates a rolling logic core, allowing continuous internal adaptation without the need for manual parameter tuning—this reinforces the “all-weather” thesis.*

### 📌 Strategy Overview

This table provides a comprehensive summary of the trading strategy based on live and backtested data, covering both long and short trades. **Just wanna mentioned here, the numbers presented here desire to reflect the real and true performance without any manipulation.**

Key performance metrics include :

- ✅ **Annual Return** : 152%
- ✅ **Sharpe Ratio : 1.24 (From June 2001 to June 2025 -> 24 years backtested sharpe ratio)**
- Maximum Drawdown : -18.12% 
- Profit Factor : 1.54 
- Win Rate (%) : 49.6243%
 
### 📌 Strategy Performance Report (Backtested Period : From July 2001 to June 2025)

This repository summarizes the performance of a trading strategy applied to Hang Seng Index Futures (HSI), highlighting core performance metrics, risk statistics, and trade breakdown.

#### 📊 Annual Performance Overview (HKD-Based)
This section outlines the annual performance of the strategy from 2001 to 2025, measured in HKD.

| Year | Net Profit (HK$) | Return (%) | Gross Profit | Gross Loss | No. of Trades | Win Rate (%) |
|------|------------------|------------|--------------|-------------|----------------|---------------|
| 2025 | 145,864          | 4.0565     | 298,230      | -152,366    | 81             | 51.85         |
| 2024 | 87,357.5         | 2.4899     | 446,010      | -358,652.5  | 170            | 45.88         |
| 2023 | 72,683           | 2.1155     | 476,820      | -404,137    | 186            | 45.70         |
| 2022 | 196,092          | 6.0528     | 732,949      | -536,857    | 211            | 48.34         |
| 2021 | 277,006          | 9.3499     | 635,088.5    | -358,082.5  | 175            | 46.29         |
| 2020 | 186,623          | 6.7226     | 628,730      | -442,107    | 183            | 46.45         |
| 2019 | 143,727          | 5.4601     | 446,130      | -302,403    | 143            | 49.65         |
| 2018 | 165,328.5        | 6.7016     | 586,100      | -420,771.5  | 160            | 50.00         |
| 2017 | 66,251.5         | 2.7596     | 171,210      | -104,958.5  | 84             | 45.24         |
| 2016 | 121,278.5        | 5.3205     | 382,900      | -261,621.5  | 156            | 48.72         |
| 2015 | 297,496          | 15.0102    | 558,580      | -261,084    | 138            | 42.75         |
| 2014 | 72,448           | 3.7941     | 265,850      | -193,402    | 110            | 45.45         |
| 2013 | 11,394           | 0.6003     | 263,625      | -252,231    | 117            | 41.88         |
| 2012 | 67,850.5         | 3.7071     | 263,290      | -195,439.5  | 130            | 47.69         |
| 2011 | 72,841           | 4.1447     | 435,795      | -362,954    | 162            | 46.91         |
| 2010 | 65,027           | 3.8423     | 342,710      | -277,683    | 134            | 50.00         |
| 2009 | 315,928          | 22.9520    | 644,577      | -328,649    | 154            | 57.79         |
| 2008 | 317,717          | 30.0085    | 924,299.5    | -606,582.5  | 147            | 53.06         |
| 2007 | 548,225          | 107.3830   | 844,590      | -296,365    | 149            | 60.40         |
| 2006 | 81,820           | 19.0851    | 175,600      | -93,780     | 103            | 52.43         |
| 2005 | 18,493.5         | 4.5082     | 94,260       | -75,766.5   | 93             | 43.01         |
| 2004 | 118,879.5        | 40.8045    | 232,995      | -114,115.5  | 136            | 61.76         |
| 2003 | 96,411.5         | 49.4601    | 221,160      | -124,748.5  | 123            | 55.28         |
| 2002 | 29,576.5         | 17.8870    | 195,520      | -165,943.5  | 138            | 48.55         |
| 2001 | 65,351.5         | 65.3515    | 166,998.5    | -101,647    | 77             | 59.74         |
---
### 📊 Performance Ratios

| Metric Description                                                                 | Value         |
|------------------------------------------------------------------------------------|---------------|
| Upside Potential Ratio                                                             | 160.2158947   |
| Annual Sharpe Ratio                                                                | 1.241336803   |
| Sortino Ratio                                                                      | 0.84828949    |
| Fouse Ratio                                                                        | 0.012585417   |
| Calmar Ratio                                                                       | 0.046519399   |
| Sterling Ratio                                                                     | 0.001951264   |

### 📊 Profitability Ratios

| Metric                                    | All Trades   | Long Trades  | Short Trades  |
| Profit Factor                             | 1.5361         | 1.5894        | 1.5010        |
| Adjusted Profit Factor                    | 1.4640         | 1.4722        | 1.4110        |
| Specified Profit Factor                   | 1.6367         | 1.8461        | 1.5101        |
| Max Position Size                        | 1              | 1             | 1             |
| Slippage Cost                             | 350,240        | 129,470       | 220,770       |
| Commission Paid                           | 0              | 0             | 0             |
| Unrealized P&L                            | n/a            | n/a           | n/a           |

### 📊 Annual and Monthly Return Metrics

| Metric                            | All Trades      | Long Trades     | Short Trades    |
|----------------------------------|------------------|------------------|------------------|
| **Annual Return (%)**            | 151.9963%      | 66.4715%      | 85.5249%      |
| **Monthly Return (%)**            | 12.6664%       | 5.5393%       | 7.1271%       |
| **Buy & Hold Benchmark**             | 81,313.63      | 92,843.19     | 81,313.63     |
| **Average Monthly Return**         | 12,644.69      | -             | -             |
| **Std. Dev. of Monthly Return**       | 25,614.48      | -             | -             |

### 📊 Risk Metrics
| Metric                                 | All Trades     | Long Trades   | Short Trades  |
|----------------------------------------|----------------|---------------|---------------|
| Max Strategy Drawdown                     | -106,880       | -113,443.5    | -95,834       |
| Max Strategy Drawdown (%)                 | -18.1241%      | -30.7676%     | -20.5632%     |
| Max Closed Trade Drawdown                 | -95,940        | -100,865      | -89,124       |
| Max Closed Trade Drawdown (%)             | -16.4166%      | -27.0360%     | -19.1547%     |
---
### 📊 Trade Summary

- **Total Number of Trades:** 3,460   
  - Long: 1,363  
  - Short: 2,097  
- **Win Rate:**  
  - All: 49.6243%  
  - Long: 51.4307% 
  - Short: 48.4502% 
---
### 📊 Return-to-Drawdown Ratios

| Ratio Description                                                                  | Value         |
|------------------------------------------------------------------------------------|---------------|
| Net Profit / Max Loss (%)                                                          | 11,622.28924  |
| Net Profit / Max Closed Trade Drawdown (%)                                         | 11,597.67516  |
| Net Profit / Max Strategy Drawdown (%)                                             | 3,407.251123  |
| Specified Net Profit / Max Loss (%)                                                | 7,854.71939   |
| Specified Net Profit / Max Closed Trade Drawdown (%)                              | 7,838.084395  |
| Specified Net Profit / Max Strategy Drawdown (%)                                   | 2,302.730632  |
| Adjusted Net Profit / Max Loss (%)                                                 | 10,299.42371  |
| Adjusted Net Profit / Max Closed Trade Drawdown (%)                                | 10,277.61124  |
| Adjusted Net Profit / Max Strategy Drawdown (%)                                    | 3,019.432942  |
---
### 📊 General Performance Metrics

| Metric                                    | All Trades     | Long Trades   | Short Trades  |
|------------------------------------------|----------------|---------------|---------------|
| Net Profit                                | 3,641,670      | 1,592,585     | 2,049,085     |
| Gross Profit                              | 10,434,017.5   | 4,294,620     | 6,139,397.5   |
| Gross Loss                                | -6,792,347.5   | -2,702,035    | -4,090,312.5  |
| Adjusted Net Profit                       | 3,227,169.93   | 1,325,361.87  | 1,732,068.31  |
| Adjusted Gross Profit                     | 10,182,211.3   | 4,132,414.44  | 5,946,787.47  |
| Adjusted Gross Loss                       | -6,955,041.38  | -2,807,052.57 | -4,214,719.16 |
| Specified Net Profit                      | 2,461,158.5    | 1,232,670     | 1,228,488.5   |
| Specified Gross Profit                    | 6,326,531      | 2,689,555     | 3,636,976     |
| Specified Gross Loss                      | -3,865,372.5   | -1,456,885    | -2,408,487.5  |
| Required Account Size                     | 95,940         | 100,865       | 89,124        |
| Account Return (%)                        | 3,795.78%      | 1,578.93%     | 2,299.14%     |
| Initial Capital Return (%)                | 3,641.67%      | 1,592.59%     | 2,049.08%     |
---
### ⏱️ Time Analysis

| Metric Description                          | Value                                   |
|---------------------------------------------|-----------------------------------------|
| Total Trading Period                        | 24 Yrs, 9 Dys                           |
| Strategy Time in Market (%)                 | 5.061564393                             |
| Longest Flat Period                         | 23 Dys, 18 Hrs, 25 Mins                 |
| Max Profit Date                             | 2007/10/3                               |
| Max Loss Date                               | 2007/8/21                               |
---
## 📈 NAV (Since June 2001)


---
## 📈 Equity Curve (Since June 2001)


## 📌 Notes

- *No strategy source code is included in this repository.*
- *Performance matrix updated from MultiCharts outputs. Profits are in HKD.*
_Last updated: 2025-06-24_

