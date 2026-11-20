from supplier import Supplier
from product import Product, PhysicalProduct, DigitalProduct
from inventory_manager import InventoryManager

def test_demonstrate_polymorphism() -> None:
    supplier = Supplier("S001", "Global Supplier", "contact@global.com")
    laptop = PhysicalProduct("P01", "Laptop", 1200.0, 5, supplier, 2.5)
    ebook = DigitalProduct("D01", "Python eBook", 35.0, 100, supplier, 12.0)

    inventory = InventoryManager() 
    inventory.products = [laptop, ebook] 

    print("=== 7.2 Polymorphism Demonstration ===")

    for product in inventory.products:
        product.display_information()
        print(f"Fulfilment: {product.get_fulfilment_info()}\n")

if __name__ == "__main__":
    test_demonstrate_polymorphism()