def get_count_char(str_):
    str1 = str_.lower()
    alpha_list = list(str1)

    alphas_dict = {}
    for alpha in alpha_list:
        if alpha in alphas_dict:
            alphas_dict[alpha] += 1
        else:
            alphas_dict[alpha] = 1

    alphas_dict
    print(alphas_dict)

    ...  # TODO посчитать количество каждой буквы в строке в аргументе str_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
