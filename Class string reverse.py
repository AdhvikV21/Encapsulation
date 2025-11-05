class reverse:
    def __init__(self, s=""):
        self.s = s

    def get_reversed_string(self):
        return self.s[::-1]

user_input = input("Enter a sentence: ")
reverse = reverse(user_input)
print(f"Reversed sentence: {reverse.get_reversed_string()}")