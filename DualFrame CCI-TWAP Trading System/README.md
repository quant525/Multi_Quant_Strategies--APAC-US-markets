## 📈 DualFrame CCI-TWAP Trading System

### 📌 Strategy Rationale
**The DualFrame CCI-TWAP System is designed to generate high-confidence directional signals through quantitative filtering of normalized price deviation metrics (CCI) across two temporal resolutions. A time-weighted average price (TWAP) component is used as a dynamic price anchor to regulate signal activation, enhancing noise suppression and trend alignment without reliance on conventional chart-based techniques.**

A directional, quantitative-filtered momentum strategy that integrates multi-horizon signal alignment (via CCI) with time-weighted price anchoring (TWAP) for noise reduction and trend validation.

🌟 **Note:** 
*All results are based on real historical market data. Backtest coverage spans over 20 years, and the strategy has been live traded on TXF for more than one year. While different versions of the strategy have been deployed during live trading to meet institutional requirements, the core logic remains unchanged. The version presented here reflects a personally preferred configuration, selected for its clarity and transparency in performance representation.*

*This README was automatically generated as part of a real-time strategy monitoring and reporting system.*

### 📌 Strategy Attributes

- **Strategy Name : DualFrame CCI-TWAP System**  
- **Asset : Taiwan Index Futures (TXF)**    
- **Type : Momentum-Based Trend-Following**  
- **Data Frequency : 10-minute bars**  
- **Holding Duration : 1.5 to 3 days**
- **% Time in Market : 24.02%**   
- **Max Contracts Size : 2 contracts** 
- **Backtested Period : From June 2017 to June 2025 (8 Yrs, 9 Dys, 5 Hrs, 10 Mins)** *(In order to test if the strategy can survive under All-Weather conditions)*

⭐️ **Key Highlight:**
#### *Why Full-History Backtesting?*
#### (1) *The strategy is tested over the full historical dataset to capture a wide range of market regimes and ensure its resilience under different volatility, correlation, and macro cycles.*
#### (2) *The system incorporates a rolling logic core, allowing continuous internal adaptation without the need for manual parameter tuning—this reinforces the “all-weather” thesis.*

### 📌 Strategy Overview

This table provides a comprehensive summary of the trading strategy based on live and backtested data, covering both long and short trades.

Key performance metrics include :

🌟 **Important Note:** **Just wanna mentioned here, the numbers presented here desire to reflect the real and true performance without any manipulation.**
- **Sharpe Ratio : 1.64 (8 years backtested sharpe ratio)**
- **Annual Return : 29.21%** 
- **Maximum Drawdown : -8.98%**
- **Profit Factor : 1.42**
- **Win Rate (%) : 44.82%**

### 📌 Strategy Performance Report **(Backtested Period : From June 2017 to June 2025)**

This repository summarizes the performance of a trading strategy applied to Taiwan Index Futures (TXF), highlighting core performance metrics, risk statistics, and trade breakdown.

### 📈 Strategy Performance by Year

| Year | Profit (¤) | Return (%)   | Gross Profit | Gross Loss | Trade Count | Win Rate (%)   |
|------|------------|--------------|---------------|-------------|--------------|----------------|
| 2025 | 769,300    | 13.0248544   | 1,763,000     | -993,700     | 107          | 46.72897196    |
| 2024 | 753,400    | 14.62060935  | 3,340,200     | -2,586,800   | 211          | 45.49763033    |
| 2023 | 347,000    | 7.22014149   | 1,421,600     | -1,074,600   | 215          | 43.72093023    |
| 2022 | 575,800    | 13.61164957  | 2,300,000     | -1,724,200   | 234          | 38.03418803    |
| 2021 | 860,000    | 25.51777343  | 2,590,400     | -1,730,400   | 222          | 50.00000000    |
| 2020 | 556,300    | 19.76971463  | 1,815,900     | -1,259,600   | 227          | 45.37444934    |
| 2019 | 500,800    | 21.65059876  | 986,200       | -485,400     | 206          | 47.08737864    |
| 2018 | 260,700    | 12.7022023   | 1,210,100     | -949,400     | 228          | 45.17543860    |
| 2017 | 52,400     | 2.62         | 377,200       | -324,800     | 126          | 42.06349206    |
---

### 📊 Performance Ratios

| Metric | Value |
|--------|-------|
| **Upside Potential Ratio** | 172.58 |
| **Sharpe Ratio** | 0.47 |
| **Annual Sharpe Ratio** | **1.64** |
| **Sortino Ratio** | 1.29 |
| **Fouse Ratio** | 0.0126 |
| **Calmar Ratio** | 0.0194 |
| **Sterling Ratio** | 0.0020 |

---

### 📊 Profitability Ratios

| Ratio | Value |
|-------|-------|
| **Profit Factor** | **1.42** |
| **Adjusted Profit Factor** | 1.33 |
| **Specific Profit Factor** | 1.38 |
| **Slippage Paid** | 1,935,500 |
| **Commission Paid** | 0 |

---
### 📊 Annual and Monthly Return Metrics

| Metric                             | Value        |
|-----------------------------------|--------------|
| **Annual Return (%)**          | **29.21%** |
| **Monthly Return (%)**             | 2.43% |
| **Buy-and-Hold Return**            | 2,177,535 |
| **Average Monthly Return**         | 48,203 |
| **Monthly Return StdDev**          | 112,044 |

---
### 📊 Risk Metrics

