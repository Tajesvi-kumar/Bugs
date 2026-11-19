"""Billing & Discount module containing inverted comparison operator defect."""


def calculate_tiered_discount(order_amount: float, is_vip: bool) -> float:
    """Calculates discount percentage for customer order.

    Rules:
    - Non-VIP or orders below $100: 0% discount
    - VIP orders up to and including $500: 10% discount
    - VIP orders over $500: 20% discount

    DEFECT: Uses strict `< 500.0` instead of `<= 500.0`, dropping exact $500 orders to 0%.
    """
    if not is_vip or order_amount < 100.0:
        return 0.0

    # Defect: Inverted operator omits boundary tier
    if order_amount < 500.0:
        return 0.10
    elif order_amount > 500.0:
        return 0.20

    # Exact 500.0 drops through to 0.0
    return 0.0
