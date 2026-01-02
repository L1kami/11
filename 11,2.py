from typing import Generator


def generate_cube_numbers(end_limit: int) -> Generator[int, None, None]:
    """
    Генерує куби чисел починаючи з 2, поки результат менший за end_limit.
    """
    n = 2
    while True:
        cube = n ** 3

        if cube >= end_limit:
            return

        yield cube
        n += 1


if __name__ == "__main__":
    limit = 100
    print(f"Куби чисел, менші за {limit}:")

    for num in generate_cube_numbers(limit):
        print(num)