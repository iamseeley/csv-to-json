import csv
import json


csv_path = 'data/emojis.csv'

json_path = 'data/emojis.json'

desired_fields = ['#', 'emoji', 'unicode', 'name']

data = []

with open(csv_path, mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        filtered_row = {("number" if field == "#" else field): row[field] for field in desired_fields if field in row or "#" in row}
        data.append(filtered_row)


with open(json_path, mode='w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4, ensure_ascii=False)