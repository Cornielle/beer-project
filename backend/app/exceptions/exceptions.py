class InvalidItemNameException(Exception):
    def __init__(self, item_name):
        self.message = f"Item name '{item_name}' is not valid."
