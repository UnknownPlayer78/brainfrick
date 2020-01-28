class Memory:
    def __init__(self):
        self.memory = []
        self.pointer = self.Pointer()
        self.update_current()

    def update_current(self):
        self.current = self.cell(self.pointer.position)

    def shift_left(self):
        self.pointer.position -= 1
        self.update_current()

    def shift_right(self):
        self.pointer.position += 1
        self.update_current()
        
    def cell(self, position):
        for c in self.memory:
            if c.position == position:
                return c
        
        self.new_cell(position)
        return self.cell(self.pointer.position)

    def new_cell(self, position):
        cell = self.Cell(position)
        self.memory.append(cell)

    class Cell:
        value = 0

        def __init__(self, position=0):
            self.position = position

        def add(self):
            self.value += 1
            if self.value > 255:
                self.value = 0

        def subtract(self):
            self.value -= 1
            if self.value < 0:
                self.value = 255

        def set(self, value):
            self.value = value

    class Pointer:
        position = 0