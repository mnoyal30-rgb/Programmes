class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    
    def apply_discount(self, discount_amount):
        if discount_amount > 0 and discount_amount <= self.price:
            self.price -= discount_amount
            print(f"Discount applied: ${discount_amount}. New price: ${self.price}")
        else:
            print("Invalid discount amount!")
    
    def display_mobile(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: ${self.price}")


# Create at least one object and call methods
mobile1 = Mobile("Apple", "iPhone 15 Pro", 999)

# Display initial mobile details
print("=== Initial Mobile Details ===")
mobile1.display_mobile()

# Apply discount
print("\n=== After Discount ===")
mobile1.apply_discount(150)

# Display updated details
print("\n=== Final Mobile Details ===")
mobile1.display_mobile()

# Create a second object to demonstrate multiple objects
print("\n" + "="*30)
mobile2 = Mobile("Samsung", "iphone 16", 899)
mobile2.display_mobile()
mobile2.apply_discount(100)
mobile2.display_mobile()
