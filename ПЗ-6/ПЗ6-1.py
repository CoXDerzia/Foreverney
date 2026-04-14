temp = int(input("Введите температуру: "))
pressure = int(input("Введите давление: "))
pulse = int(input("Введите пульс: "))
if (36<= temp >= 37) and (110<= pressure>= 130) and (60<= pulse >= 100):
    print("У вас нормальное состояние")
elif (35<temp<36) or (37<temp<38) or (105<pressure<110) or (130<pressure<140) or (55<pulse<60) or (100<pulse<110):
    print("У вас легкое недомогание")
elif (25< temp <35) or (38<temp<42) or (60< pressure <105) or (140< pressure <180) or (0< pulse <35) or (110< pulse < 160):
    print("Вам срочно требуется врач")
else:
    print("Ошибка, при данных значениях вы не можете выжить")
