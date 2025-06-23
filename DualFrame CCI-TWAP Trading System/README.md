# 📈 DualFrame CCI-TWAP Trading Strategy

## 📌 Strategy Rationale
The DualFrame CCI-TWAP System is designed to generate high-confidence directional signals through quantitative filtering of normalized price deviation metrics (CCI) across two temporal resolutions. A time-weighted average price (TWAP) component is used as a dynamic price anchor to regulate signal activation, enhancing noise suppression and trend alignment without reliance on conventional chart-based techniques.

A directional, quantitative-filtered momentum strategy that integrates multi-horizon signal alignment (via CCI) with time-weighted price anchoring (TWAP) for noise reduction and trend validation.

🌟 **Note:** 
**All results are based on real historical market data. Backtest coverage spans over 20 years, and the strategy has been live traded on TXF for more than one year. While different versions of the strategy have been deployed during live trading to meet institutional requirements, the core logic remains unchanged. The version presented here reflects a personally preferred configuration, selected for its clarity and transparency in performance representation.**

*This README was automatically generated as part of a real-time strategy monitoring and reporting system.*

## 📌 Strategy Attributes

- **Strategy Name : DualFrame CCI-TWAP System**  
- **Asset : Taiwan Index Futures (TXF)**    
- **Type : Momentum-Based Trend-Following**  
- **Data Frequency : 10-minute bars**  
- **Holding Duration : 1.5 to 3 days**
- **Max Contracts Held : 2 contracts** 
- **Backtested Period : From June 2017 to June 2025** *(In order to test if the strategy can survive under All-Weather conditions)*

⭐️ **Key Highlight:**
#### *Why Full-History Backtesting?*
#### (1) *The strategy is tested over the full historical dataset to capture a wide range of market regimes and ensure its resilience under different volatility, correlation, and macro cycles.*
#### (2) *The system incorporates a rolling logic core, allowing continuous internal adaptation without the need for manual parameter tuning—this reinforces the “all-weather” thesis.*

## 📌 Strategy Overview

This table provides a comprehensive summary of the trading strategy based on live and backtested data, covering both long and short trades.

Key performance metrics include :

🌟 **Important Note:** **Just wanna mentioned here, the numbers presented here desire to reflect the real and true performance without any manipulation.**
- **Sharpe Ratio : 1.64 (8 years backtested sharpe ratio)**
- **CAGR (Annualized Return) : 29.21%** 
- **Maximum Drawdown : -8.98%**
- **Profit Factor : 1.42**
- **Win Rate (%) : 44.82%**

## 📌 Strategy Performance Report **(Backtested Period : From June 2017 to June 2025)**

This repository summarizes the performance of a trading strategy applied to Taiwan Index Futures (TXF), highlighting core performance metrics, risk statistics, and trade breakdown.

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
| **Return After Max DD** | 8.10 |
| **Slippage Paid** | 1,935,500 |
| **Commission Paid** | 0 |

---
### 📊 Annual and Monthly Return Metrics

| Metric                             | Value        |
|-----------------------------------|--------------|
| **Annualized Return (%)**          | **29.21%** |
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

| Metric | All Trades | Long Trades | Short Trades |
|--------|------------|-------------|--------------|
| **Net Profit** | **4,675,700** | 2,530,600 | 2,145,100 |
| **Adjusted Net Profit** | 3,758,009 | 1,823,471 | 1,534,731 |
| **Gross Profit** | 15,804,600 | 10,152,200 | 5,652,400 |
| **Gross Loss** | -11,128,900 | -7,621,600 | -3,507,300 |

| **Max Contracts Held** | **2** | 2 | 2 |

---

### 📌 Return Statistics

| Metric | Value |
|--------|-------|
| **Required Capital** | 551,600 |
| **Account Return (%)** | 847.66% |
| **Return on Initial Capital (%)** | 233.79% |


---

## 🧮 Return-to-Drawdown Metrics


---
## Summary Statistics

| Metric | All Trades | Long Trades | Short Trades |
|--------|------------|-------------|--------------|
| **Total Trades** | **1776** | 1287 | 489 |
| **Win Rate (%)** | **44.82** | 46.78 | 39.67 |
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
