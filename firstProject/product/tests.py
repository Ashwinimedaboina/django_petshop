from django.test import TestCase
from .models import product

# Create your tests here.
class productTest(TestCase):
    def setUp(self):
        self.Product=product.pm.create(product_name="testproduct",
        product_description="product has been created for testing",
        product_price=500,
        product_brand="producttestBrand")

    def test_create_product(self):
        Product=product.pm.get(product_name="testproduct")   
        self.assertEqual(Product.id,self.Product.id)

    def test_update_product(self):
        Product=product.pm.get(product_name="testproduct")
        Product.product_price=5000
        Product.save()

        self.assertNotEqual(Product.product_price,self.Product.product_price)

    def test_fetch_product(self):
        Products=product.pm.all() 
        count=len(Products) 
        self.assertGreater(count,0)  



