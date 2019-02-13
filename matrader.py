import datetime 
import sys
import getopt
import time
from poloniex import poloniex

version_number = " ALPHA 0.1.3"

def main(argv):
	period = 10 
	currentMA = 0;
	lengthOfMA = 0
	pair = "BTC_XMR"
	prices = []
	
#API Usher

	print("POLONIEX MA Trader." + version_number +  "\n ")

	try:
		opts, args = getopt.getopt(argv, "hp",["period=",])
	except getopt.GetoptError:
		print('njord.py -p <period>')
		sys.exit(2)

	for opt, arg in opts:
		if opt == '-h':
			print('matrader.py -p <period>')
			sys.exit()

		elif opt in ("-p", "--period"):
			if (int(arg) in [300,900,1800,7200,14400,86400]):
				period = arg
			else:
				print('Clock Error. Exchange requires periods in 300,900,1800,7200,14400,86400 seconds.')
				sys.exit(2)
 	#insert public & private key here
	conn = poloniex("","")
				
	
	while True:	
		currentValues = conn.api_query("returnTicker")

		lastPairPrice = currentValues[pair]["last"]

		if (len(prices) > 0):
			currentMA = sum(prices) / float(len(prices))

		print(" TIME: " + "{:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now()) + " PERIOD: %ss. \n Pair: %s %s  \n Current MA: %s." % (period, pair, lastPairPrice, currentMA) )
		prices.append(float(lastPairPrice))
		#prices = prices[-lengthOfMA:]	
		time.sleep(int(period))

		#Highest/Lowest prices

		def highest_price(prices):
			highest = prices[0] 
			for high in prices:
				if high > highest:
					highest = high
			return highest 	

		highpoint = highest_price(prices)

		print( " High: " + str(highpoint))


		def lowest_price(prices):
			lowest = prices[0] 
			for low in prices:
				if low < lowest:
					lowest = low
			return lowest

		lowpoint = lowest_price(prices)

		print( " Low: " + str(lowpoint) +"\n ")

if __name__ == "__main__":
		main(sys.argv[1:])

#Add Trading Parameters here
 
		


	
