import itertools


class ComboNumbers:
    def __init__(self, maximum):
        self.maximum = maximum
        self.odd_numbers = self.find_all_odd_numbers(self.maximum)
        self.numbers = self.all_number(self.maximum)

    @staticmethod
    def find_all_odd_numbers(maximum: int) -> list:
        odd_numbers = []
        for i in range(1, maximum + 1):
            if i % 2 != 0:
                odd_numbers.append(i)
        return odd_numbers

    @staticmethod
    def all_number(maximum: int) -> list:
        return [i for i in range(1, maximum + 1)]

    def combo_with_odd(self) -> list:
        combos = []
        for i in range(1, self.maximum+1):
            res = list(sorted(el) for el in itertools.combinations_with_replacement(self.odd_numbers, i)
                       if sum(el) == self.maximum)
            if res:
                for r in res:
                    combos.append(r)
        return combos

    def combo_with_unique(self) -> list:
        combos = []
        for i in range(1, self.maximum+1):
            res = list(sorted(el) for el in itertools.combinations(self.numbers, i)
                       if sum(el) == self.maximum)
            if res:
                for r in res:
                    combos.append(r)
        return combos
