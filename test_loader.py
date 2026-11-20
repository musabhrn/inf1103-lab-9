from inventory_manager import InventoryManager
from supplier import Supplier
from product_loader import load_products

manager = InventoryManager("test_inventory.json")
supplier = Supplier("S000", "Default Supplier", "none@example.com")
load_products("products.csv", manager, supplier)