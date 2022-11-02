src = not False and True or False and not True  # исходное выражение


# result = True and True or False and False  # избавляемся от отрицаний
# result = True or False  # избавляемся от логического "И"
# result = True  # Избавляемся от логического "ИЛИ"

result = True  # TODO подставить результат выражения

print(src == result)
