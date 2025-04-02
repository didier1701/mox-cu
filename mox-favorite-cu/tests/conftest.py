import pytest
from script.deploy import deploy_favorites


@pytest.fixture(scope= "session")
def favorite_contract():
    favorite_contract = deploy_favorites()
    return favorite_contract