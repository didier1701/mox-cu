from vyper import compile_code
from web3 import Web3
from dotenv import load_dotenv
import os
from encrypt_key import KEYSTORE_PATH
import getpass
from eth_account import Account

load_dotenv()

RPC_URL = os.getenv("RPC_URL")
MY_ADDRESS = os.getenv("MY_ADDRESS")

def main():
    print(" Getting into Deploying favorites...")
    with open("favorites.vy", "r") as favorite_file:
        favorites_code = favorite_file.read()
        compilation_details = compile_code(favorites_code, output_formats=["bytecode", "abi"])
        print(compilation_details)
    print("Deployed favorites!")
    
    w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
    favorite_contract = w3.eth.contract( bytecode=compilation_details["bytecode"], abi=compilation_details["abi"])

    print("bulding transaction...")
    nonce = w3.eth.get_transaction_count(MY_ADDRESS)
    transaction = favorite_contract.constructor().build_transaction({
        "from": MY_ADDRESS,
        "nonce": nonce,
        "gas": 1000000,
        "gasPrice": w3.eth.gas_price
    })
    private_key = decrypt_key()
    signed_transaction =  w3.eth.account.sign_transaction(transaction, private_key= private_key)
    print(signed_transaction)

    tx_hash = w3.eth.send_raw_transaction(signed_transaction.raw_transaction)
    print("my tx hash is : ", tx_hash)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print("my tx receipt is : ", tx_receipt)
    print("Deployed favorites contract at: ", tx_receipt["contractAddress"])

def decrypt_key() -> str:
    with KEYSTORE_PATH.open("r") as fp:
        encrypted_account = fp.read()
        password = getpass.getpass("Enter your password: ")
        key = Account.decrypt(encrypted_account, password)
        print("Your private key is: ")
        return key


if __name__ == "__main__":
    main()