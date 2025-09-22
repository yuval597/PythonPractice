x = "Hello"
y = "Bye"

def equalstrings (x,y):
    if x == y:
        return (f"{x} is equal to {y}")
    else:
        return (f"{y} is not {x}")

word = equalstrings (x,y)
print(word)