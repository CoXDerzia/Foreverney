while True:
    stroki = int(input("Введите количество строк(Меньше или равно 10): "))

    if stroki > 10:
        print("Слишком большое количество символов, попробуйте еще раз")
        continue

    result = []

    for i in range(stroki):
        sim_stroki = input("Введите символ: ")
        result.extend(list(sim_stroki))
    print(*result, sep=", ")
    break