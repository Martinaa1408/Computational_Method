from sys import argv

# -----------------------------------------------------
# 1. LETTURA FILE
# -----------------------------------------------------
def read_file(filename):
    ricette = []
    f = open(filename, "r")
    for line in f:
        line = line.strip()
        if line == "":
            continue
        parts = line.split()
        nome = parts[0]
        ingredienti = parts[1:]
        ricette.append((nome, ingredienti))
    f.close()
    return ricette


# -----------------------------------------------------
# 2. CERCA RICETTE CHE CONTENGONO UN INGREDIENTE
# -----------------------------------------------------
def cerca_ingrediente(ricette, ingr):
    risultati = []
    for nome, ingredienti in ricette:
        if ingr in ingredienti:
            risultati.append(nome)
    return risultati


# -----------------------------------------------------
# 3. CERCA RICETTE CHE CONTENGONO TUTTI GLI INGREDIENTI
# -----------------------------------------------------
def cerca_tutti(ricette, lista_ingredienti):
    risultati = []
    for nome, ingredienti in ricette:
        ok = True
        for x in lista_ingredienti:
            if x not in ingredienti:
                ok = False
                break
        if ok:
            risultati.append(nome)
    return risultati


# -----------------------------------------------------
# 4. AGGIUNGI NUOVA RICETTA
# -----------------------------------------------------
def aggiungi(ricette):
    nome = input("Nome ricetta: ")
    ingredienti = input("Ingredienti separati da spazi: ").split()

    # controllo se esiste
    for r, _ in ricette:
        if r == nome:
            print("Esiste già!")
            return

    ricette.append((nome, ingredienti))
    print("Aggiunta.")


# -----------------------------------------------------
# 5. SALVA SU FILE
# -----------------------------------------------------
def salva(filename, ricette):
    f = open(filename, "w")
    for nome, ingredienti in ricette:
        f.write(nome + " " + " ".join(ingredienti) + "\n")
    f.close()
    print("Salvato.")


# -----------------------------------------------------
# MAIN
# -----------------------------------------------------
def main():
    if len(argv) < 2:
        print("Uso: python file.py ricette.txt")
        return

    ricette = read_file(argv[1])

    while True:
        print()
        print("1. Cerca ricette che contengono un ingrediente")
        print("2. Cerca ricette che contengono tutti gli ingredienti dati")
        print("3. Aggiungi nuova ricetta")
        print("4. Salva su file")
        print("5. Esci")
        print()

        scelta = input("Scelta: ")

        if scelta == "1":
            ingr = input("Ingrediente: ")
            ris = cerca_ingrediente(ricette, ingr)
            print("Risultati:", ris)

        elif scelta == "2":
            lista_ingr = input("Ingredienti separati da spazio: ").split()
            ris = cerca_tutti(ricette, lista_ingr)
            print("Risultati:", ris)

        elif scelta == "3":
            aggiungi(ricette)

        elif scelta == "4":
            salva(argv[1], ricette)

        elif scelta == "5":
            break

        else:
            print("Opzione non valida.")

main()
