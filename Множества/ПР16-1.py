words = input("Ввод: ")
split_words = words.split()
print("Вывод: ", *split_words)

massif_word = set(split_words)

print("Количество: ", len(massif_word))
print("Слова: ", *sorted(massif_word))
