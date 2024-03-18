import pytest
from src.classes import Category
from src.classes import Product


@pytest.fixture()
def Category_Phone():
    return Category('nokia', 'plastic', '6230i')


def test_init(Category_Phone):
    assert Category_Phone.name == 'nokia'
    assert Category_Phone.description == 'plastic'
    assert Category_Phone.product == '6230i'
    assert Category_Phone.number_of_categories == 1
    assert Category_Phone.unique_product == 1


@pytest.fixture()
def Product_Samsung():
    return Product('tv', '65', 'lcd', 1)


def test_init2(Product_Samsung):
    assert Product_Samsung.name == 'tv'
    assert Product_Samsung.description == '65'
    assert Product_Samsung.price == 'lcd'
    assert Product_Samsung.availability == 1
