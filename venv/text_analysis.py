# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

from collections import Counter

text = 'Родился 7 ноября 1879 года (26 октября по старому стилю) в деревне Яновка Елисаветградского уезда Херсонской ' \
       'губернии Российской империи (ныне - село Береславка Кировоградской области Украины). Его отец был крупным ' \
       'землевладельцем-арендатором, торговцем зерном. Настоящее имя - Лейба Бронштейн. Учился в еврейской ' \
       'религиозной школе - хедере, в 1896 году окончил Николаевское реальное училище. Высшего образования не ' \
       'получил. ' \
       'Жизнь и революционная деятельность до 1917 года. С середины 1890-х годов увлекся народническими, ' \
       'а затем социалистическими идеями, в 1896 году стал одним из создателей социал-демократической организации ' \
       '"Южнорусский рабочий союз" в г. Николаеве. Писал листовки, выступал на митингах, \ участвовал в издании ' \
       'подпольной газеты. В 1898 году был арестован и на следующий год приговорен к четырем годам' \
       'высылки в Иркутскую губернию. В ссылке служил приказчиком у купца, затем сотрудничал в иркутской газете ' \
       '"Восточное " \ "обозрение". С 1900 года - сторонник марксизма. В августе 1902 года, оставив жену и двух ' \
       'дочерей, ' \
       'бежал за границу. Во время побега использовал поддельный паспорт, куда вписал фамилию надзирателя одесской ' \
       'тюрьмы Троцкого, ставшую впоследствии его псевдонимом. В 1902-1905 годах жил в эмиграции в Европе. В Лондоне ' \
       'познакомился с одним из лидеров российских социал-демократов Владимиром Лениным (Ульяновым), ' \
       'который предложил ему сотрудничать в газете "Искра". В июле-августе 1903 года участвовал во II съезде ' \
       'Российской социал-демократической партии (РСДРП). В ходе произошедшего в партии раскола выступил против ' \
       'Ленина, обвинив его в стремлении установить среди партийцев "казарменный режим", и примкнул к меньшевикам. ' \
       'Однако позднее занял внефракционную позицию. В феврале 1905 года нелегально вернулся в Россию, где принял ' \
       'активное участие в революции 1905-1907 годов В октябре-декабре 1905 года входил в исполком Петербургского ' \
       'Совета ' \
       'рабочих депутатов, играл ведущую роль в его президиуме. Являлся редактором печатного органа Совета - газеты ' \
       '"Известия". В декабре 1905 года был арестован после публикации Советом финансового манифеста, содержащего ' \
       'призывы к акциям гражданского неповиновения (отказу от уплаты налогов и др.). В заключении сформулировал ' \
       'теорию "перманентной революции", разработанную вместе с Александром Парвусом (Гельфандом). Согласно ей, ' \
       '"социалистическая революция начинается на национальной арене, развивается на интернациональной и завершается ' \
       'на мировой". '

def text_low(text):
    return text.lower()

def text_separate(text, delimiter):
    return text.split(delimiter)

def replace(text):
    return text.replace('  ', ' ')

def remove(text):
    chars_to_remove = ".,-—!\"?()/:"
    trans = str.maketrans('', '', chars_to_remove)
    return text.translate(trans)

def count(text):
    return Counter(text)

def most_common(text, count):
    return text.most_common(count)

text_list = text_separate(text_low(replace(remove(text))), ' ')
print('В введенной строке ', len(text_separate(text_low(text), ' ')), ' слов')
print('10 наиболее часто повторяющихся слов ', most_common(count(text_list), 10))
