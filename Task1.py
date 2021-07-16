from typing import Union


def to_power(x: Union[int, float], exp: int) -> Union[int, float]:
    """Returns  x ^ exp"""
    if exp <= 0:
        raise ValueError('This function works only with exp > 0.')

    elif exp == 1:
        return x

    else:
        return (x * to_power(x, exp - 1))


def main():
    print(to_power(2, 3))
    print(to_power(3.5, 2))
    print(to_power(2, -1))


if __name__ == '__main__':
    try:
        main()
    except ValueError as massage:
        print(massage)
