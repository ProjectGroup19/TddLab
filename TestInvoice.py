import pytest
from Invoice import Invoice

@pytest.fixture()
def products():
    products = {'Pen' : {'qnt' : 10, 'unit_price' : 3.75, 'discount' : 5},
                'Notebook' : {'qnt' : 5, 'unit_price' : 7.5, 'discount' : 10}}
    return products

@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice

def test_CanCalculateTotalImpurePrice(invoice, products):
    invoice.totalImpurePrice(products)
    assert invoice.totalImpurePrice(products) == 75

def test_CanCalculateTotalDiscount(invoice, products):
    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.62

def test_CalCalculateTotalPurePrice(invoice, products):
    invoice.totalPurePrice(products)
    assert invoice.totalPurePrice(products) == 69.38

# New Test case 1
def test_AddProduct(invoice, products):
    products['New Product'] = invoice.addProduct(5, 7, 3)
    assert products['New Product']['qnt'] == 5
    assert products['New Product']['unit_price'] == 7
    assert products['New Product']['discount'] == 3

# New Test case 2
def test_RemoveProduct(invoice, products):
    assert invoice.removeProduct('Pen', products) == {'qnt' : 10, 'unit_price' : 3.75, 'discount' : 5}
    try:
        products['Pen'] == {}
    except:
        assert True
