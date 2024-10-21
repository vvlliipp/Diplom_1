import pytest
from praktikum.bun import Bun
from helpers import Burger_Info


@pytest.mark.parametrize('name', [Burger_Info.Bun_1, Burger_Info.Bun_2])
def test_bun_get_name(name):
    bun = Bun(name, 0)
    assert bun.get_name() == name


def test_bun_get_price():
    bun = Bun('Галактика', Burger_Info.Price_Bun)
    assert bun.get_price() == Burger_Info.Price_Bun
