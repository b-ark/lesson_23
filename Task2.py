def is_palindrome(looking_str: str) -> bool:
    if len(looking_str) == 1:
        return True
    if looking_str[0] != looking_str[-1]:
        return False
    if len(looking_str) == 2:
        return True
    return is_palindrome(looking_str[1:-1])


def main():
    print(is_palindrome('mom'))
    print(is_palindrome('sassas'))
    print(is_palindrome('o'))
    print(is_palindrome('qw'))


if __name__ == '__main__':
    try:
        main()
    except ValueError as massage:
        print(massage)
