# Import the Web3 library
 

  
from web3 import Web3

# Create an instance of Web3
w3 = Web3()

# Create an instance of the EthereumTesterProvider
provider = EthereumTesterProvider()

# Update the Web3 instance to include the provider
w3 = Web3(provider)

# Access information for the most recent block
print(w3.eth.get_block("latest"))


