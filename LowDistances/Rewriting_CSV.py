import csv

with open("all_cities.csv", "r", encoding="utf-8") as source:
    reader = csv.reader(source, delimiter=';')
    with open("all_cities_filter.csv", "w", encoding="utf-8") as result:
        writer = csv.writer(result, delimiter=';')
        for r in reader:
            writer.writerow((r[0], r[2], r[7], r[19]))