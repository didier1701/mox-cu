# pragma version >= 0.4.0
# @license MIT

# we import the favorites module into this contract 
import favorites

# we import a module we would like to use in the contract
import favorites_factory

# we initialize the module so as to able to access it 
initializes: favorites
initializes: favorites_factory
#exports: ( favorites.__interface__) <- This help us select all the functions of our imported module for availability in this module
# we select the functions we want to make available from our target_lock module

exports: (
    favorites.retrieve,
    favorites.add_person
)
exports: (
    favorites_factory.view_from_factory
)
@deploy
def __init__():
    favorites.__init__()
    favorites_factory.__init__()

@external
def store(new_number: uint256):
    favorites.my_favorite_number = new_number + 5




# @external
# def store(favorite_number: uint256):
#     self.my_favorite_number = favorite_number