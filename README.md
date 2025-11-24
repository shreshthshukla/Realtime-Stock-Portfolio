## 📈 NSE Stock Portfolio CLI Tracker

This is a **simple command-line interface (CLI) application** written in Python for simulating and tracking a stock portfolio, specifically focused on **Indian stocks listed on the NSE (National Stock Exchange)**. It uses the `yfinance` library to fetch real-time market data.

-----

## ✨ Features

  * **Real-time Market Data:** Fetches the live current price for any valid NSE ticker using `yfinance` and the `.NS` suffix.
  * **Portfolio Management:** Allows users to simulate **buying** and **selling** stocks.
  * **Weighted Average Cost Basis:** Automatically calculates the **weighted average buy price** (cost basis) upon every purchase to accurately track investment performance.
  * **Profit/Loss Calculation:** Calculates the realized **profit or loss** when a stock is sold.
  * **Portfolio Summary:** Displays current holdings, total investment, current market value, and overall unrealized profit/loss.

-----

## 🛠️ Installation and Setup

### Prerequisites

You need **Python 3** installed on your system.

### Dependencies

This script requires the `yfinance` library:

1.  **Clone the repository** (or save the code as `stock_tracker.py`).
2.  **Install the dependency** using pip:
    ```bash
    pip install yfinance
    ```

### Running the Application

Execute the script from your terminal:

```bash
python stock_tracker.py
```

-----

## 🚀 How to Use

The application runs in a loop, presenting the main menu:

```
1. Check Price Only
2. Buy Stock
3. Sell Stock
4. View Portfolio
5. Exit
Enter your choice: 
```

### 1\. Check Price Only (Option 1)

Enter the **NSE Ticker** (e.g., `RELIANCE`, `TCS`). This provides the current price without affecting your portfolio.

### 2\. Buy Stock (Option 2)

Adds a stock to your portfolio.

  * If the stock is new, the average buy price is set to the current market price.
  * If the stock is already held, the new purchase price is averaged with the existing cost basis using the **weighted average formula**:
    $$\text{New Buy Avg} = \frac{(\text{Existing Qty} \times \text{Existing Buy Avg}) + (\text{New Qty} \times \text{Current Price})}{\text{Existing Qty} + \text{New Qty}}$$

### 3\. Sell Stock (Option 3)

Reduces the quantity of a stock.

  * Calculates the **realized profit/loss** based on the difference between the current selling price and the stock's recorded average buy price.
  * If you attempt to sell more shares than you hold, the transaction will be rejected.

### 4\. View Portfolio (Option 4)

Displays a summary table of your current holdings, fetching the live prices to calculate:

  * Quantity held
  * Average Buy Price
  * Current Market Price
  * Current Total Value
  * Overall Unrealized Profit/Loss (Total Value - Total Invested)

-----

## ⚠️ Important Limitation

### Data Persistence

The current implementation uses a simple Python dictionary (`portfolio = {}`) for storing all investment data. This means the portfolio is only stored in **memory** and is **lost** every time the script is closed or terminated (Option 5: Exit).

For a real-world application, you would need to implement data persistence using:

  * **JSON/CSV files:** To save the dictionary data to a local file before exiting and loading it upon startup.
  * **SQLite Database:** For a more robust, structured, and scalable solution.

-----

## 💡 Code Structure

The code is organized into clear functions for easy maintenance:

| Function | Purpose |
| :--- | :--- |
| `get_price(symbol)` | Fetches the current price from `yfinance` for the symbol + `.NS`. |
| `check_price(symbol)` | Calls `get_price` and prints the result to the console. |
| `buy_stock(symbol, qty)` | Handles stock purchase and updates the weighted average buy price. |
| `sell_stock(symbol, qty)` | Handles stock sale, updates quantity, and calculates realized profit/loss. |
| `show_portfolio()` | Iterates through holdings, calculates live value, and displays the summary. |
