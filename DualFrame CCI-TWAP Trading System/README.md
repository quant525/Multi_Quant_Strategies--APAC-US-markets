# TXFstrategyC - DualFrame CCI-TWAP System

## Strategy Overview

- **Strategy Name**: DualFrame CCI-TWAP System  
- **Asset**: TAIEX Futures  
- **Type**: Momentum-Based Trend-Following  
- **Data Frequency**: 10-minute K-bars  
- **Holding Duration**: 1.5 to 3 days  

## Position Chart (Last 20 Days @13:45)

![Position Chart](charts/last20days_chart.png)

## Sample Position Table (Last 20 Days)

File: `data/last20days_table.csv`

## Files Included

- `data/pos_TXFstrategyC.csv`: Raw position data
- `charts/last20days_chart.png`: Recent position chart
- `data/last20days_table.csv`: Filtered table at 13:45
- `.github/workflows/update_positions.yml`: GitHub Action for daily updates
- `scripts/update_and_plot.py`: Python script for processing and chart generation

---

_Last Updated: 2025-06-22_
