from ComboNumbers import ComboNumbers


def algo_demo():
    numbers_for_algo = [1, 3, 5, 7, 9, 10]
    for n in numbers_for_algo:
        tmp = ComboNumbers(n)
        with_odd = tmp.combo_with_odd()
        with_unique = tmp.combo_with_unique()
        print(f"Liczba: {tmp}")
        print(f"Liczby pierwsze: {tmp.odd_numbers}")
        print(f"Wszystkie liczby: {tmp.numbers}")
        print(f"Ilosc kombinacji dla liczb pierwszych: {len(with_odd)}")
        print(f"Ilosc kombinacji dla liczb pierwszych: {len(with_unique)}")
        print(f"Kombinajce dla liczb pierwszych: {with_odd}")
        print(f"Kombinacje dla liczb unikalnych: {with_unique}")
        print("-----------------------------------------------------------------------------------------------")


if __name__ == '__main__':
    #new_number = ComboNumbers(int(input("Podaj liczbe dla ktorych chcesz obliczyc kombinacje: ")))
    #print(new_number.combo_with_odd())
    #print(new_number.combo_with_unique())
    algo_demo()
