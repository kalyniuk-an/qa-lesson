def normalize_name(name):
    return name.strip().title()


def count_letter(text, letter):
    return text.lower().count(letter.lower())


def triangle_area(base, height):
    return base * height / 2


name = input("Enter your name: ")
text = input("Enter any text: ")
letter = input("Which letter should we count? ")

base = float(input("Triangle base: "))
height = float(input("Triangle height: "))

print("\n--- Results ---")
print("Hello,", normalize_name(name))
print(f"Letter '{letter}' appears {count_letter(text, letter)} time(s).")
print(f"Triangle area: {triangle_area(base, height)}")