import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    csv_data = []
    with open(INPUT_FILENAME, encoding="utf-8") as input_f:
        csv_reader = csv.reader(input_f)
        headers = next(csv_reader)
        for row in csv_reader:
            csv_data.append(row)

    json_data = []
    for row in csv_data:
        json_row = {}
        for i in range(len(headers)):
            json_row[headers[i]] = row[i]
        json_data.append(json_row)

    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as output_f:
        json.dump(json_data, output_f, indent=4)


if __name__ == '__main__':
    task()