| Metric      | All Trades   | Long Trades  | Short Trades  |
|-----------|--------------|--------------|---------------|
| **Max Drawdown** | -577,400 | -447,500 | -293,000 |
| **Max Drawdown (%)** | **-8.98%** | -10.29% | -8.04% |
| **Max Trade Loss** | -551,600 | -390,400 | -234,600 |
| **Max Trade Loss (%)** | -8.59% | -9.06% | -6.46% |

---
### 📊 Trade Summary

- **Total Number of Trades:** 1,776 
  - Long: 1,287 
  - Short: 489 
- **Win Rate:**  
  - All: 44.82%  
  - Long: 46.78%  
  - Short: 39.67%
---
### 📊 Return-to-Drawdown Ratios

| Ratio Description  | Value |
|--------|-------|
| Net Profit / Max Loss (%) | 4,620.26% |
| Net Profit / Max Trade DD (%) | 4,369.81% |
| Net Profit / Max Strategy DD (%) | 809.79% |
| Specific Net / Max Loss (%) | 2,483.89% |
| Specific Net / Max Trade DD (%) | 2,349.25% |
| Specific Net / Max Strategy DD (%) | 435.35% |
| Adjusted Net / Max Loss (%) | 3,713.45% |
| Adjusted Net / Max Trade DD (%) | 3,512.16% |
| Adjusted Net / Max Strategy DD (%) | 650.85% |
---

### 📊 General Performance Metrics

| Metric                             | All Trades    | Long Trades    | Short Trades   |
|-----------------------------------|---------------|----------------|----------------|
| Net Profit                         | 4,675,700     | 2,530,600      | 2,145,100      |
| Gross Profit                       | 15,804,600    | 10,152,200     | 5,652,400      |
| Gross Loss                         | -11,128,900   | -7,621,600     | -3,507,300     |
| Adjusted Net Profit                | 3,758,009.03  | 1,823,471.70   | 1,534,731.44   |
| Adjusted Gross Profit              | 15,244,420.81 | 9,738,427.22   | 5,246,581.33   |
| Adjusted Gross Loss                | -11,486,411.78| -7,914,955.52  | -3,711,849.89  |
| Specific Net Profit                | 2,513,700     | 2,597,200      | -83,500        |
| Specific Gross Profit              | 9,205,200     | 7,026,000      | 2,179,200      |
| Specific Gross Loss                | -6,691,500    | -4,428,800     | -2,262,700     |
| Required Account Capital (Max)     | 551,600       | 390,400        | 234,600        |
| Account Return (Multiple)          | 847.66x       | 648.21x        | 914.36x        |
| Initial Capital Return (Multiple)  | 233.785x      | 126.53x        | 107.255x       |
---
## ⏱ Time Analysis

| Metric                             | Value                          |
|------------------------------------|--------------------------------|
| Total Backtest Period              | 8 Yrs, 9 Dys, 5 Hrs, 10 Mins   |
| Time Strategy Was in Market        | 1 Yr, 11 Mths, 8 Dys, 55 Mins  |
| % Time in Market                   | 24.01595941 %                  |
| Longest Flat (No Position) Period  | 12 Dys, 19 Hrs, 50 Mins        |
| Maximum Profit Date                | 2025/4/10                      |
| Maximum Loss Date                  | 2024/8/5                       |
| Max Strategy Drawdown Timestamp    | 2024/11/26 10:25               |
| Max Trade Drawdown Timestamp       | 2024/11/26 13:35               |
---
## Summary Statistics

| Metric | All Trades | Long Trades | Short Trades |
|--------|------------|-------------|--------------|
| Avg Trade P&L | 2632.71 | 1966.28 | 4386.71 |
| Avg Win | 19855.03 | 16864.12 | 29136.08 |
| Avg Loss | -11484.93 | -11291.26 | -11929.59 |
| Win/Loss Ratio | 1.73 | 1.49 | 2.44 |
| Max Win | 167400 | 144400 | 167400 |
| Max Loss | -101200 | -101200 | -77200 |
| Avg Bars Held | 53.3 | 57.9 | 41.3 |
| Avg Bars (Win Trades) | 73.3 | 77.6 | 60 |
| Avg Bars (Loss Trades) | 37 | 40.4 | 29 |
| Avg Bars Between Trades | 50.5 | 53 | 25 |
| Avg Bars Between Wins | 228.3 | 321.2 | 1177.5 |
| Avg Bars Between Losses | 210.8 | 315.2 | 787.6 |

---

## 📈 NAV (Since June 2017)

![NAV_DualFrame CCI-TWAP System](https://github.com/user-attachments/assets/be667483-9072-4df6-9304-5d90fbfba249)

---
## 📈 Equity Curve (Since June 2017)

![EquityCurve_DualFrame CCI-TWAP System](https://github.com/user-attachments/assets/1051c406-6c75-487e-bf5f-6ce09dfe1760)


## Position Chart (Last 20 Days @13:45)

![Position Chart](charts/last20days_chart.png)

## Position Table (Last 20 Days)

File: `data/last20days_table.csv`

## Files Included

- `data/pos_TXFstrategyC.csv`: Raw position data
- `charts/last20days_chart.png`: Recent position chart
- `data/last20days_table.csv`: Filtered table at 13:45
- `.github/workflows/update_positions.yml`: GitHub Action for daily updates
- `scripts/update_and_plot.py`: Python script for processing and chart generation

---

_Last Updated: 2025-06-22_
