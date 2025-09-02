import csv
# list some stock priceses using dicitinoary 
stock_prices={
    "APPLE":180,
    "TATA":250,
    "GOOGLE":135,
    "AMAZON":140,
    "TESLA":260,
    "MSSOFT":210,
    "MRF":1000,
}

def stock_portfolio_tracker():
    portfolio={}
    total_values=0
    print("Avaliable Stock and Prices: ")
    for stock,prices in stock_prices.items():
        print(f"{stock}: ${prices}")
    
    while True:
        stock=input("\nEnter stock symbol(or 'done' to finish): ").upper()
        if stock== "DONE":
            break
        if stock not in stock_prices:
            print("Stock not found! please choose from the available list.")
            continue
        try:
            quantity=int(input(f"Enter quantity for {stock}: "))
        except ValueError:
            print("please enter a valid number.")
            continue

        #Add the portfolio of stock
        portfolio[stock]=portfolio.get(stock,0)+quantity
        total_values=total_values+stock_prices[stock]*quantity

        #display the result 
    print("\n----Portfolio Summary----")
    for stock,qty in portfolio.items():
        value=stock_prices[stock]*qty
        print(f"{stock} -> quantity:{qty}, Value: ${value} ")
    print(f"\nTotal Investment Value: ${total_values}")

    #save to csv file 
    save=input("\nDo you want to save portfolio to CSV(y/n): ").lower()
    if save=="y":
        with open("portfolio.csv","w",newline="")as file:
            writer=csv.writer(file)
            writer.writerow(["Stock","Quantity","price","Value"])
            for stock,qty in portfolio.items():
                writer.writerow([stock,qty,stock_prices[stock],stock_prices[stock]*qty])
            writer.writerow(["Total","","",total_values])
            print("portfolio saved to portfolio.csv")

#run the program by calling the function 
stock_portfolio_tracker()
