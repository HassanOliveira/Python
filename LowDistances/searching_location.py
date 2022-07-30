from low_distance import citys
import csv

locations = []

with open("all_cities_filter.csv", "r", encoding="utf-8") as source:
    reader = csv.reader(source, delimiter=';')
    locations = []
    for a in citys:
        for r in reader:
            if r != []:
                if r[1] == a:
                    locations.append(r[3])