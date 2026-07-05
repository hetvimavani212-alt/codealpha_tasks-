# 📈 Stock Portfolio Tracker

A simple Python-based **Stock Portfolio Tracker** that allows users to calculate the total value of their stock investments using predefined (hardcoded) stock prices. Users can add multiple stocks, view their portfolio summary, and save the investment details to a text file.

## 🚀 Features

- View available stock symbols and prices.
- Enter multiple stock purchases.
- Calculate investment for each stock.
- Calculate total portfolio investment.
- Validate stock names.
- Save portfolio details to a `portfolio.txt` file.
- Simple command-line interface.

## 🛠 Technologies Used

- Python 3
- Dictionary
- List
- Loops
- Conditional Statements
- File Handling

## 📂 Project Structure

```
Stock-Portfolio-Tracker/
│
├── stock_tracker.py      # Main Python program
├── portfolio.txt         # Generated portfolio summary
├── README.md             # Project documentation
```

## 📌 Hardcoded Stock Prices

| Stock | Price |
|--------|------:|
| AAPL | 150 |
| MSFT | 300 |
| TCS | 200 |
| TSLA | 700 |
| UBER | 450 |
| ADANI | 900 |

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/codealpha_tasks.git
```

2. Navigate to the project folder:

```bash
cd codealpha_tasks
```

3. Run the program:

```bash
python stock_tracker.py
```

## 💻 Sample Output

```
================================
 Welcome to Stock Tracker
================================

Available Stock List:

AAPL : 150
MSFT : 300
TCS  : 200
TSLA : 700
UBER : 450
ADANI: 900

Enter stock name: AAPL
Enter stock quantity: 5

Investment in AAPL: 750

Do you want to add another stock? yes

Enter stock name: MSFT
Enter stock quantity: 2

Investment in MSFT: 600

========== Portfolio Summary ==========
AAPL  Quantity: 5  Investment: 750
MSFT  Quantity: 2  Investment: 600

---------------------------------------
Total Investment = 1350

Portfolio saved to portfolio.txt
```

## 📄 Output File

The program generates a `portfolio.txt` file containing:

- Purchased stock names
- Quantity of each stock
- Investment value of each stock
- Total portfolio investment

## 📚 Concepts Used

- Python Dictionary
- Lists
- Loops (`while`, `for`)
- Conditional Statements (`if-else`)
- User Input
- Arithmetic Operations
- File Handling

## 🎯 Learning Outcome

This project demonstrates how Python can be used to build a basic stock portfolio tracker using fundamental programming concepts such as dictionaries, loops, user input, and file handling.



