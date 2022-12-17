table_data = [
    ["Ticker", "Open", "Close"],
    ["AAPL", 363.25, 363.4],
    ["AMZN", 2756.0, 2757.99],
    ["GOOG", 1409.1, 1408.2]
]


#amazon_data = table_data[2]
#print(amazon_data)

#amazon_data = table_data[2]
#amazon_opening_price = amazon_data[1]
#print(amazon_opening_price)

#amazon_opening_price = table_data[2][1]
#print(amazon_opening_price)

for row in table_data:
    ticker = row[0]
    print(ticker)


table_data = [
    {
        "Ticker": "AAPL",
        "Open": 363.25,
        "Close": 363.4
    },
    {
        "Ticker": "AMZN",
        "Open": 2756.0,
        "Close": 2757.99
    },
    {
        "Ticker": "GOOG",
        "Open": 1409.1,
        "Close": 1408.2
    }
]

#for item in table_data:
#    print(item)

for item in table_data:
    ticker = item["Ticker"]
    print(ticker)

# can use get(), works like key syntax but can return a default value if the key does not exist 

ticker = item.get("Ticker")


