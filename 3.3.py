def contains_letter(text, letter):
    for char in text:
        if char == letter:
            return True

    return False


print(contains_letter("Python", "t"))