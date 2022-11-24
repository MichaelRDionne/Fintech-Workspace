# Ethereum Account Functions

################################################################################

# Imports
import os
import requests
from dotenv import load_dotenv
load_dotenv('.env')
from bip44 import Wallet
from web3 import Account
from web3 import middleware
from web3.gas_strategies.time_based import medium_gas_price_strategy
from web3 import Web3
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
################################################################################

# total gas paid = unit gas price * amount of gas required for transaction

# Create a function called `generate_account` that automates the Ethereum
# account creation process
def generate_account():
    """Create a digital wallet and Ethereum account from a mnemonic seed phrase."""
    # Access the mnemonic phrase from the `.env` file
    mnemonic=os.getenv('MNEMONIC')

    # Create Wallet object instance
    wallet=Wallet(mnemonic)

    # Derive Ethereum private key
    sk, pk=wallet.derive_account('eth')

    # Convert private key into an Ethereum account
    account=Account.privateKeyToAccount(sk)

    # Return the account from the function
    return account

def get_balance(w3, address): 
    bal_eth=w3.fromWei(w3.eth.get_balance(address), 'ether')
    return bal_eth

def send_transaction(w3, account, receiver, val_eth): 
    val_wei=w3.toWei(val_eth, 'ether')
    raw_tx={'from': account.address, 
            'to': receiver, 
            'value': val_wei, 
            'gas': w3.eth.estimateGas({'from': account.address, 'to': receiver, 'value': val_wei}), 
            'gasPrice': 0, 
            'nonce': w3.eth.getTransactionCount(account.address)}
    signed_tx=account.signTransaction(raw_tx)
    return w3.eth.sendRawTransaction(signed_tx.rawTransaction)












