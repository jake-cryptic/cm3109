class Matrix:

    _data: list[list[int]]

    i: int
    j: int

    def __init__(self, i, j):
        self.i = i
        self.j = j
        self._data = []

        self.zeros()

    def zeros(self) -> None:
        for i in range(self.i):
            self._data.append([])
            for j in range(self.j):
                self._data[i].append([])
                self._data[i][j] = 0

    def write(self, i, j, val) -> None:
        print(self._data)
        print(self.i, self.j)
        print(i, j, val)
        self._data[i][j] = val

    def read(self, i, j) -> int:
        return self._data[i][j]

    def display(self):
        str_out = ''
        str_out2 = ''
        for i in range(self.i):
            str_out += f'{i}|\t'
            str_out2 += f'{i}|\t'
            for j in range(self.j):
                str_out2 += f'{self._data[i][j]}|\t'
            str_out2 += '\n'
        print(f'{str_out}\n{str_out2}')