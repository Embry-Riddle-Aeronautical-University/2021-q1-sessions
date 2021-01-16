from unittest import TestCase, main
from Foo import Foo


def setUpModule():
    print("Module Setup")


def tearDownModule():
    print("Module clean-up")


class FooTest(TestCase):
    data = None

    @classmethod
    def setUpClass(cls) -> None:
        print("Class Setup")
        cls.data = [(2, 3, 6), (2, 4, 8), (3, 3, 10), (3, 5, 11)]

    @classmethod
    def tearDownClass(cls) -> None:
        print("Class clean-up")

    def setUp(self) -> None:
        print("Test Setup")

    def tearDown(self) -> None:
        print("Test clean-up")

    def test_computation(self):
        f = Foo(2, 3)
        self.assertEqual(6, f.get_product())

    def test_dataset(self):
        print("in test_dataset")
        for x, y, z, in FooTest.data:
            with self.subTest():
                self.assertEqual(z, Foo(x, y).get_product())


if __name__ == "__main__":
    main()
