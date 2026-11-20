from supplier import Supplier
from product import PhysicalProduct
from order_line import OrderLine

s = Supplier("S1", "Test", "t@x.com")
p = PhysicalProduct("P1", "Item", 10.0, 5, s, 1.0)
for test in [lambda: PhysicalProduct("P2", "X", 0, 5, s, 1.0),
             lambda: PhysicalProduct("P3", "X", 10.0, -1, s, 1.0),
             lambda: p.update_stock(-5),
             lambda: OrderLine(p, 0)]:
    try:
        test()
        print("No error (FAIL)")
    except ValueError as e:
        print("ValueError:", e, "(PASS)")