import random
import string


class RandomString:

    def __init__(self):
        self.letters = string.ascii_letters
        self.digits = string.digits

    def choose_letters(self, string_length: int = 10) -> str:
        return ''.join(random.choice(self.letters) for _ in range(string_length))

    def choose_number(self, string_length: int = 10) -> str:
        return ''.join(random.choice(self.digits) for _ in range(string_length))

    def choose_letters_and_numbers(self, string_length: int = 10) -> str:
        return ''.join(random.choice(self.digits + self.letters) for _ in range(string_length))
