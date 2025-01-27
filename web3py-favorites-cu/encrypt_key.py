import getpass
from eth_account import Account
from pathlib import Path
import json

KEYSTORE_PATH = Path(".keystore.json")

def main():
    private_key = getpass.getpass("Enter your private key:")
    my_account = Account.from_key(private_key)
    password = getpass.getpass("Enter the password to encrypt the key:")
    encrpted_account = my_account.encrypt(password)

    print(f"saving the encrypted key to a file {KEYSTORE_PATH}")
    with KEYSTORE_PATH.open("w") as fp:
        json.dump(encrpted_account, fp)
if __name__ == "__main__":
    main()