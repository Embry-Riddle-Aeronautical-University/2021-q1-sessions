class Foo:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def get_product(self) -> int:
        return self.x * self.y

    def __str__(self):
        return f"This is a Foo with values {self.x}, {self.y}"

    def __repr__(self):
        return f"Foo({self.x},{self.y})"

    def __eq__(self, other):
        if isinstance(other, Foo):
            if self.x == other.x and self.y == other.y:
                return True
        return False


w = 27

if __name__ == "__main__":
    f = Foo(2, 3)
    g = Foo(2, 4)
    print(f)
    print(f == g)
    print(f is g)

    s = g.__repr__()
    print(type(s))
    x = eval(s)
    print(x)
    print(type(x))
