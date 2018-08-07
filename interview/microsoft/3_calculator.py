inputs = "-1 * 2 / 3 + - 2--3+3.2234"


class Token:
    def __init__(self, type=None, text=None):
        self.type = type
        self.text = text


def is_number(s):
    return str(s) in "0123456789"


class Parser:
    def __init__(self):
        self.tokens = []
        self.inputs = ""
        self.index = 0

    def next_token(self):
        start_index = self.index
        if self.index >= len(self.inputs):
            return None
        if self.inputs[self.index] == " ":
            self.index += 1
            return None
        if self.inputs[self.index] == '-':
            self.index += 1
            if not is_number(self.inputs[self.index]):
                return Token('sign', '-')
        if self.inputs[self.index] == '+':
            self.index += 1
            return Token('sign', '+')
        if self.inputs[self.index] == '*':
            self.index += 1
            return Token('sign', '*')
        if self.inputs[self.index] == '/':
            self.index += 1
            return Token('sign', '/')

        while self.index < len(self.inputs) and is_number(self.inputs[self.index]):
            self.index += 1

        if self.index < len(self.inputs) and self.inputs[self.index] != ".":
            return Token("number", int(self.inputs[start_index:self.index]))
        else:
            self.index += 1

        while self.index < len(self.inputs) and is_number(self.inputs[self.index]):
            self.index += 1
            return Token("number", float(self.inputs[start_index:self.index]))

    def parse(self):
        self.inputs = inputs
        while self.index < len(self.inputs):
            t = self.next_token()
            if t:
                print(t.text)
                self.tokens.append(t)


p = Parser()
p.parse()
