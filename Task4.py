def reverse(input_str: str) -> str:
    if len(input_str) == 1:
        return input_str
    elif len(input_str) == 2:
        return input_str[-1] + input_str[0]
    else:
        return reverse(input_str[1:]) + input_str[0]


def main():
    print(reverse("hello"))
    print(reverse("o"))


if __name__ == '__main__':
    try:
        main()
    except ValueError as massage:
        print(massage)
