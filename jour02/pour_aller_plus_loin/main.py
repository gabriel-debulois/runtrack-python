def triangle(p1, p2, p3):
    if p1 == p2 and p1 == p3:
        print("équilatéral")
    if p1 == p2 and p1 != p3 or p1 == p3 and p1 != p2:
        print("isocèle")
    if p1 == p2 / p3:
        print("rectangle")


triangle(10, 10, 10)
triangle(10, 10, 15)
triangle(10, 20, 20)
