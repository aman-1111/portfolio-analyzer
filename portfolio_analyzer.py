import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# --- Step 1: Define Your Portfolio ---
portfolio = {
    'AAPL': 10,   # Apple
    'MSFT': 5,    # Microsoft
    'GOOGL': 2    # Alphabet (Google)
}

start_date = "2023-01-01"
end_date = "2024-01-01"

# --- Step 2: Fetch Stock Data ---
def fetch_data(tickers, start, end):
    data = yf.download(tickers, start=start, end=end , auto_adjust=False)["Adj Close"]
    return data

tickers = list(portfolio.keys())
prices = fetch_data(tickers, start_date, end_date)

# --- Step 3: Calculate Daily Portfolio Value ---
portfolio_df = prices.copy()
for stock in portfolio:
    portfolio_df[stock] = portfolio_df[stock] * portfolio[stock]

portfolio_df["Total"] = portfolio_df.sum(axis=1)

# --- Step 4: Plot Portfolio Value ---
plt.figure(figsize=(12, 6))
plt.plot(portfolio_df["Total"], label="Portfolio Value", color="green")
plt.title("📈 Portfolio Value Over Time")
plt.xlabel("Date")
plt.ylabel("Total Value ($)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# --- Step 5: Return & Volatility ---
daily_returns = portfolio_df["Total"].pct_change().dropna()
total_return = (portfolio_df["Total"][-1] / portfolio_df["Total"][0]) - 1
volatility = daily_returns.std()

print(f"Total Return: {total_return:.2%}")
print(f"Volatility (Std Dev): {volatility:.2%}")
