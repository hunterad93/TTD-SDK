
from enum import Enum

class DataEventType(Enum):
    """
    An event is an action that a user takes, such as viewing a product page, adding something to a shopping cart, or purchasing a product.
    """
    ADD_TO_CART = "ADD_TO_CART"
    DIRECTION = "DIRECTION"
    LOGIN = "LOGIN"
    LOYALTY_MEMBERS = "LOYALTY_MEMBERS"
    MESSAGE_BUSINESS = "MESSAGE_BUSINESS"
    OTHER = "OTHER"
    PURCHASE = "PURCHASE"
    PURCHASE_CATEGORY = "PURCHASE_CATEGORY"
    SEARCH_CATEGORY = "SEARCH_CATEGORY"
    SEARCH_ITEM = "SEARCH_ITEM"
    SITE_VISIT = "SITE_VISIT"
    START_CHECKOUT = "START_CHECKOUT"
    SUBSCRIBE_TO_NEWSLETTER = "SUBSCRIBE_TO_NEWSLETTER"
    VIEW_CART = "VIEW_CART"
    VIEW_ITEM = "VIEW_ITEM"
    WISH_LIST_ITEM = "WISH_LIST_ITEM"
