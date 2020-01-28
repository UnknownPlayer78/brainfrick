from .memory import Memory
from .utils import find_closing_bracket, find_opening_bracket

DEBUG = False

class Interpreter:
    BRAINFUCK = ["+", "-", "<", ">", "[", "]", ",", "."]
    pointer = 0

    def __init__(self, file=""):
        self.file = file
        if file != "":
            self.read_file()
        else:
            self.code = input()

        self.memory = Memory()


    def read_file(self):
        f = open(self.file)
        self.code = f.read()
        f.close()

    def remove_comments(self):
        self.parsed_code = ""
        for char in self.code:
            if char in self.BRAINFUCK:
                self.parsed_code += char

    def get_input(self):
        user_input = input()
        value = ord(user_input)
        if value > 255:
            value = value % 255
        self.set_cell(value)

    def set_cell(self, value):
        self.memory.current.set(value)

    def get_cell(self):
        return self.memory.current.value

    def print_cell(self):
        value = self.memory.current.value
        char = chr(value)
        return char

    def left(self):
        self.memory.shift_left()

    def right(self):
        self.memory.shift_right()

    def plus(self):
        self.memory.current.add()

    def minus(self):
        self.memory.current.subtract()

    def step(self):
        char = self.parsed_code[self.pointer]

        if char == "+":
            self.plus()

        elif char == "-":
            self.minus()

        elif char == "<":
            self.left()

        elif char == ">":
            self.right()

        elif char == ".":
            print(self.print_cell(), end="", flush=True)

        elif char == ",":
            self.get_input()

        elif char == "[":
            if self.memory.current.value == 0:
                closing = find_closing_bracket(self.parsed_code, self.pointer)
                self.pointer = closing
            
        elif char == "]":
            if self.memory.current.value != 0:
                opening = find_opening_bracket(self.parsed_code, self.pointer)
                self.pointer = opening

        if DEBUG:
            print(self.pointer, "\t", char, "\t", self.memory.current.value)
        self.pointer += 1

    def run(self):
        self.remove_comments()

        while self.pointer != len(self.parsed_code):
            self.step()

        print()