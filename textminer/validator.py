import re


def binary(example):
    return re.match(r'[01]', example)


def binary_even(example):
    return re.match(r'[01]+0$', example)


def hex(example):
    return re.match(r'^[A-F0-9]+$', example)


def word(example):
    return re.match(r'^[a-z0-9\-]+[a-z]+$', example)


def words(example, count=None):
    string = re.findall(r'[a-z0-9]*\-*[a-z]+', example)
    if count is None:
        return len(string) == len(example.split(' '))
    else:
        return len(string) == count


def phone_number(example):
    return re.match(r'\(?(\d{3})\)?[-.]?.*(\d{3})[-.]?(\d{4})', example)


def money(example):
    # return re.match(r'^[$]\d+[\.,]?(\d+)?[\.,]?(\d+)?[\.,]?(\d+)?', example)
    return re.match(r'^[$]\d+((\,\d{3})?)*(\.\d{2})?$', example)
    # (\.\d{2})?
    # ((\,\d{3})?)*
# assert v.money("$4")
# assert v.money("$19")
# assert v.money("$19.00")
# assert v.money("$3.58")
# assert v.money("$1000")
# assert v.money("$1000.00")
# assert v.money("$1,000")
# assert v.money("$1,000.00")
# assert v.money("$5,555,555")
# assert v.money("$5,555,555.55")
# assert v.money("$45,555,555.55")
# assert v.money("$456,555,555.55")
# assert v.money("$1234567.89")
# assert not v.money("")
# assert not v.money("$12,34")
# assert not v.money("$1234.9")
# assert not v.money("$1234.999")
# assert not v.money("$")
# assert not v.money("31")
# assert not v.money("$$31")


def zipcode(example):
    return re.match(r'^\d{5}(?:[-\s]\d{4})?$', example)


def date(example):
    return re.match(r'\d+[/-]?\d+[/-]\d+', example)


def email(example):
    return re.findall(r'\w+[\.]?\w+@\w+\.\w+', example)
