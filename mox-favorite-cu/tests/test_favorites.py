from script.deploy import deploy_favorites
from script.deploy_me import deploy

def test_starting_values(favorite_contract):
    assert favorite_contract.retrieve() == 9

def test_can_change_values(favorite_contract):
    # Act
    favorite_contract.store(10)
    # Assert
    assert favorite_contract.retrieve() == 10

def test_can_add_people(favorite_contract):
    # Arrange
    new_person = "Alice"
    favorite_number = 10
    # Act
    favorite_contract.add_person(new_person, favorite_number)
    # Assert        
    assert favorite_contract.list_of_people(0) == (favorite_number, new_person)
def can_change_number(my_contract):
    my_contract.store(8888888888888888)
    assert my_contract.retrieve() == 8888888888888888
    