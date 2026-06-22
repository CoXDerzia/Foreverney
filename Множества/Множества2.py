first_word = set(input("Напишите первое слово: "))
second_word = set(input("Напишите второе слово: "))

letters_only_in_both = first_word.intersection(second_word)
print("Буквы, которые общие для двух словах: ", letters_only_in_both)

letters_only_in_first = second_word.intersection(first_word)
print("Буквы, которые встречаются только в первом слове: ", letters_only_in_first)

letters_only_in_second = first_word.difference(second_word)
print("Буквы, которые встречаются только во втором слове: ", letters_only_in_second)

all_letters = first_word.union(second_word)
print("Все буквы, которые есть в двух словах: ", all_letters)