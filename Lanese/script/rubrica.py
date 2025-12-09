from sys import argv

def read_file(filename):
    rubrica = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            parts = line.split()
            nome = parts[0]
            numero = parts[1]
            rubrica.append((nome, numero))
    return rubrica

def cerca_prefisso(rubrica, pref):
    risultati = []
    for nome, numero in rubrica:
        if nome.startswith(pref):
            risultati.append((nome, numero))
    return risultati

def aggiungi_contatto(rubrica):
    nome = input("Nome: ").strip()
    numero = input("Numero: ").strip()
    for n, _ in rubrica:
        if n == nome:
            print("Errore: esiste gia' un contatto con questo nome.")
            return
    rubrica.append((nome, numero))
    print("Contatto aggiunto.")

def modifica_numero(rubrica):
    nome = input("Nome da modificare: ").strip()
    nuovo = input("Nuovo numero: ").strip()
    for i, (n, num) in enumerate(rubrica):
        if n == nome:
            rubrica[i] = (nome, nuovo)
            print("Numero aggiornato.")
            return
    print("Nessun contatto con questo nome.")

def salva(filename, rubrica):
    with open(filename, "w") as f:
        for nome, numero in rubrica:
            f.write(nome + " " + numero + "\n")
    print("Rubrica salvata su", filename)

def main():
    if len(argv) < 2:
        print("Uso: python rubrica.py rubrica.txt")
        return

    filename = argv[1]
    rubrica = read_file(filename)

    while True:
        print("\n--- RUBRICA ---")
        print("1. Cerca contatto per prefisso")
        print("2. Aggiungi nuovo contatto")
        print("3. Modifica numero")
        print("4. Salva su file")
        print("5. Esci")
        scelta = input("Scelta: ").strip()

        if scelta == "1":
            pref = input("Prefisso nome: ").strip()
            ris = cerca_prefisso(rubrica, pref)
            if not ris:
                print("Nessun contatto trovato.")
            else:
                for nome, numero in ris:
                    print(nome, "->", numero)

        elif scelta == "2":
            aggiungi_contatto(rubrica)

        elif scelta == "3":
            modifica_numero(rubrica)

        elif scelta == "4":
            salva(filename, rubrica)

        elif scelta == "5":
            break

        else:
            print("Scelta non valida.")

if __name__ == "__main__":
    main()
