from product_factory import ProductFactory
from supplier import Supplier

s = Supplier("S1", "Test", "t@x.com")
p = ProductFactory.create("physical", "P2", "Mouse", 10.0, 5, s, weight=1.0)
print(type(p).__name__)
ProductFactory.create("service", "P3", "Thing", 10.0, 5, s)