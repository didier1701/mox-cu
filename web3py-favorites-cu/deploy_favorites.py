from vyper import compile_code
from web3 import Web3, EthereumTesterProvider
import os
from dotenv import load_dotenv
from encrypt_key import KEYSTORE_PATH
import getpass
from eth_account import Account

load_dotenv()
RPC_URL = os.getenv("RPC_URL")
MY_ADDRESS = os.getenv("MY_ADDRESS")
def main():
    print("let's read in a vypper codes and deploy it to the blockchain!")
    with open("favorites.vy", "r") as favorotes_file:
        favorites_code = favorotes_file.read()
        compilation_details = compile_code(favorites_code, output_formats=["bytecode", "abi"])
        print(compilation_details)
    w3 = Web3(Web3.HTTPProvider(RPC_URL))
    favourite_contract = w3.eth.contract( bytecode=compilation_details["bytecode"], abi=compilation_details["abi"])
    print(favourite_contract)

    # to deploy thi will require a transaction
    print("Building a transaction...")
    nonce = w3.eth.get_transaction_count(MY_ADDRESS)
    transaction = favourite_contract.constructor().build_transaction(
        {
            "nonce": nonce,
            "from": MY_ADDRESS,
            "gasPrice": w3.eth.gas_price,
        }
    )
    private_key = decrypt_key()
    print(transaction)
    signed_transaction =  w3.eth.account.sign_transaction(transaction, private_key = private_key)
    print(signed_transaction)

    tx_hash = w3.eth.send_raw_transaction(signed_transaction.raw_transaction)
    print(f"tx_hash: {tx_hash.hex()}")
    tex_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"Done! transaction has been deployed!: {tex_receipt}")

def decrypt_key():
    with open(KEYSTORE_PATH, "r") as fp:
        encrypted_account = fp.read()
        password = getpass.getpass("Enter the password to decrypt the key:")
        key = Account.decrypt(encrypted_account, password)
        print(f"Decrypted key: {key.hex()}")
if __name__ == "__main__":
    main()
