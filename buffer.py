# На языке Python написать минимум по 2 класса реализовывающих
# циклический буфер FIFO. Объяснить плюсы и минусы каждой реализации.


# Оценивается:
# 1. Полнота и качество реализации
# 2. Оформление кода
# 3. Наличие сравнения и пояснения по быстродействию


# Первый вариант реализации


# Быстродействие: Операция вставки и удаления элемента работает
# за O(1), так как манипуляция с индексами не требует реальных перемещений данных.

# Данная реализация больше подходит для случаев, когда требуется полный
# контроль над внутренними операциями и состоянием буфера. Этот вариант
# более гибкий, но сложнее в реализации. А так же в буфере всегда выделено
# фиксированное количество памяти, что может быть не совсем эффективно
# для некоторого рода задач.


class Buffer1:

    def __init__(self, size: int) -> None:
        if size <= 0:
            raise ValueError("Размер буфера должен быть целым положительным числом")
        self.cnt = 0
        self.head = 0
        self.cursor = 0
        self.size = size
        self.buffer = [None] * size

    def _check_empty(self) -> None:
        """
        Проверяет, пустой ли буфер

        Raises:
            Exception: если буфер пуст
        """
        if self.cnt == 0:
            raise Exception("Буфер пуст")

    def get_peek(self) -> int:
        """
        Возвращает первое значение из буфера

        Raises:
            Exception: если буфер пуст

        Returns:
            int: первое значение из буфера
        """
        self._check_empty()
        return self.buffer[self.head]

    def push_back(self, x: int) -> None:
        """
        Добавляет значение в буфер

        Args:
            x (int): значение для добавления в буфер

        Raises:
            Exception: если буфер заполнен
        """
        if self.cnt == self.size:
            self.head = (self.head + 1) % self.size
        else:
            self.cnt += 1

        self.buffer[self.cursor] = x
        self.cursor = (self.cursor + 1) % self.size

    def pop_front(self) -> int:
        """
        Возвращает первое значение из буфера и удаляет его

        Raises:
            Exception: если буфер пуст

        Returns:
            int: первое значение из буфера
        """
        self._check_empty()

        value = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) % self.size
        self.cnt -= 1
        return value

    def __repr__(self) -> str:
        if self.cnt == 0:
            return "Буфер пуст"
        return f"Текущее состояние буфера: {self.buffer}"


# Второй вариант реализации
from collections import deque


# Быстродействие: Операции вставки и удаления в deque выполняются
# за O(1) благодаря внутренней реализации двухсторонней очереди.


# Реализация на deque сама по себе проще, менее подвержена ошибкам и отлично
# подходит для ситуаций, где важна скорость и надежность. Она автоматически
# оптимизирует память.
class Buffer2:

    def __init__(self, size: int) -> None:
        if size <= 0:
            raise ValueError("Размер буфера должен быть целым положительным числом")
        self.buffer = deque(maxlen=size)

    def _check_empty(self) -> None:
        """
        Проверяет, пустой ли буфер

        Raises:
            Exception: если буфер пуст
        """
        if not self.buffer:
            raise Exception("Буфер пуст")

    def get_peek(self) -> int:
        """
        Возвращает первое значение из буфера

        Raises:
            Exception: если буфер пуст

        Returns:
            int: первое значение из буфера
        """
        self._check_empty()
        return self.buffer[0]

    def push_back(self, x: int) -> None:
        """
        Добавляет значение в буфер

        Args:
            x (int): значение для добавления в буфер
        """
        self.buffer.append(x)

    def pop_front(self) -> int:
        """
        Удаляет первое значение из буфера и возвращает его

        Raises:
            Exception: если буфер пуст

        Returns:
            int: первое значение из буфера
        """
        self._check_empty()
        return self.buffer.popleft()

    def __repr__(self) -> str:
        return (
            f"Текущее состояние буфера: {list(self.buffer)}"
            if self.buffer
            else "Буфер пуст"
        )
