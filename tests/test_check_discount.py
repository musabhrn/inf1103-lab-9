from supplier import Supplier
from product import PhysicalProduct
from order import Order
from discount import BulkDiscount, PercentageDiscount
from discount import StudentDiscount

supplier = Supplier("S1", "Test Supplier", "test@example.com")
item = PhysicalProduct("P1", "Test Item", 250.0, 10, supplier, 1.0)

# Test 1: BulkDiscount, then swap to PercentageDiscount
order = Order("T1", BulkDiscount(200, 20))
order.add_order_line(item, 1)

first = order.calculate_total()
print("Bulk discount:", first, "| expected 230.0 |", "PASS" if first == 230.0 else "FAIL")

order.set_discount(PercentageDiscount(10))
second = order.calculate_total()
print("After set_discount:", second, "| expected 225.0 |", "PASS" if second == 225.0 else "FAIL")

# Test 2: two orders sharing the same discount object
shared = PercentageDiscount(10)
o1 = Order("A", shared)
o2 = Order("B", shared)
print("Shared same object:", o1.discount is o2.discount, "| expected True |", "PASS" if o1.discount is o2.discount else "FAIL")

# Student discount
order.set_discount(StudentDiscount())
third = order.calculate_total()
print("Student discount:", third, "| expected 237.5 |", "PASS" if third == 237.5 else "FAIL")