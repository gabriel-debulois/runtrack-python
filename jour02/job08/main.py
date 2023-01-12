def typesaison(type,saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine et kiwi")
    if type == "fruits" and saison == "ete":
        print("poire, fraise, cassis")
    if type == "legume" and saison == "hiver":
        print("carotte, topinambour, endive")
    if type == "legume" and saison == "ete":
        print("artichaut, aubergine, navet")


typesaison("fruits", "hiver")
typesaison("fruits", "ete")
typesaison("legume", "hiver")
typesaison("legume", "ete")
