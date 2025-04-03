# pragma version >= 0.4.0
# @license MIT

from interfaces import i_favorites

list_of_favorites_contract: public(DynArray[i_favorites, 100])
original_favorite_contract: address

@deploy
def __init__(original_favorite_contract: address):
    self.original_favorite_contract = original_favorite_contract

@external
def create_favorite_contract():
    new_favorite_contract: address = create_copy_of(self.original_favorite_contract)
    self.list_of_favorites_contract.append(i_favorites(new_favorite_contract))   

@external
def store_from_factory(favorite_index: uint256, new_number: uint256):
    favorite_contract: i_favorites = self.list_of_favorites_contract[favorite_index]
    extcall favorite_contract.store(new_number)
@view
@external
def view_from_factory(favorites_index: uint256) -> uint256:
    return staticcall self.list_of_favorites_contract[favorites_index].retrieve()
    # favorites_contract: i_favorites = self.list_of_favorite_contracts[favorites_index]
    # value: uint256 = staticcall favorites_contract.retrieve()
    # return value
    

    