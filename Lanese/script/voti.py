from sys import argv

def read_file(filename):
    studenti = {}
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            parts = line.split()
            nome = parts[0]
            voti = [int(x) for x in parts[1:]]
            studenti[nome] = voti
    return studenti

def media_studente(studenti, nome):
    if nome not in studenti or len(studenti[nome]) == 0:
        return None
    voti = studenti[nome]
    return sum(voti)/len(voti)

def studenti_con_media_maggiore(studenti, soglia):
    res = []
    for nome, voti in studenti.items():
        if not voti:
            continue
        m = sum(voti)/len(voti)
        if m > soglia:
            res.append((nome, m))
    return res

def aggiungi_studente(studenti):
    nome = input("Nome studente: ").strip()
    if nome in studenti:
        print("Esiste gia'.")
        return
    voti_str = input("Voti separati da spazio (es: 28 30 27): ").split()
    voti = [int(x) for x in voti_str]
    studenti[nome] = voti
    print("Studente aggiunto.")

def salva(filename, studenti):
    with open(filename, "w") as f:
        for nome, voti in studenti.items():
            riga = nome + " " + " ".join(str(v) for v in voti) + "\n"
            f.write(riga)
    print("Dati salvati.")

def main():
    if len(argv) < 2:
        print("Uso: python voti.py voti.txt")
        return

    filename = argv[1]
    studenti = read_file(filename)

    while True:
        print("\n--- VOTI STUDENTI ---")
        print("1. Media di uno studente")
        print("2. Elenca studenti con media > soglia")
        print("3. Aggiungi nuovo studente")
        print("4. Salva file")
        print("5. Esci")
        scelta = input("Scelta: ").strip()

        if scelta == "1":
            nome = input("Nome: ").strip()
            m = media_studente(studenti, nome)
            if m is None:
                print("Studente non trovato o nessun voto.")
            else:
                print("Media di", nome, "=", m)

        elif scelta == "2":
            soglia = float(input("Soglia: "))
            res = studenti_con_media_maggiore(studenti, soglia)
            if not res:
                print("Nessuno supera la soglia.")
            else:
                for nome, m in res:
                    print(nome, "->", m)

        elif scelta == "3":
            aggiungi_studente(studenti)

        elif scelta == "4":
            salva(filename, studenti)

        elif scelta == "5":
            break

        else:
            print("Scelta non valida.")

if __name__ == "__main__":
    main()
