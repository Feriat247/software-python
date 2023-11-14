# TODO решите задачу
import json

INPUT_FILE = 'input.json'

def task() -> float:
    with open(INPUT_FILE, encoding='utf-8') as file:
        data = json.load(file)

        sum = 0
        for current_data in data:
            sum += current_data['score'] * current_data['weight']
        return round(sum,3)


print(task())
