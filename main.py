import copy
import array
import time
from typing import List


class Wrestler:
    name: str = None
    weight: int = None
    age: int = None
    gender: str = None
    number_of_wins: int = 0
    number_of_defeats: int = 0
    score: int = 0
    fight_score: int = 0

    def __init__(self, name: str = None, weight: int = None, age: int = None, gender: str = None):
        self.name = name
        self.weight = weight
        self.age = age
        self.gender = gender

    def __str__(self):
        return self.name

    def check_correct(self) -> bool:
        check = True
        if self.name is None:
            print('Неверное имя участника')
            check = False
        if self.age is None:
            print('Неверный возвраст участника')
            check = False
        if self.weight is None:
            print('Неверный вес участника')
            check = False
        if not (self.gender == 'М' or self.gender == 'Ж'):
            print('Неверный пол участника')
            check = False
        return check


class Category(Wrestler):
    weight_low = None
    age_low = None
    wrestlers = []

    def __init__(self, name: str = None, weight: int = None, weight_low: int = None, age: int = None,
                 age_low: int = None, gender: str = None, replace_wrestlers: array = None):
        super().__init__(name, weight, age, gender)
        if replace_wrestlers is None:
            replace_wrestlers = [0]
        if replace_wrestlers is None:
            replace_wrestlers = [0]
        if replace_wrestlers is None:
            self.wrestlers = self.wrestlers.clear()
        self.weight_low = weight_low
        self.age_low = age_low

    def __str__(self):
        return self.name

    def check_for_matches(self, current_wrestler: Wrestler) -> bool:
        if current_wrestler.gender == self.gender and self.age_low <= current_wrestler.age <= self.age and \
                self.weight_low <= current_wrestler.weight <= self.weight:
            return True
        else:
            return False


class InputBlock:
    wrestlers = []
    categories = []

    def __init__(self):
        self.input_wrestlers()
        self.input_categories()

    def input_wrestlers(self):
        amount = int(input('Введите количество участников: '))
        i = 0

        while i < amount:
            wrestler = Wrestler()
            wrestler.name = input('Введите имя и фамилию участника: ')
            wrestler.weight = int(input('Введите вес участника: '))
            wrestler.age = int(input('Введите возраст участника: '))
            wrestler.gender = input('Введите пол участника: ')
            if wrestler.check_correct():
                self.wrestlers.append(copy.deepcopy(wrestler))
            i += 1

    def input_categories(self):
        non_category = Category(name='Вне категории')
        non_category.wrestlers = copy.deepcopy(self.wrestlers)
        self.categories.append(copy.copy(non_category))
        amount = int(input('Введите количество категорий'))
        i = 0
        while i < amount:
            category = Category()
            category.name = input('Введите название категории')
            category.weight = int(input('Введите максимальный вес в категории'))
            category.weight_low = int(input('Введите минимальный вес в категории'))
            category.age = int(input('Введите максимальный возраст в категории'))
            category.age_low = int(input('Введите минимальный возраст в категории'))
            category.gender = input('Введите пол категории')
            category.wrestlers = []
            j = 0
            while j < len(non_category.wrestlers):
                if category.check_for_matches(non_category.wrestlers[j]):
                    category.wrestlers.append(copy.deepcopy(non_category.wrestlers[j]))
                    non_category.wrestlers.pop(j)
                    j -= 1
                j += 1
            self.categories.append(copy.deepcopy(category))
            i += 1


class Fight:
    wrestler1: Wrestler = None
    wrestler2: Wrestler = None
    timer: int = None

    def __init__(self, wrestler1: Wrestler, wrestler2: Wrestler):
        self.wrestler1 = wrestler1
        self.wrestler2 = wrestler2
        self.wrestler1.fight_score = 0
        self.wrestler2.fight_score = 0

    def in_fight(self):
        while self.wrestler1.fight_score < 10 and self.wrestler2.fight_score < 10:
            print('add mark to ', self.wrestler1.name, ' press 1\n', 'add mark to ', self.wrestler2.name, ' press 2\n',
                  'your choice: ')
            choose = int(input())
            if choose == 1:
                print('Input mark: \n', 'Epon: 1\n', 'Vasare: 2\n', 'Your choice: ')
                choose = int(input())
                if choose == 1:
                    self.wrestler1.fight_score += 10
                elif choose == 2:
                    self.wrestler1.fight_score += 5
            elif choose == 2:
                print('Input mark: \n', 'Epon: 1\n', 'Vasare: 2\n', 'Your choice: ')
                choose = int(input())
                if choose == 1:
                    self.wrestler2.fight_score += 10
                elif choose == 2:
                    self.wrestler2.fight_score += 5

    def end_fight(self):
        self.wrestler1.score += self.wrestler1.fight_score
        self.wrestler2.score += self.wrestler2.fight_score
        if self.wrestler1.fight_score > self.wrestler2.fight_score:
            self.wrestler1.number_of_wins += 1
            self.wrestler2.number_of_defeats += 1
        elif self.wrestler1.fight_score < self.wrestler2.fight_score:
            self.wrestler2.number_of_wins += 1
            self.wrestler1.number_of_defeats += 1

    def make_fight(self):
        self.in_fight()
        self.end_fight()


class OlympicSystem:
    wrestlers: List[Wrestler] = None

    def __init__(self, wrestlers):
        self.wrestlers = wrestlers

    def find_next_fight_index(self):
        wins = []
        for i in range(len(self.wrestlers)):
            wins.append(self.wrestlers[i].number_of_wins)
        return max(wins)

    def make_new_score_category(self) -> List[Wrestler]:
        score_category = []
        win_value = self.find_next_fight_index()
        for i in range(len(self.wrestlers)):
            if self.wrestlers[i].number_of_wins == win_value:
                score_category.append(self.wrestlers[i])
        if len(score_category) > 1:
            return score_category
        return score_category

    def make_couples(self, score_category: List[Wrestler]) -> List[List[Wrestler]]:
        couples = []
        for i in range(0, len(score_category), 2):
            pass


competition = InputBlock()
result = Fight(competition.wrestlers[0], competition.wrestlers[1])
result.make_fight()
