import pandas
import pandas as pd
import csv


def is_prime(n):
    if n > 1:
        i = 2
        while i < n//2:
            if n % i == 0:
                return False
            i += 1
        return True
    return False


def is_even(n):
    return n % 2 == 0


def is_palidrom(s:str) -> bool:
    if isinstance(s, str):
        if s == s[::-1]:
            return True
        return False
    else:
        print("provide valid text")
        return False


if __name__ == "__main__":
    d1 = {'foo': 1, 'bar': 2, 'check': 3}
    d2 = {'foo': 4, 'bar': 5, 'check': 6}
    d3 = {'foo': 7, 'bar': 8, 'check': 9}

    d4 = {'foo': [3,4,5], 'bar': [2,3,5], 'check': [1,2,3]}
    l1 = [d1,d2,d3]
    with open('check.csv', 'w', newline='') as file:
        spamwriter = csv.writer(file, delimiter=';')
        spamwriter.writerow(d4.keys())
        spamwriter.writerows(d4.values())

