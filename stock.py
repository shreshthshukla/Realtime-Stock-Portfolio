import yfinance as yfin

#Creating portfolio dictionary
portfolio = {}

#Getting Current price from NSE
def get_price(symbol):
    try:
        ticker = yfin.Ticker(symbol + '.NS')
        return ticker.info['currentPrice']
    except:
        return 0  # 0 if error

#Fetching Current prices
def check_price(symbol):
    price = get_price(symbol)
    if price == 0:
        print("Price fetch error.")
    else:
        print("Current price of", symbol, ":", price)

#Buying a stock
def buy_stock(symbol, qty):
    price = get_price(symbol)
    if price == 0:
        print("Price fetch error.")
        return
    if symbol not in portfolio:
        portfolio[symbol] = {'qty': 0, 'buy_price': 0}
    total_cost = portfolio[symbol]['qty'] * portfolio[symbol]['buy_price'] + qty * price
    portfolio[symbol]['qty'] += qty
    portfolio[symbol]['buy_price'] = total_cost / portfolio[symbol]['qty']
    print(f"Bought {qty} {symbol} at {price:.2f}")

#Sell Stocks
def sell_stock(symbol, qty):
    if symbol not in portfolio or portfolio[symbol]['qty'] < qty:
        print("Not enough stock.")
        return
    price = get_price(symbol)
    if price == 0:
        print("Price fetch error.")
        return
    profit = qty * (price - portfolio[symbol]['buy_price'])
    portfolio[symbol]['qty'] -= qty
    print(f"Sold {qty} {symbol} at {price:.2f}, Profit: {profit:.2f}")

#show portfolio
def show_portfolio():
    total_value = 0
    total_invested = 0

    for stock, data in portfolio.items():
        current_price = get_price(stock)

        value = data['qty'] * current_price

        invested = data['qty'] * data['buy_price']

        total_value += value

        total_invested += invested

        print(stock, ": Qty", data['qty'], "Buy Avg", round(data['buy_price'], 2), "Current", round(current_price, 2), "Value", round(value, 2))

    total_profit = total_value - total_invested
    
    print("Total Value:", round(total_value, 2), "Total Profit:", round(total_profit, 2))

#Main Men
while True:
    print("1. Check Price Only")
    print("2. Buy Stock")
    print("3. Sell Stock")
    print("4. View Portfolio")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '2':
        symbol = input("Symbol (e.g., RELIANCE): ").upper()
        qty = int(input("Qty: "))
        buy_stock(symbol, qty)
    elif choice == '3':
        symbol = input("Symbol: ").upper()
        qty = int(input("Qty: "))
        sell_stock(symbol, qty)
    elif choice == '4':
        show_portfolio()
    elif choice == '1':
        symbol = input("Symbol: ").upper()
        check_price(symbol)
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid.")