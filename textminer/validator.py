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
    return re.match(r'^[$]\d+((\,\d{3})?)*(\.\d{2})?$', example)


def zipcode(example):
    return re.match(r'^\d{5}(?:[-\s]\d{4})?$', example)


def date(example):
    return re.match(r'\d+[/-]?\d+[/-]\d+', example)


def email(example):
    return re.findall(r'\w+[\.]?\w+@\w+\.\w+', example)
