class Cell:
    def __init__(self, num_cells):
        self.num_cells = int(num_cells)
    def __add__(self, second_cell):
        return Cell(self.num_cells + second_cell.num_cells)
    # def __str__(self):
    #     return '*' * self.num_cells
    def __sub__(self, second_cell):
        return Cell(int(self.num_cells - second_cell.num_cells) if self.num_cells > second_cell.num_cells else print('Вычетание невозможно!'))
    def __mul__(self, second_cell):
        return Cell(self.num_cells * second_cell.num_cells)
    def __truediv__(self, second_cell):
        return Cell(self.num_cells / second_cell.num_cells)
    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.num_cells / cells_in_row)):
            row += f'{"*" * cells_in_row}\\n'
        row += f'{"*" * (self.num_cells % cells_in_row)}'
        return row
# #     или
#     def make_order(self, cells_in_row):
#         str_obj = self.__str__()
#         count = int(len(str_obj)) // cells_in_row
#         ost_count = int(len(str_obj)) % cells_in_row
#         str_2 = f'{str_obj[:cells_in_row]}\\n' * count
#         return f'{str_2}{"*"*ost_count}'


my_cell = Cell(12)
print(my_cell.make_order(5))






