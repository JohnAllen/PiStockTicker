import sys

from yahoo_finance import Share
from time import sleep
from lcd_module import Adafruit_CharLCD

def getStockSymbols():
      if len(sys.argv) > 1:
        print "True"      


def displayStockQuotes(symbols, seconds):
    """
    Display each symbol's price, volume and percent change for seconds

    :param: symbols: List of stock symbols in Yahoo format.  E.g. 'AMZN' or 'BRK-B' (NOTE: not 'BRK.B').
    :param: seconds: Number of seconds to display each stock.
    
    # The following Adafruit_CharLCD library is found here: 
    # https://github.com/adafruit/Adafruit_Python_CharLCD 
    # See this tutorial for a hello world Python/Raspberry Pi/LCD tutorial:
    # https://learn.adafruit.com/drive-a-16x2-lcd-directly-with-a-raspberry-pi/python-code
    """
 
    lcd = Adafruit_CharLCD()
    while True:
      for symbol in symbols:
        stock = Share(symbol)
        lcd.clear()
        lcd.message(symbol + ":  $")	
        lcd.message(stock.get_price() + "\n")
        volume = stock.get_volume()
        change = stock.get_change()
        lcd.message(change + "|")
      
        open = stock.get_open()
      
      if type(open) is str and type(change) is str:
        percentChange = float(change) / float(open)
        # format percent change in human-readable format: "1%" instead of ".01"
	lcd.message("{0:.00%}".format(percentChange))
      else:
        lcd.message("?")

      if volume:
        lcd.message("|" + volume)
      else:
        lcd.message("|?")

      sleep(seconds) # Delay between each stock/symbol			


if __name__ == '__main__':
  getStockSymbols()
#  displayStockQuotes()
