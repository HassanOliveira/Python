from adding_cities import citys
import csv

locations = []

for a in citys:
    with open("all_cities_filter.csv", "r", encoding="utf-8") as source:
        reader = csv.reader(source, delimiter=';')
        for r in reader:
            if r != []:
                if r[1] == a:
                    locations.append(r[3])

