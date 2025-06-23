# 📈 Intermarket Trend Divergence Trading Strategy

## 📌 Strategy Logic
The Beta Divergence Momentum (BDM) strategy is a directional trading model applied to Taiwan Index Futures (TXF), which exploits structural divergences between the Electronic Futures (TE) and Financial Futures (TF) sectors.

> 🎯 This combines **beta exposure (trend direction)** with **alpha generation (inter-sector relative value)** — resembling a breakout of a spread.

---

### 💼 Capital & Risk Management

- **Macro-Aware Position Sizing:**
  - **Reduce exposure during full-year earnings announcement months.**
  - **In other months**, use **ATR-based position sizing** for volatility adjustment.

Synthetic Asset Construction:
A synthetic ratio is created by dividing the price of Electronic Futures by Financial Futures (TE/TF), forming a relative strength index that reflects sector divergence.

This approach conceptually blends beta directionality (market trend exposure) with an alpha insight (relative value spread between sectors), creating a structural divergence-driven entry mechanism.

Risk & Capital Management:

During annual earnings announcement months, the position size is reduced to manage macro-event risk.

In other months, position sizing is dynamically adjusted using ATR for volatility-based exposure control.

🔹 Optional One-Liner Summary (for README or Pitch Deck):
Beta Divergence Momentum (BDM): A structural breakout strategy trading Taiwan Index Futures based on the sector-relative momentum between Electronics and Financials, filtered by DMI and adjusted by macro timing and volatility control.

**Beta Divergence Momentum (BDM)** is a directional trading strategy for Taiwan Index Futures (TXF) that detects structural divergence between the Electronics and Financial sectors.  
By analyzing the TE/TF ratio and applying DMI-based breakout detection, it captures market momentum aligned with sector outperformance.  
The strategy blends beta exposure with alpha insights and adjusts risk dynamically using ATR and macro event timing.  
Exits are triggered by monthly events, volatility thresholds, and profit/loss limits to ensure controlled execution.

**Beta Divergence Momentum (BDM)** is a directional trading strategy for Taiwan Index Futures (TXF) that capitalizes on structural divergence between the Electronics Futures (TE) and Financial Futures (TF) sectors.

---


### 🧭 Strategy Type

- 🟢 **Directional Spread-Based Strategy**
- 🔁 **Beta + Alpha Hybrid Model**
- 🧠 **Sector Divergence Quant Strategy**
- 📉 **Volatility-Aware Execution Logic**

---

### ✨ Summary

> **BDM** captures structural breakout opportunities in Taiwan's equity index by monitoring the relative momentum between Electronics and Financials, integrating trend filters and volatility-aware execution to improve robustness and adaptability.

🧭 Strategy Type Classification:
Directional Spread-Based Strategy

Relative Strength + Breakout Momentum

Sector Divergence Quant Strategy

Volatility-Adjusted, Event-Aware Execution

*This README was automatically generated as part of a real-time strategy monitoring and reporting system.*

## 📌 Strategy Attributes

- **Strategy Name : Intermarket Trend Divergence Model**  
- **Asset : Taiwan Index Futures (TXF)**    
- **Type : Directional Alpha Model**  
- **Data Frequency : 30-minute bars**  
- **Holding Duration : 3 to 6 days**
- **Market Time :**
- **Backtested Period : From April 2007 to June 2025** *(In order to test if the strategy can survive under All-Weather conditions)*

⭐️ **Key Highlight:**
**The reason why I didn't consider In sample/Out Sample type of test is to prove that the strategy is itself enough robust without changing any parameters throughout the whole dataset.**

## 📌 Strategy Overview

This table provides a comprehensive summary of the trading strategy performance based on real data, covering both long and short trades.

Key performance metrics include :

🌟 **Important Note:** **Just wanna mentioned here, the numbers presented here desire to reflect the real and true performance without any manipulation.**
- **Sharpe Ratio** : **1.4671**
- **CAGR (Annualized Return)** : **16.16%**
- **Maximum Drawdown** : -13.39%
- **Profit Factor** : ***2.91***
- **Win Rate (%)**: ***78.57%***


## 📌 Strategy Performance Report (Backtested Period : From April 2007 to June 2025)

This repository summarizes the performance of a trading strategy applied to Taiwan Index Futures (TXF), highlighting core performance metrics, risk statistics, and trade breakdown.

### 📊 Performance Ratios

| Metric Description                                                  | Value         |
|--------------------------------------------------------------------|---------------|
| **Upside Potential Ratio**                                         | 143.72        |
| **Sharpe Ratio**                                                   | 0.4235        |
| **Annualized Sharpe Ratio**                                        | 1.4671        |
| **Sortino Ratio**                                                  | 0.5451        |
| **Fouse Ratio**                                                    | 0.0062        |
| **Calmar Ratio**                                                   | 0.0593        |
| **Sterling Ratio**                                                 | 0.0020        |
---
### 📊  Profitability Ratios

| Metric                                  | All Trades   | Long Trades   | Short Trades   |
|----------------------------------------|--------------|---------------|----------------|
| **Profit Factor**                          | 2.910850097  | 4.530221734   | 1.824362422    |
| Adjusted Profit Factor                 | 2.494546323  | 3.652137138   | 1.464196652    |
| Specific Profit Factor                 | 2.933654127  | 2.996478013   | 2.867845261    |
| Max Contracts Held Concurrently        | 19           | 18            | 19             |
| Slippage Paid                          | 1469000      | 774000        | 695000         |
| Commission Paid                        | 0            | 0             | 0              |
| Unrealized P&L                         | n/a          | n/a           | n/a            |

### 📊 Annual and Monthly Return Metrics

| Metric                                  | Value        |
|----------------------------------------|--------------|
| **Annualized Return (%)**                  | 16.15580837  | 
| Monthly Return (%)                         | 1.346317364  | 
| Buy-and-Hold Return ($)                    | 17440121.66  | 
| Average Monthly Return ($)                 | 135074.3119  |     
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
  - **All**: 78.57%  
  - Long: 82.23%  
  - Short: 73.96%
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

## ⚙️ Automation
This repository includes:
- Python script to parse position CSV and auto-generate visuals
- GitHub Actions workflow to update chart + table daily

---

© Strategy logic remains proprietary. This repository only presents portfolio-level analytics and is safe to be shared publicly.
