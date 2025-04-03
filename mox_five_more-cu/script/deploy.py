from src import favorites, favorites_factory, five_more
from moccasin.boa_tools import VyperContract

def deploy_favorites() -> VyperContract:
    favorites_contract: VyperContract = favorites.deploy()
    return favorites_contract

def deploy_factory(favorites_contract: VyperContract):
    factory_contract: VyperContract = favorites_factory.deploy(favorites_contract.address)
    factory_contract.create_favorite_contract()

    new_favorites_address: str = factory_contract.list_of_favorites_contract(0)
    new_favorites_contract: VyperContract = favorites.at(new_favorites_address)
    new_favorites_contract.store(88)
    print(f"Stored value is: {new_favorites_contract.retrieve()}")

    factory_contract.store_from_factory(0, 99)
    print(f"New contract stored value is {new_favorites_contract.retrieve()}")
    print(f"Original contract stored value is {favorites_contract.retrieve()}")

def deploy_five_more():
    five_more_contractt = five_more.deploy()
    five_more_contractt.store(55)
    print(five_more_contractt.retrieve())


def moccasin_main():
    favorites_contract = deploy_favorites()
    deploy_factory(favorites_contract)
    deploy_five_more()