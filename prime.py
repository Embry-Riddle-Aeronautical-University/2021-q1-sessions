from math import sqrt


def is_prime(k: int) -> bool:
    """
    A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers
    """
    if k < 2:
        return False
    if k == 2:
        return True
    if k % 2 == 0:
        return False
    for i in range(3, 1 + int(sqrt(k)), 2):
        if k % i == 0:
            return False
    return True


if __name__ == '__main__':
    for i in range(100):
        if is_prime(i):
            print(i, end=", ")
