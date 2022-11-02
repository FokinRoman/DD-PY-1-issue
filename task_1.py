list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
i_max = 0

for i in range(len(list_numbers)):
    max_a = list_numbers[i_max]
    current_a = list_numbers[i]
    if current_a > max_a:
        i_max = i  # перебор, аналогичный представленному в теоретическом блоке

a, b = max(list_numbers), list_numbers[-1]
a, b = b, a
list_numbers[-1], list_numbers[i_max] = b, a  # сама замена мест элементов списка

print(list_numbers)