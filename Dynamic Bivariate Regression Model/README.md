## Dynamic Bivariate Regression Model – Position Tracker
 
This strategy is based on a Dynamic Bivariate Regression Model that captures evolving relationships between two market variables, using rolling 30-minute intervals to forecast short-term directional movement on the Taiwan Index Futures.
This repository tracks the position changes of the TXF Dynamic Bivariate Regression Model Strategy.

## 📌 Strategy Attributes

- **Strategy Name:** Dynamic Bivariate Regression Model  
- **Asset:** Taiwan Index Futures (TXF)  
- **Type:** Statistical Forecasting Model  
- **Rolling Frequency:** 30-minute bars  
- **Typical Holding Time:** 2 to 3 days

## 📈 Equity Curve (Since June 2001)

![EquityCurve_Dynamic Bivariate Regression Model](https://github.com/user-attachments/assets/20feb853-ac5f-4681-8eef-bd6b5db079e2)

## 📈 Position (Since March 2024)

![Position Chart](images/position_plot_english_fixed.png)

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
