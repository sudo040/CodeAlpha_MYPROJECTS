# Stock Portfolio Tracker

A simple Python command-line application that calculates the total value of a stock portfolio using manually defined stock prices. You enter stock symbols and the number of shares you own, and the program calculates each holding's value and the portfolio total.

> **Note:** The stock prices in this project are examples hardcoded in the program. They are not live market prices and should not be used for financial decisions.

## Features

- Stores example stock prices in a Python dictionary.
- Accepts stock symbols and share quantities from the user.
- Checks stock symbols against the available list.
- Validates quantity input and rejects non-positive quantities.
- Combines quantities when the same stock is entered more than once.
- Displays each holding's value and the total portfolio value.
- Optionally saves the summary to `stock_portfolio.txt`.

## Requirements

- Python 3
- A terminal or command-line interface

No third-party Python packages are required.

## Getting Started

### 1. Save the program

Save the Python code in a file named `stock_tracker.py`.

### 2. Run the program

From the directory containing the file, run:

```bash
python3 stock_tracker.py
```

## How to Use

1. Start the program.
2. Choose a stock symbol from the list displayed by the program.
3. Enter the quantity of shares you own.
4. Repeat for any additional stocks.
5. Type `done` when you have finished entering stocks.
6. Review the portfolio summary and total investment value.
7. Enter `yes` when asked whether you want to save the results, or `no` to skip saving.

### Example

Using the example prices in the code, entering 5 shares of `AAPL` and 2 shares of `TSLA` produces a result similar to:

```text
===== PORTFOLIO SUMMARY =====
AAPL: 5 shares x $180 = $900.00
TSLA: 2 shares x $250 = $500.00
------------------------------
Total Investment: $1,400.00
```

The total is calculated as:

```text
(5 * 180) + (2 * 250) = 1400
```

## Example Stock Prices

The program includes these hardcoded sample prices:

| Stock symbol | Example price per share |
|---|---:|
| AAPL | $180 |
| TSLA | $250 |
| MSFT | $420 |
| GOOGL | $165 |
| AMZN | $190 |

To change these values or add more stocks, edit the `stock_prices` dictionary in `stock_tracker.py`.

## Output File

If you choose to save the result, the program creates `stock_portfolio.txt` in the directory from which you run it. The file contains each entered stock, its quantity, its calculated value, and the total portfolio value. Running the program again with the same output filename will overwrite the previous summary.

## Concepts Practiced

- Dictionaries
- User input and printed output
- `while` loops and `for` loops
- Conditional statements
- Basic multiplication and addition
- Input validation with `try` / `except`
- File handling with `open()` and the `with` statement

## Limitations

- Stock prices are entered in the source code and do not update automatically.
- The program calculates the value of the shares entered; it does not track purchase history, profit/loss, fees, dividends, or live market prices.
- The example uses US dollars (`$`) for display.

## Possible Improvements

- Export portfolio summaries to CSV.
- Allow users to update stock prices while the program is running.
- Track purchase price and calculate profit or loss.
- Save and reload portfolio quantities between sessions.
- Integrate a reliable market-data API for current prices.

## License

This project is provided for learning and personal practice. Add a license file if you plan to distribute it publicly.
