import random
import string
import datetime
import os
import fnmatch


def random_string(string_length=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))


def random_number(number_length=10):
    """Generate a random string of fixed length """
    digits = string.digits
    return ''.join(random.choice(digits) for i in range(number_length))


def random_price(number_length=3):
    return random_number(number_length) + '.' + random_number(2)


def get_date_as_string(days=0, time_format="%Y-%m-%d"):
    date_as_string = (get_now() + datetime.timedelta(days)).strftime(time_format)
    return date_as_string


def get_now():
    return datetime.datetime.now()

def cleanup_results(patterns):
    files = os.listdir('.')
    for pattern in patterns.split(','):            
        for filename in fnmatch.filter(files, pattern):
            try:
                os.remove(filename)
            except OSError:
                print("Error while deleting file")
    pass