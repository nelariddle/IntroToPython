def print_name(name):
    """prints the name input provided

    Args:
        name (string): the name to be printed
    """
    print("my name is", name)


# print_name("nela")


def area_of_triangle(base, height):
    """calculates the area of a triangle

    Args:
        base (float): length of base
        height (float): length of height

    Returns:
        float: the total area
    """
    return base * height / 2


# print(area_of_triangle(4, 5))

import math


def hypotenuse(a, b):
    """finds the hypotenuse of a right triangle

    Args:
        a (float): the first leg
        b (float): the second leg

    Returns:
        float: the hypotenuse
    """
    return math.sqrt(a**2 + b**2)


# print(hypotenuse(3, 4))


def print_name_and_age(name, age):
    """prints both the name and age

    Args:
        name (string): the name to print
        age (string): the age to print
    """
    print("my name is", name, "and i am", age)


# print_name_and_age("nela", 123)


def area_of_circle(r):
    """calculates the area of a circle

    Args:
        r (float): radius of the circle

    Returns:
        float: the total area
    """
    return math.pi * r**2


# print(area_of_circle(4))


from datetime import datetime


def time_since(date_day, date_month, date_year):
    """calculates the time from a date until now

    Args:
        date_day (int): the day of the date
        date_month (int): the month of the date
        date_year (int): the year of the date

    Returns:
        datetime: a datetime representing the time gap
    """
    current_date = datetime.now()
    provided_date = datetime(date_year, date_month, date_day)
    time_difference = current_date - provided_date

    return time_difference


# print(time_since(12, 5, 2002))


def factorial(n):
    """finds the factorial of a number

    Args:
        n (int): number to find factorial of

    Returns:
        int: the factorial
    """
    if n == 1:
        return 1
    return n * factorial(n - 1)


# print(factorial(5))


def print_names(names):
    """prints each name in a list of names

    Args:
        names (list): a list of names
    """
    for name in names:
        print_name(name)


print_names(["nela", "stuti", "dikshita"])


import random


def approximate_pi(n):
    """a monte carlo approximation of pi

    Args:
        n (int): number of iterations
    """
    count = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        z = hypotenuse(x, y)
        if z < 1:
            count += 1

    return count / n * 4


# print(approximate_pi(1000000))


def nato_translation(name):
    """finds a word's spelling in the NATO alphabet

    Args:
        name (string): any word

    Returns:
        string: the NATO translation
    """
    dictionary = {
        "A": "Alpha",
        "B": "Bravo",
        "C": "Charlie",
        "D": "Delta",
        "E": "Echo",
        "F": "Foxtrot",
        "G": "Golf",
        "I": "India",
        "J": "Juliet",
        "K": "Kilo",
        "L": "Lima",
        "M": "Mike",
        "N": "November",
        "O": "Oscar",
        "P": "Papa",
        "Q": "Quebec",
        "R": "Romeo",
        "S": "Sierra",
        "T": "Tango",
        "U": "Uniform",
        "V": "Victor",
        "W": "Whiskey",
        "X": "Xray",
        "Y": "Yankee",
        "Z": "Zulu",
    }
    output = ""

    for char in name:
        output += dictionary[char.upper()]
        # same as output = output + dictionary[char]

    return output


# print(nato_translation("Nela"))


def reverse(name):
    """reverses a string

    Args:
        name (string): string to be reversed

    Returns:
        string: the reverse of the input string
    """
    output = ""

    for char in name:
        output = char + output
    return output


# print(reverse("women who code"))


# make sure you do pip install requests and pip install beautifulsoup4 in terminal
import requests
from bs4 import BeautifulSoup


def national_debt():
    """finds the current national debt

    Returns:
        string: the national debt, in dollar format
    """
    url = "https://www.pgpf.org/national-debt-clock"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    span_element = soup.find("span", class_="ticker")
    ticker_text = span_element.text
    return ticker_text


# print(national_debt())


def per_person_debt():
    """finds the current national debt per person

    Returns:
        string: the national debt per person
    """
    url = "https://www.pgpf.org/national-debt-clock"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    span_element = soup.find("div", class_="per-person-debt-num")
    ticker_text = span_element.text
    return ticker_text


# print(per_person_debt())


def dollars_to_int(dollars):
    """converts a string-formatted dollar amount to int

    Args:
        dollars (string): a string containing a dollar amount, possibly with $ and ,

    Returns:
        int: the dollar amount in integer format
    """
    output = ""
    for char in dollars:
        if not char == "$" and not char == ",":
            output += char
    return int(output)


# print(dollars_to_int(per_person_debt()))

# print(dollars_to_int(national_debt()) / dollars_to_int(per_person_debt()))


def word_counts():
    """finds the counts of each word in a file

    Returns:
        dict: a dictionary containing word:count
    """
    counts = {}
    with open("iu.txt", "r", encoding="utf-8") as file:
        for line in file:
            for word in line.split():
                if word in counts:
                    counts[word] += 1
                else:
                    counts[word] = 1

    return counts


def bigram_counts():
    """finds the counts of each bigram in a file

    Returns:
        dict: a dictionary containing bigram:count
    """
    counts = {}
    with open("iu.txt", "r", encoding="utf-8") as file:
        for line in file:
            words = line.split()
            for i in range(len(words) - 1):
                bigram = words[i] + " " + words[i + 1]
                if bigram in counts:
                    counts[bigram] += 1
                else:
                    counts[bigram] = 1

    return counts


def trigram_counts():
    """finds the counts of each trigram in a file

    Returns:
        dict: a dictionary containing trigram:count
    """
    counts = {}
    with open("iu.txt", "r", encoding="utf8") as file:
        for line in file:
            words = line.split()
            for i in range(len(words) - 2):
                trigram = words[i] + " " + words[i + 1] + " " + words[i + 2]
                if trigram in counts:
                    counts[trigram] += 1
                else:
                    counts[trigram] = 1

    return counts


import csv


def write_word_counts(counts):
    """takes a dictionary of counts (outputted from before) and writes to a csv

    Args:
        counts (dict): a dictionary of containing string:count
    """
    with open("counts.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        for key, value in counts.items():
            writer.writerow([key, value])


# words = trigram_counts()
# write_word_counts(words)
