class vowels:
    vowel_chars = "eyuioa"

    def __init__(self, text):
        self.text = text
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.text):
            if self.text[self.index].lower() not in self.vowel_chars:
                self.index += 1
                continue
            value_to_return = self.text[self.index]
            self.index += 1
            return value_to_return

        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)


#s generator
def iter_with_gen(self):
    return (x for x in self.text if x.lower() in self.vowel_chars)

