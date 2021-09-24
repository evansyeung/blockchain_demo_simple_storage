from brownie import accounts, config, network, SimpleStorage

def deploy_simple_storage():
  # Brownie defaults to using ganache-cli with 10 accounts
  account = get_account()

  # Manually add e.g. MetaMask account to Brownie
  # account = accounts.load("metamask-account")

  # Environment Variable
  # account = accounts.add(config["wallets"]["from_key"])
  # print(account)

  simple_storage = SimpleStorage.deploy({"from": account})
  # print(simple_storage)

  stored_value = simple_storage.retrieve()
  print("favoriteName: {}".format(stored_value))

  transaction = simple_storage.store(15, {"from": account})
  transaction.wait(1)

  updated_stored_value = simple_storage.retrieve()
  print("favoriteName: {}".format(updated_stored_value))
  pass

# Check if we're using a development network or a testnet
def get_account():
  # network is another Brownie keyword
  if network.show_active() == "development":
    return accounts[0]
  else:
    return accounts.add(config["wallets"]["from_key"])

def main():
  deploy_simple_storage()
