import random
import string

def execute(arguments: dict):

    length = arguments.get("length", 12)

    chars = (
        string.ascii_letters +
        string.digits +
        "!@#$%^&*"
    )

    password = "".join(
        random.choice(chars)
        for _ in range(length)
    )

    return password