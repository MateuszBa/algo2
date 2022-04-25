from ComboNumbers import ComboNumbers


if __name__ == '__main__':
    new_number = ComboNumbers(int(input("Podaj liczbe dla ktorych chcesz obliczyc kombinacje: ")))
    print(new_number.combo_with_odd())
    print(new_number.combo_with_unique())
