def find_closing_bracket(code, position):
    result = position
    counter = 1

    while counter > 0:
        result += 1
        c = code[result]

        if c == '[':
            counter += 1

        elif c == ']':
            counter -= 1
        
    return result

def find_opening_bracket(code, position):
    result = position
    counter = 1

    while counter > 0:
        result -= 1
        c = code[result]

        if c == ']':
            counter += 1

        elif c == '[':
            counter -= 1

    return result