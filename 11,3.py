def is_even(number: int) -> bool:
    """
    Перевіряє, чи є число парним, використовуючи побітове 'І'.
    Повертає True, якщо парне, і False, якщо непарне.
    """
    return (number & 1) == 0

if __name__ == "__main__":
    print(is_even(10))           # True
    print(is_even(11))           # False
    print(is_even(999999999999)) # False
    print(is_even(0))            # True
    print(is_even(-42))          # True