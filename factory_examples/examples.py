"""
Модуль генерации заданий на математические операции с 2 или 3 числами:
- сложение и вычитание без скобок и со скобками,
- умножение в пределах таблицы умножения,
- деление чисел,
- сложение и вычитание с умножением и делением без скобок и со скобками.
Результат вычисления для всех сгенерированных заданий не превышает 100.
"""

import random


class Example:
    """
    Родительский класс для инициирования ограничения limit и произвольных чисел.
    Наследуется дочерними классами, генерирующими задания.
    """

    def __init__(self, limit) -> None:
        """limit: число-ограничение (в пределах этого числа будут числа в примерах)
        Например, limit=20 -> числа в примерах будут НЕ более 20.
        Результаты вычисления примеров - в пределах 100.
        """
        self.limit = limit  # число-ограничение

    def get_nums(self):
        """Метод возвращает три рандомных числа в пределах ограничения limit."""
        x = random.randint(1, self.limit)
        y = random.randint(1, self.limit)
        z = random.randint(1, self.limit)
        return x, y, z


class Addsub(Example):
    """
    Дочерний класс для генерации заданий на сложение/вычитание
    2 или 3 чисел со скобками и без.
    """

    def __init__(self, limit) -> None:
        super().__init__(limit)

    def add_2args_wb(self):
        """Сложение ДВУХ чисел с результатом не более 100."""
        while True:
            x, y, z = self.get_nums()
            if x + y > 100:
                continue
            return f"{x} + {y} ="

    def sub_2args_wb(self):
        """Вычитание ДВУХ чисел с результатом больше нуля."""
        while True:
            x, y, z = self.get_nums()
            if x - y < 0:
                continue
            return f"{x} - {y} ="

    def add_3args_wb(self):
        """Сложение ТРЕХ чисел без скобок с результатом не более 100."""
        while True:
            x, y, z = self.get_nums()
            if x + y + z > 100:
                continue
            return f"{x} + {y} + {z} ="

    def sub_3args_wb(self):
        """Вычитание ТРЕХ чисел без скобок с результатом больше нуля."""
        while True:
            x, y, z = self.get_nums()
            if x - y - z < 0:
                continue
            return f"{x} - {y} - {z} ="

    def addsub_3args_wb(self):
        """Сложение и вычитание ТРЕХ чисел без скобок с результатом не более 100."""
        while True:
            x, y, z = self.get_nums()
            if x - y >= 0 and x - y + z <= 100:
                return f"{x} - {y} + {z} ="
            elif x + y > 100 or x + y - z < 0:
                continue
            return f"{x} + {y} - {z} ="

    def addsub_3args(self):
        """Сложение и вычитание ТРЕХ чисел со скобками с результатом не более 100."""
        while True:
            x, y, z = self.get_nums()
            if 0 <= x - (y + z) <= 100:
                return f"{x} - ({y} + {z}) ="
            if y - z > 0 and x - (y - z) > 0:
                return f"{x} - ({y} - {z}) ="
            elif y - z < 0 or x + (y - z) > 100:
                continue
            return f"{x} + ({y} - {z}) ="


class Muldiv:
    """Класс для генерации заданий на умножение/деление в пределах 100."""

    def mul_2args_wb(self):
        """Умножение в пределах таблицы умножения (в пределах 100)."""
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        return f"{x} · {y} ="

    def div_2args_wb(self):
        """Деление в пределах 100."""
        while True:
            x = random.randint(1, 100)
            y = random.randint(1, 100)
            if x % y != 0:
                continue
            return f"{x} ∶ {y} ="


class Mix(Example):
    """
    Дочерний класс для генерации заданий на умножение/деление
    со сложением и вычитанием со скобками и без.
    """

    def __init__(self, limit) -> None:
        super().__init__(limit)

    def mul_mix_wb(self):
        """Умножение со сложением и вычитанием без скобок."""
        while True:
            a = random.randint(1, 10)
            x, y, z = self.get_nums()
            if a * y + z <= 100:
                return f"{a} · {y} + {z} ="
            elif y - z * a < 0:
                continue
            return f"{y} - {z} · {a} ="

    def div_mix_wb(self):
        """Деление со сложением и вычитанием без скобок."""
        while True:
            a = random.randint(1, 10)
            x, y, z = self.get_nums()
            if y % a != 0:
                continue
            if x + int(y / a) <= 100:
                return f"{x} + {y} ∶ {a} ="
            elif x - int(y / a) < 0:
                continue
            return f"{x} - {y} ∶ {a} ="

    def mul_mix(self):
        """Умножение со сложением и вычитанием со скобками."""
        while True:
            a = random.randint(1, 10)
            x, y, z = self.get_nums()
            if a * (y + z) <= 100:
                return f"{a} · ({y} + {z}) ="
            elif y - z < 0 or (y - z) * a > 100:
                continue
            return f"({y} - {z}) · {a} ="

    def div_mix(self):
        """Деление со сложением и вычитанием со скобками."""
        while True:
            a = random.randint(1, 10)
            x, y, z = self.get_nums()
            if a % (y + z) == 0:
                return f"{a} ∶ ({y} + {z}) ="
            elif y - z < 0 or (y - z) % a != 0:
                continue
            return f"({y} - {z}) ∶ {a} ="
