import re


def phone_numbers(text):
    return re.findall(r'\W\d{3}\W+\d{3}\-\d{4}', text)


def emails(text):
    return re.findall(r'\w+[\.]?\w+@\w+\.\w+', text)
