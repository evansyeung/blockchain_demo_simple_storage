from brownie import SimpleStorage, accounts

def test_deploy():
  # Arrange (setup)
  account = accounts[0]
  simple_storage = SimpleStorage.deploy({"from": account})
  expected = 0

  # Act
  starting_value = simple_storage.retrieve()

  # Assert
  assert starting_value == expected

def test_update_storage():
  # Arrange (setup)
  account = accounts[0]
  simple_storage = SimpleStorage.deploy({"from": account})
  expected = 15

  # Act
  simple_storage.store(15)
  updated_value = simple_storage.retrieve()

  # Assert
  assert updated_value == expected
