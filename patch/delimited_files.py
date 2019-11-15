import csv
''' For technical reasons that you should feel free to blame on Microsoft, you should always
work with csv files in binary mode by including a b after the r or w '''

if __name__ == "__main__":
	def process(*args):
	        print(*args)

	

	with open('tab_delimited_stock_prices.txt', 'r', encoding='utf8') as f:
		reader = csv.reader(f, delimiter='\t')
		print("tab delimited stock prices:")
		for row in reader:
			date = row[0]
			symbol = row[1]
			closing_price = float(row[2])
			#print(row["date"])
			process(date, symbol, closing_price)

	print()

	with open('colon_delimited_stock_prices.txt', 'r', encoding='utf8',newline='') as f:
		reader = csv.DictReader(f, delimiter = ':')
		print("writing out comma_delimited_stock_prices.txt")
		for row in reader:
			date = row["date"]
			symbol = row["symbol"]
			closing_price = float(row["closing_price"])
			process(date, symbol, closing_price)

	print()

	# Write out delimited data using csv.writer
	today_prices = { 'AAPL': 90.91, 'MSFT' : 41.68, 'FB' : 64.5 }
	print("writing out comma_delimited_stock_prices2.txt")
	with open('comma_delimited_stock_prices2.txt', 'w', encoding='utf8', newline='') as f:
		writer = csv.writer(f, delimiter=',')
		for stock, price in today_prices.items():
			writer.writerow([stock, price])
