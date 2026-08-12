def greet_user(name):
    return f"Hey, {name}!"


def add_numbers(a, b):
    return a + b


if __name__ == "__main__":
    name = "Sandhya"

    print(greet_user(name))

    result = add_numbers(10, 20)

    print(f"Sum = {result}")