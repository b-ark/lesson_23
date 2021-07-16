def mult(a: int, n: int) -> int:
    if n < 0:
        raise ValueError("This function works only with positive integers")
    elif a == 0 or n == 0:
        return 0
    elif n == 1:
        return a
    else:
        return (a + mult(a, n - 1))


def main():
    print(mult(2, 4))
    print(mult(2, 0))
    print(mult(2, -4))


if __name__ == '__main__':
    try:
        main()
    except ValueError as massage:
        print(massage)
