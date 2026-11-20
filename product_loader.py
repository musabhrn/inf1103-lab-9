import csv
from product_factory import ProductFactory
from inventory_manager import InventoryManager
from supplier import Supplier


def load_products(path: str, inventory: InventoryManager, supplier: Supplier) -> None:
    try:
        file = open(path, newline="")
    except FileNotFoundError:
        print(f"Products file not found: {path}")
    else:
        loaded = 0
        with file:
            reader = csv.reader(file)
            next(reader)  # skip the header row
            for row in reader:
                try:
                    product_type, product_id, name, price, stock = row
                    product = ProductFactory.create(
                        product_type.strip(), product_id.strip(), name.strip(),
                        float(price), int(stock), supplier
                    )
                    inventory.add_product(product)
                    loaded += 1
                except ValueError as e:
                    print(f"Skipped row {row}: {e}")
        print(f"{loaded} products loaded.")
    finally:
        print("Load attempt finished.")