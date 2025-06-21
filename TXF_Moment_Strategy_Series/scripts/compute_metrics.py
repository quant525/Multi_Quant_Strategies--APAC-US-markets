import pandas as pd
import numpy as np

# Load equity curve
df = pd.read_csv('../data/equity_curve.csv', parse_dates=['Date'])
df['Returns'] = df['Equity'].pct_change()

# Calculate Sharpe
sharpe_ratio = df['Returns'].mean() / df['Returns'].std() * np.sqrt(252)

# Calculate CAGR
years = (df['Date'].iloc[-1] - df['Date'].iloc[0]).days / 365
cagr = (df['Equity'].iloc[-1] / df['Equity'].iloc[0]) ** (1/years) - 1

# Max Drawdown
cum_max = df['Equity'].cummax()
drawdown = df['Equity'] / cum_max - 1
max_dd = drawdown.min()

print(f'Sharpe Ratio: {sharpe_ratio:.2f}')
print(f'CAGR: {cagr:.2%}')
print(f'Max Drawdown: {max_dd:.2%}')
