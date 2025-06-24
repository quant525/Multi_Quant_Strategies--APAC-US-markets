## 📈 Beta-Alpha Intermarket Trend Divergence Trading Strategy

### 📌 Strategy Rationale

**The Intermarket Trend Divergence strategy is a directional momentum model applied to Taiwan Index Futures (TXF), which exploits structural divergences between the Electronics Sector Index Futures (TE) and Financial Sector Index Futures (TF) sectors. This approach conceptually blends beta exposure with an alpha insight (relative value spread between sectors), creating a structural divergence-driven mechanism. Position sizing is dynamically adjusted using ATR for volatility-based exposure control.**


🌟 **Note:** 
*All results are based on real historical market data. Backtest coverage spans over 18 years, and *the strategy has been live traded on TXF for more than one year*. While different versions of the strategy have been deployed during live trading to meet institutional requirements, the core logic remains unchanged. The version presented here reflects a personally preferred configuration, selected for its clarity and transparency in performance representation.*

*This README was automatically generated as part of a real-time strategy monitoring and reporting system.*

### 📌 Strategy Attributes

- **Strategy Name : Intermarket Trend Divergence Model**  
- **Asset : Taiwan Index Futures (TXF)**    
- **Type : Directional Alpha Model (Relative Strength)**  
- **Data Frequency : 30-minute bars**  
- **Holding Duration : 3 to 6 days**
- **Max Contracts Size : 19**
- **Market Time :**
- **Backtested Period : From April 2007 to June 2025** *(In order to test if the strategy can survive under All-Weather conditions)*
> Note: Profit is represented in local currency (HSI).
⭐️ **Key Highlight:**
#### *Why Full-History Backtesting?*
#### (1) *The strategy is tested over the full historical dataset to capture a wide range of market regimes and ensure its resilience under different volatility, correlation, and macro cycles.*
#### (2) *The system incorporates a rolling logic core, allowing continuous internal adaptation without the need for manual parameter tuning—this reinforces the “all-weather” thesis.*

### 📌 Strategy Overview

This table provides a comprehensive summary of the trading strategy performance based on real data, covering both long and short trades.

Key performance metrics include :

🌟 **Important Note:** **Just wanna mentioned here, the numbers presented here desire to reflect the real and true performance without any manipulation.**
- **Sharpe Ratio** : **1.4671**
- **Annual Return** : **16.16%**
- **Maximum Drawdown** : -13.39%
- **Profit Factor** : ***2.91***
- **Win Rate (%)**: ***78.57%***


### 📌 Strategy Performance Report (Backtested Period : From April 2007 to June 2025)

This repository summarizes the performance of a trading strategy applied to Taiwan Index Futures (TXF), highlighting core performance metrics, risk statistics, and trade breakdown.

### 📊 Annual Performance (TWD-Based)

| Year | Net Profit (¤) | Return (%) | Gross Profit (¤) | Gross Loss (¤) | Number of Trades | Win Rate (%) |
|------|----------------|-------------|------------------|----------------|------------------|---------------|
| 2025 | 1,418,600      | 3.730448411 | 1,543,200        | -124,600       | 14               | 78.57142857   |
| 2024 | 1,280,300      | 3.484065496 | 3,889,200        | -2,608,900     | 19               | 63.15789474   |
| 2023 | 2,345,100      | 6.81671521  | 2,856,000        | -510,900       | 25               | 84.0          |
| 2022 | 1,304,300      | 3.9407334   | 2,004,300        | -700,000       | 27               | 70.37037037   |
| 2021 | 1,085,900      | 3.392165438 | 2,429,100        | -1,343,200     | 26               | 76.92307692   |
| 2020 | 267,200        | 0.841712658 | 2,098,200        | -1,831,000     | 21               | 76.19047619   |
| 2019 | 3,115,100      | 10.8806589  | 4,386,500        | -1,271,400     | 33               | 78.78787879   |
| 2018 | 2,970,500      | 11.5767444  | 4,258,100        | -1,287,600     | 36               | 75.0          |
| 2017 | 2,089,800      | 8.866581245 | 2,775,600        | -685,800       | 19               | 73.68421053   |
| 2016 | 1,970,500      | 9.12314979  | 2,322,700        | -352,200       | 20               | 85.0          |
| 2015 | 708,100        | 3.38953032  | 1,483,900        | -775,800       | 26               | 76.92307692   |
| 2014 | 2,669,800      | 14.65232424 | 3,253,800        | -584,000       | 22               | 86.36363636   |
| 2013 | 1,930,700      | 11.85183821 | 2,604,500        | -673,800       | 15               | 80.0          |
| 2012 | 1,088,300      | 7.158926457 | 1,298,700        | -210,400       | 16               | 75.0          |
| 2011 | -45,200        | -0.296447872| 1,115,000        | -1,160,200     | 25               | 68.0          |
| 2010 | 2,109,200      | 16.05419394 | 2,554,300        | -445,100       | 27               | 85.18518519   |
| 2009 | 818,900        | 6.64740119  | 858,000          | -39,100        | 15               | 86.66666667   |
| 2008 | 600,400        | 5.123435193 | 1,431,000        | -830,600       | 25               | 76.0          |
| 2007 | 1,718,700      | 17.187      | 1,829,500        | -110,800       | 24               | 95.83333333   |
---

