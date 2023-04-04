import pytest
from pages.login_page import Login
from pages.list_products_page import Product
from pages.add_to_cart import AddCart
from pages.your_cart_page import YourCart
from pages.details_page import AddPersonalInfo
from pages.finish_purchase_page import PurchaseComplete

@pytest.mark.usefixtures("setup")
class TestPurchaseFlow():
    def test_purchase_flow(self,username):
        login = Login(self.driver)
        login.enterusername_password(username,"secret_sauce")
        login.clicklogin()
        product = Product(self.driver)
        product.select_product('Sauce Labs Bike Light')
        addcart = AddCart(self.driver)
        addcart.add_to_cart()
        cartdetails = YourCart(self.driver)
        cartdetails.checkout_cart()
        personalinfo = AddPersonalInfo(self.driver)
        personalinfo.add_personal_information("Kushagra","Singh","282001")
        verifypurchase = PurchaseComplete(self.driver)
        verifypurchase.vaildate_purchase_success()

