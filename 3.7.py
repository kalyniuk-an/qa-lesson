def triangle_area(base, height):
    if base <= 0 or height <= 0:
        return None

    return base * height / 2


b = float(input("Base: "))
h = float(input("Height: "))

area = triangle_area(b, h)

if area is None:
    print("Invalid values.")
else:
    print(f"Area = {area}")