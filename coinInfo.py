# Jonathan Kizer
# 7/16/17

# requires coinmarketcap; install before running
# info here: https://pypi.python.org/pypi/coinmarketcap/


def main():
  from coinmarketcap import Market

  def coinInfo(coin):

    coinmarketcap = Market()

    coinLookup = coinmarketcap.ticker(str(coin))
  

    print("-------",str(coin),"-------")
    print(coinLookup)
    
  
  status = "Yes"
  print("To quit, type 'exit'; to find documentation, type 'info'.")
  while status == "Yes":
    coin = input("What coin would you like info for? ")
    if (coin == "Exit" or coin == "exit"):
      break
    if (coin == "Info" or coin == "info"):
      print("\nWritten by Jonathan Kizer, 7/16/17, utilizing the coinmarketcap Python package")
      print("Type the name of a coin to look up; to exit, type 'Exit'\n")
      print("+-----------------+")
      print("|jonathankizer.com|")
      print("+-----------------+\n\n")
      continue
    try:
      coinInfo(coin)
      print()
    except Exception:
      print("That doesn't appear to be a known currency; try again!\n")
  
  print("\nThanks for using this delightfully fun script!\n")
main()