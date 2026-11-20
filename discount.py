from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    """Interface for all discount strategies."""
    @abstractmethod
    def apply(self, total: float) -> float:
        pass


class NoDiscount(DiscountStrategy):
    """Returns the total unchanged."""
    def apply(self, total: float) -> float:
        return total


class PercentageDiscount(DiscountStrategy):
    """Takes a percentage off the total, e.g. PercentageDiscount(10) takes 10% off."""
    def __init__(self, percentage: float) -> None:
        self._percentage: float = percentage

    def apply(self, total: float) -> float:
        return total * (1 - self._percentage / 100)


class BulkDiscount(DiscountStrategy):
    """Takes a fixed amount off totals at or above a threshold, e.g. BulkDiscount(200, 20)."""
    def __init__(self, threshold: float, amount: float) -> None:
        self._threshold: float = threshold
        self._amount: float = amount

    def apply(self, total: float) -> float:
        if total >= self._threshold:
            return total - self._amount
        return total

class StudentDiscount(DiscountStrategy):
    """Takes 5% off the total for students."""
    def apply(self, total: float) -> float:
        return total * 0.95