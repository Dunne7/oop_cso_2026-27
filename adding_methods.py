class Rectangle:
    length = 20
    width = 40
    colour = "green"

    def display(self):
        print(f"Rectangle[Length={self.length}, width={self.width}, colour={self.colour}]")

if __name__ == "__main__":
    shape_type = Rectangle()

    print(f"Length: {shape_type.length}")
    print(f"Width: {shape_type.width}")
    print(f"Colour: {shape_type.colour}")

    shape_type.display()

