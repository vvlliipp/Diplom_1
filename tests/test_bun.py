import pytest
from bun import Bun
from helpers import Burger_Info

@pytest.mark.parametrize('name, price, expected_name', [
    (Burger_Info.Bun_1, Burger_Info.Price_Bun, Burger_Info.Bun_1),
    (Burger_Info.Bun_2, Burger_Info.Price_Bun, Burger_Info.Bun_2),
])
def test_bun_get_name(name, price, expected_name):
    bun = Bun(name, price)
    assert bun.get_name() == expected_name
