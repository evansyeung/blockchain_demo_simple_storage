from brownie import SimpleStorage

def read_contract():
  # SimpleStorage acts like an array of (deployed) contracts. It reads from our deployment
  simple_storage = SimpleStorage[-1]
  # Brownie knows what the contract's ABI + Address because it saved the JSON after compilation
  print(simple_storage.retrieve())
  pass

def main():
  read_contract()
