#Дан список повторяющихся элементов.
#Вернуть список с дублирующимися элементами.
#В результирующем списке не должно быть дубликатов.

my_list = [2, 2, 1, 7, 'g', 'g', 'h']

def search (name_list):
    doublication = []
    for i in range(0, len(my_list)):
        for j in range(0, len(my_list)):
            if name_list[i] in doublication:
                j += 1
            else:
                if i == j:
                    j += 1
                else:
                    if name_list[i] == name_list[j]:
                        doublication.append(name_list[i])
                        j += 1
                    else:
                        j += 1
    return doublication

print('В списке ', my_list, ' найдены следующие повторяющиеся элементы ', search(my_list))


