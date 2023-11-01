import pytest

pytestmark = pytest.mark.django_db 




class TestCategoryModel:
    def test_string_method(self, category_factory ):
        #Arrnage
        #Act
        x = category_factory(name='test_cat')
        #Assert
        assert x.__str__() == "test_cat"

        pass


class TestBrandModel:
    def test_string_method(self, brand_factory):
        #Arrnage
        #Act
        obj = brand_factory(name='test_brand')
        #Assert
        assert obj.__str__() == 'test_brand'
     


class TestProductModel:
    def test_string_method(self, product_factory):
        #Arrange
        #Act
        obj = product_factory(name="test_product")
        assert obj.__str__() == 'test_product'

        #Assert