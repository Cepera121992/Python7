# Писал вмместе с наставником
from copy import deepcopy


class Matrix:
    def __init__(self, lst: list):
        self.data = deepcopy(lst)
        self.raw = [item for row in lst for item in row] if type(lst[0]) == list else self.data
        self.rows = len(lst)
        self.cols = len(self.raw) // self.rows
        if type(lst[0]) != list or len(self.raw) != self.rows * self.cols:
            raise Exception('Неккоретные данные')

    @property
    def shape(self):
        return self.rows, self.cols
    def reshape(self, shape):
        if len(shape) == 2 and shape[0] * shape[1] == len(self.raw):
            self.data = list(zip(*[iter(self.raw)] * shape[1]))
            self.rows, self.cols = shape
        else:
            raise Exception('Невозможно преобразовать матрицу')
    def __str__(self):
        return '\n'.join('\t'.join(str(item) for item in row) for row in self.data)

    def __add__(self, other):
        if type(self) == type(other) and self.shape == other.shape:
            new_matrix = self.__class__([[x + y, ] for x, y in zip(self.raw, other.raw)])
            new_matrix.reshape(self.shape)
            return new_matrix
        else:
            raise Exception('Сложение можно выполнять только между матрицами одинаковой размерности')




a = Matrix([[31, 22], [37, 43], [51, 86]])
b = Matrix([[3, 5], [2, 4], [-1, 64]])
print(a + b)