### 📊 Performance Ratios

| Metric Description                                                  | Value         |
|--------------------------------------------------------------------|---------------|
| **Upside Potential Ratio**                                         | 143.72        |
| **Annual Sharpe Ratio**                                        | 1.4671        |
| **Sortino Ratio**                                                  | 0.5451        |
| **Fouse Ratio**                                                    | 0.0062        |
| **Calmar Ratio**                                                   | 0.0593        |
| **Sterling Ratio**                                                 | 0.0020        |
---
### 📊  Profitability Ratios

| Metric                                  | All Trades   | Long Trades   | Short Trades   |
|----------------------------------------|--------------|---------------|----------------|
| **Profit Factor**                          | **2.9108**  | **4.5302**   | 1.8243    |
| Adjusted Profit Factor                 | **2.4945**  | **3.6521**   | 1.4641    |
| Specific Profit Factor                 | 2.9336  | 2.9964   | 2.8678    |
| Max Contracts Size        | 19           | 18            | 19             |
| Slippage Paid                          | 1469000      | 774000        | 695000         |
| Commission Paid                        | 0            | 0             | 0              |
| Unrealized P&L                         | n/a          | n/a           | n/a            |

### 📊 Annual and Monthly Return Metrics

| Metric                                  | Value        |
|----------------------------------------|--------------|
| **Annual Return (%)**                  | 16.1558  | 
| Monthly Return (%)                         | 1.3463  | 
| **Buy-and-Hold Return ($)**                    | **17440122**  | 
| **Strategy Net Profit ($)**                    | **29446200**   |      
| Average Monthly Return ($)                 | 135074  |     
| Standard Deviation of Monthly Returns  | 333431.9566  | 

### 📊 Risk Metrics

| Metric                             | All Trades   | Long Trades  | Short Trades  |
|-----------------------------------|--------------|--------------|---------------|
| Maximum Strategy Drawdown              | -3304000     | -3304000      | -2962200       |
| **Maximum Strategy Drawdown (%)**          | -13.38540569 | -15.79380103  | -16.90685874   |
| Maximum Closed Trade Loss              | -989600      | -839800       | -2003700       |
| Maximum Closed Trade Loss (%)          | -5.001412359 | -2.648359203  | -11.67419233   |
| Return After Maximum Strategy Drawdown | 8.912288136  | 6.61125908    | 2.566538384    |
---
### 📊 Trade Summary

- **Total Number of Trades:** 434  
  - Long: 242
  - Short: 192  
- **Win Rate:**  
  - **All : 78.57%**  
  - **Long: 82.23%**  
  - **Short: 73.96%**
---
### 📊 Core Metrics

| Metric                                 | All Trades   | Long Trades   | Short Trades   |
|:---------------------------------------|:-------------|:--------------|:---------------|
| **Net Profit**                         | 29446200     | 21843600      | 7602600        |
| **Gross Profit**                           | 44856200     | 28031200      | 16825000       |
| **Gross Loss**                             | -15410000    | -6187600      | -9222400       |
| Net Profit (Adjusted)                  | 25419158.02  | 18912920.76   | 4886433.049    |
| Gross Profit (Adjusted)                | 42427100.58  | 26044120.92   | 15413077.36    |
| Gross Loss (Adjusted)                  | -17007942.56 | -7131200.154  | -10526644.32   |
| Specific Net Profit                    | 18565400     | 9806700       | 8758700        |
| Specific Gross Profit                  | 28166600     | 14718700      | 13447900       |
| Specific Gross Loss                    | -9601200     | -4912000      | -4689200       |
| Required Account Capital               | 989600       | 839800        | 2003700        |
| Account Return (%)                     | 2975.565885  | 2601.047869   | 379.4280581    |
| Return on Initial Capital (%)          | 294.462      | 218.436       | 76.026         |
---
### 📊 Return-to-Drawdown Ratios

| Ratio Description                                                 | Value         |
|-------------------------------------------------------------------|---------------|
| **Net Profit / Max Loss (%)**                                      | 3414.45       |
| **Net Profit / Max Trade Drawdown (%)**                            | 1001.09       |
| **Net Profit / Max Strategy Drawdown (%)**                         | 891.23        |
| **Specific Net Profit / Max Loss (%)**                             | 2152.76       |
| **Specific Net Profit / Max Trade Drawdown (%)**                   | 631.18        |
| **Specific Net Profit / Max Strategy Drawdown (%)**                | 561.91        |
| **Adjusted Net Profit / Max Loss (%)**                             | 2947.49       |
| **Adjusted Net Profit / Max Trade Drawdown (%)**                   | 864.19        |
| **Adjusted Net Profit / Max Strategy Drawdown (%)**                | 769.34        |
---
## 📈 NAV (Since June 2007)


![NAV_ Intermarket Trend Divergence Model](https://github.com/user-attachments/assets/ad7a1eff-8696-4089-a674-6605ca8098fa)
---
## 📈 Equity Curve (Since June 2007)


![EquityCurve_ Intermarket Trend Divergence Model](https://github.com/user-attachments/assets/97b6b009-a921-4d63-8bfc-f511c3a547c5)

## 📊 Recent 20 Trading Days (13:45 Snapshot)
Daily positions taken at 13:45 each day.

![Position Table](charts/position_table.png)
---

© Strategy logic remains proprietary.
