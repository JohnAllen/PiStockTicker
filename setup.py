from distutils.core import setup

setup(
  name = 'PiStockTicker',
  packages = ['PiStockTicker'],
  version = '0.1',
  description = "Print a stock\'s price volume and percentage every five seconds using a Raspberry Pi",
  author = 'JohnAllen',
  author_email = 'johnjalleniii@gmail.com',
  url = 'https://github.com/JohnAllen/PiStockTicker',
  download_url = 'https://github.com/JohnAllen/PiStockTicker/tarball/0.1',
  dependency_links=['https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code/tree/master/Adafruit_CharLCD'],
  keywords = ['stocks', 'raspberry pi'],
)
