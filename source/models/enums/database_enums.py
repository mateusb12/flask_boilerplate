from enum import Enum


class OrderStatus(Enum):
    IN_PREPARATION = 'In preparation'
    OUT_FOR_DELIVERY = 'Out for delivery'
    ORDER_CONFIRMED = 'Order Confirmed'
    ORDER_DELAYED = 'Order Delayed'