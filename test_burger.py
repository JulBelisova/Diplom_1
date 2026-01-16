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
    
    def test_set_buns_correctly(self, burger, mock_bun):
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun