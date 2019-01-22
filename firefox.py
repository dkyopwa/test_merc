import application
import pytest
from test_goo import Test_Goo

@pytest.fixture(scope='session')
def app():
    return application.Application('Firefox')
