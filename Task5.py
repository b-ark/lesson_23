from typing import Union


def sum_of_digits(digit_string: Union[str, int]) -> int:
    if isinstance(digit_string, str):
        if not digit_string.isdigit():
            raise ValueError("input string must be digit string")
        else:
            digit_string = int(digit_string)
    if digit_string == 0:
        return 0
    return digit_string % 10 + sum_of_digits(digit_string // 10)


def main():
    print(sum_of_digits('26'))
    print(sum_of_digits('1111'))
    sum_of_digits('test')


if __name__ == '__main__':
    try:
        main()
    except ValueError as massage:
        print(massage)
