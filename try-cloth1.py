class Clothing:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

    def __str__(self):
        return f"{self.name} ({self.color}, {self.size})"

class DressingRoom:
    def __init__(self):
        self.clothes = []

    def add_clothing(self, clothing):
        self.clothes.append(clothing)

    def try_on(self, index):
        if index >= len(self.clothes):
            print("Error: Clothing not found.")
        else:
            print(f"Trying on: {self.clothes[index]}")

# Example usage
room = DressingRoom()
room.add_clothing(Clothing("Shirt", "Blue", "M"))
room.add_clothing(Clothing("Pants", "Black", "L"))
room.try_on(0) # Output: Trying on: Shirt (Blue, M)
room.try_on(1) # Output: Trying on: Pants (Black, L)
room.try_on(2) # Output: Error: Clothing not found.
