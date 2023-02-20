# python3, Roberts Kārlis Kaudze, 221RDB216

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i + 1))

            pass

        if next in ")]}":
            if len(opening_brackets_stack) == 0:
                return i + 1

            augsa = opening_brackets_stack.pop()
            if not are_matching(augsa.char, next):
                return i + 1
                
    if len(opening_brackets_stack) > 0:
        return opening_brackets_stack[0].position
        
    else:
        return "Success"

def main():
    firstText = input()
    if firstText == "I":

        text = input()
        mismatch = find_mismatch(text)
        print(mismatch)

    elif firstText == "F":
        filename = input()
        text = open(filename)
        mismatch = find_mismatch(text)
        print(mismatch)


if __name__ == "__main__":
    main()
