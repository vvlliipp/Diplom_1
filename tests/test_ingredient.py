import pytest
from praktikum.ingredient import Ingredient
from helpers import Burger_Info


@pytest.mark.parametrize("ingredient_type, name, price", [
    ("sauce", Burger_Info.Sauce, Burger_Info.Price_Sauce),
    ("filling", Burger_Info.Filling, Burger_Info.Price_Filling),
])
def test_ingredient_get_price(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type=ingredient_type, name=name, price=price)
    assert ingredient.get_price() == price, "Неверная цена ингредиента"


@pytest.mark.parametrize("ingredient_type, name, price", [
    ("sauce", Burger_Info.Sauce, Burger_Info.Price_Sauce),
    ("filling", Burger_Info.Filling, Burger_Info.Price_Filling),
])
def test_ingredient_get_name(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type=ingredient_type, name=name, price=price)
    assert ingredient.get_name() == name, "Неверное название ингредиента"


@pytest.mark.parametrize("ingredient_type, name, price", [
    ("sauce", Burger_Info.Sauce, Burger_Info.Price_Sauce),
    ("filling", Burger_Info.Filling, Burger_Info.Price_Filling),
])
def test_ingredient_get_type(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type=ingredient_type, name=name, price=price)
    assert ingredient.get_type() == ingredient_type, "Неверный тип ингредиента"
