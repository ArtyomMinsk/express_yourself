import re


def words(example):
    string = re.findall(r'[a-z0-9]*\-*[a-z]+', example)
    if string == []:
        return None
    else:
        return string
