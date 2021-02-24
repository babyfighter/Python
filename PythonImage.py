from PIL import Image
import csv


data = open('example.csv', encoding='utf-8')
csv_data = csv.reader(data)
data_lines = list(csv_data)
for line in data_lines[:5]:
    print(line)
