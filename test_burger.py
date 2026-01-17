import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import pytest
from burger import Burger

from unittest.mock import Mock


class TestBurger:

    @pytest.fixture
    def burger(self):
        burger = Burger()

        return burger

    @pytest.fixture
    def mock_bun(self):
        mock_bun = Mock()
        mock_bun.get_name.return_value = "ТестБулочка"
        mock_bun.get_price.return_value = 50.0

        return mock_bun
    
    @pytest.fixture
    def mock_ingredient(self):
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 100.0
        mock_ingredient.get_name.return_value = "Бекон"
        mock_ingredient.get_type.return_value = "Мяско"

        return mock_ingredient

    def test_set_buns_correctly(self, burger, mock_bun):
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    def test_add_ingredient_correct(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0].get_name() == "Бекон"
        assert burger.ingredients[0].get_price() == 100.0

    def test_remove_ingredient_correct(self, burger):
        mock1 = Mock()
        mock2 = Mock()
        mock3 = Mock()

        burger.ingredients = [mock1, mock2, mock3]

        burger.remove_ingredient(1)

        assert burger.ingredients == [mock1, mock3]

    def test_move_ingredient(self, burger):
        mock1 = Mock()
        mock2 = Mock()
        mock3 = Mock()

        burger.ingredients = [mock1, mock2, mock3]
        burger.move_ingredient(0, 2)

        assert burger.ingredients == [mock2, mock3, mock1]

    def test_burger_price(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        assert burger.get_price() == 200.0

    def test_receipt_correct(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        receipt = burger.get_receipt()

        assert "(==== ТестБулочка ====)" in receipt  
        assert "= мяско Бекон =" in receipt        
        assert "Price: 200.0" in receipt  
