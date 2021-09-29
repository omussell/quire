import secrets

import nacl.encoding
import nacl.hash

from code_books.english import english_code_book
from conversion_tables.english import english_conversion_table

PAGE_SEPARATOR = "-" * 30
HASHER = nacl.hash.blake2b


def random_pad():
    random_numbers = "".join(str(secrets.randbelow(10)) for i in range(250))
    rows = [random_numbers[i : i + 25] for i in range(0, len(random_numbers), 25)]

    for row in rows:
        group = [row[i : i + 5] for i in range(0, len(row), 5)]
        print(" ".join(group))


def pad_identifier():
    random_numbers = "".join(str(secrets.randbelow(10)) for i in range(50))
    digest = HASHER(bytes(random_numbers, "UTF-8"), encoder=nacl.encoding.HexEncoder)

    return digest.decode()


def quire():
    print(pad_identifier())
    print(PAGE_SEPARATOR)
    for _ in range(50):
        random_pad()
        print(PAGE_SEPARATOR)
    print(english_conversion_table)
    print(english_code_book)


quire()
