class Formater(object):
    def __init__(self):
        self.line_width = 0
        self.ret = []

    def parse_line(self, words):
        # print "-->",words
        line_str = ""
        one_line = []
        free_space = self.line_width
        while len(words) > 0 and len(words[0]) <= free_space:
            next_word = words.pop(0)
            free_space -= len(next_word) + 1
            one_line.append(next_word)
        if not one_line:
            return
        if len(one_line) == 1:
            line_str = one_line[0] + " " * free_space
        else:
            gap = free_space // (len(one_line) - 1)
            redent_gap = free_space - gap * (len(one_line) - 1)
            for i in range(len(one_line) - 1):
                line_str += one_line[i] + " "
                line_str += " " * gap
                if i <= redent_gap:
                    line_str += " "
            line_str += one_line[-1]
        self.ret.append(line_str)

    def input(self, line_width, raw_words):
        self.line_width = line_width
        words = raw_words.split(" ")
        # print words ,self.line_width
        while len(words) > 0:
            self.parse_line(words)

    def print_result(self):
        for r in self.ret:
            print r


class FormaterNew(Formater):
    def parse_line(self, words):
        free_space = self.line_width
        one_line = []
        while len(words) > 0 and len(words[0]) <= free_space:
            word = words.pop(0)
            one_line.append(word)
            free_space -= len(word) + 1

        gaps = [1 for i in one_line]

        if free_space == -1:
            gaps[-1] = 0
            # free_space= 0

        average_gap_sapce = free_space // len(gaps)

        redent_gap_space = free_space % len(gaps)
        line_str = ""
        for i in range(len(gaps)):
            line_str += one_line[i] + (gaps[i] + average_gap_sapce) * " "
            if i < redent_gap_space:
                line_str += " "

        self.ret.append(line_str)


# Ruby is a dynamic, open source programming language with a focus on simplicity and productivity. It has an elegant syntax that is natural to read and easy to write.

formater = FormaterNew()
formater.input(20,
               "Ruby is a dynamic, open source programming language with a focus on simplicity and productivity. It has an elegant syntax that is natural to read and easy to write.")
formater.print_result()


print  "------------"
formater = Formater()
formater.input(20,
               "Ruby is a dynamic, open source programming language with a focus on simplicity and productivity. It has an elegant syntax that is natural to read and easy to write.")
formater.print_result()