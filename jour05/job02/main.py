p1 = int(input("Vôtre hauteur :"))
p2 = int(input("Vôtre largeur :"))


def draw_rectangle(width, height):
    firstlast_line = "-" * height
    center = " " * height
    i = 3
    print("|" + firstlast_line + "|")
    while i <= width:
        print("|" + center + "|")
        i += 1
    print("|" + firstlast_line + "|")


draw_rectangle(p1, p2)
