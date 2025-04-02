from src import favorites
from moccasin.boa_tools import VyperContract
from moccasin.config import get_active_network

def deploy_favorites() -> VyperContract:
    favorite_contract: VyperContract = favorites.deploy()
    starting_number: int = favorite_contract.retrieve()
    print("Starting number is: ", starting_number)

    favorite_contract.store(9)
    ending_number: int = favorite_contract.retrieve()
    print("Ending number is: ", ending_number)

    active_network = get_active_network()
    if active_network.has_explorer():
        result = active_network.moccasin_verify(favorite_contract)
        result.wait_for_verification()
    return favorite_contract

def moccasin_main() -> VyperContract:
    return deploy_favorites()


