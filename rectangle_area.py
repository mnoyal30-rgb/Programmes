# Rectangle Area Calculator

class Rectangle:
    # Initialize with length and breadth
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    # Method to calculate area
    def calculate_area(self):
        return self.length * self.breadth
    
    # Method to update dimensions
    def update_dimensions(self, new_length, new_breadth):
        self.length = new_length
        self.breadth = new_breadth


# Create an object and test methods
rect = Rectangle(10, 5)

# Test calculate_area()
print("Initial Dimensions:")
print(f"Length: {rect.length}, Breadth: {rect.breadth}")
print(f"Area: {rect.calculate_area()}")

# Test update_dimensions()
rect.update_dimensions(8, 6)
print("\nAfter updating dimensions to length=8, breadth=6:")
print(f"Length: {rect.length}, Breadth: {rect.breadth}")
print(f"Area: {rect.calculate_area()}")
