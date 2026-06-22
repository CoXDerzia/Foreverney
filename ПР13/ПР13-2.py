while True:
    stroki = int(input("Введите количество строк(Меньше или равно 10): "))
    result = []
    if stroki > 10:
        print("Слишком большое количество символов, попробуйте еще раз")
        continue
    for i in range(stroki):
        sim_stroki = input("Введите символ: ")
        simvol = list(sim_stroki)
        result.append(simvol)
    print(result)
    break