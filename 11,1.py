from typing import Generator


def is_prime(n: int) -> bool:
    """
    Допоміжна функція: перевіряє, чи є число n простим.
    Оптимізована для швидкості (перевірка до sqrt(n)).
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def prime_generator(end: int) -> Generator[int, None, None]:
    """
    Генерує прості числа в діапазоні від 2 до end (включно).
    """
    number = 2
    while number <= end:
        if is_prime(number):
            yield number
        number += 1



if __name__ == "__main__":
    print(list(prime_generator(10)))

    print(list(prime_generator(30)))