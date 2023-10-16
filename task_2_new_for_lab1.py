# TODO Найдите количество книг, которое можно разместить на дискете

disk_memory = 1.44 * 1024 * 1024
book_memory = 4 * 25 * 50 * 100
book_count = int(disk_memory // book_memory)

#print("Общая память дискеты:", disk_memory)
#print("Занимаемая память в книге:", book_memory)
print("Количество книг, помещающихся на дискету:", book_count)
