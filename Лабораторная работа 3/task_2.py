# TODO Напишите функцию find_common_participants
def find_common_participants(first_gr, second_gr, indentation=','):
    first_gr = first_gr.split(indentation)
    second_gr = second_gr.split(indentation)
    first_set = set(first_gr)
    second_set = set(second_gr)
    inter = first_set.intersection(second_set)
    list_res = list(inter)
    list_res.sort()
    return list_res


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))

# TODO Провеьте работу функции с разделителем отличным от запятой