from product import Product
from order_line import OrderLine
from discount import DiscountStrategy, NoDiscount


class Order:
    """Holds the order lines and applies a discount strategy to the total."""

    def __init__(self, order_id: str, discount: DiscountStrategy | None = None) -> None:
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []
        self.discount: DiscountStrategy = discount if discount is not None else NoDiscount()

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.order_lines.append(order_line)

    def set_discount(self, discount: DiscountStrategy) -> None:
        self.discount = discount

    def calculate_total(self) -> float:
        """Calculates and returns the total value of the order after discount."""
        total = sum(line.calculate_subtotal() for line in self.order_lines)
        return self.discount.apply(total)