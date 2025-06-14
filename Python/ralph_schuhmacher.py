import csv
import itertools


list = [
    "du ",
    "willst ",
    "wissen ",
    "wie ",
    "viel ",
    "dein ",
    "Auto ",
    "Wert ",
    "ist? ",
    "Ralph ",
    "Schuh ",
    "macher ",
    ]

def main(list):
    with open('combinations.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # For all possible lengths (1 to len(list))
        for r in range(1, len(list) + 1):
            for combo in itertools.permutations(list, r):
                writer.writerow([''.join(combo)])

main(list)
