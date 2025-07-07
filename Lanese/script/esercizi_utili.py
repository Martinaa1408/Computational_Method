# Lista iniziale di parole
words = ["apple", "application", "apply", "banana", "band", "bandana"]
text = []  # Qui si memorizzano le parole scelte dall’utente

while True:
    print("Enter word or prefix (empty to exit):", end=' ')
    pre = input().strip().lower()  # Legge il prefisso/parola

    if pre == "":
        break  # Termina il programma

    # Verifica se è una parola esatta
    found = False
    i = 0
    while i < len(words):
        if words[i] == pre:
            found = True
        i = i + 1

    if found:
        print("Added:", pre)  # 🖨️ Esempio: se pre = "banana" → Added: banana
        text.append(pre)
    else:
        # Cerca suggerimenti
        suggestions = []
        i = 0
        while i < len(words):
            word = words[i]
            if len(pre) <= len(word):
                j = 0
                match = True
                while j < len(pre):
                    if pre[j] != word[j]:
                        match = False
                    j = j + 1
                if match:
                    suggestions.append(word)
            i = i + 1

        if len(suggestions) > 0:
            print("Suggestions:")
            i = 0
            while i < len(suggestions):
                print(str(i+1) + ". " + suggestions[i])
                # 🖨️ Esempio se pre = "app":
                # Suggestions:
                # 1. apple
                # 2. application
                # 3. apply
                i = i + 1

            print("Choose number, 'p'=propose, 'd'=discard:", end=' ')
            choice = input().strip().lower()

            if choice == 'd':
                print("Discarded.")  # 🖨️ Se scrivi d
                continue
            elif choice == 'p':
                if pre not in words:
                    words.append(pre)
                text.append(pre)
            else:
                is_number = True
                j = 0
                while j < len(choice):
                    if choice[j] < '0' or choice[j] > '9':
                        is_number = False
                    j = j + 1

                if is_number:
                    num = int(choice)
                    if num >= 1 and num <= len(suggestions):
                        selected = suggestions[num - 1]
                        print("Added:", selected)  # 🖨️ Esempio: Added: apple
                        text.append(selected)
                    else:
                        print("Invalid number.")
                else:
                    print("Invalid input.")
        else:
            # Nessuna parola inizia con quel prefisso
            print("No match. Add '" + pre + "'? (y/n):", end=' ')
            yn = input().strip().lower()
            if yn == 'y':
                words.append(pre)
                text.append(pre)
            else:
                print("Discarded.")

    print("Current text:", ' '.join(text))  # 🖨️ Mostra il testo costruito finora
    # Esempio: Current text: apple banana
#---------------------------------------------------------------------------------------------------------------------------
dictionary = ["cat", "catalog", "catch", "dog", "dot", "dove"]
selected = []

while True:
    print("Enter prefix (empty to exit):", end=' ')
    pre = input().strip().lower()

    if pre == "":
        break

    suggestions = []
    i = 0
    while i < len(dictionary):
        word = dictionary[i]
        if len(pre) <= len(word):
            j = 0
            ok = True
            while j < len(pre):
                if pre[j] != word[j]:
                    ok = False
                j = j + 1
            if ok:
                suggestions.append(word)
        i = i + 1

    if len(suggestions) > 0:
        print("Suggestions:")
        i = 0
        while i < len(suggestions):
            print(str(i+1) + ". " + suggestions[i])
            i = i + 1
        # 🖨️ Esempio: pre = "do" → 1. dog  2. dot  3. dove

        print("Choose number, 'p'=propose, 'd'=discard:", end=' ')
        choice = input().strip().lower()

        if choice == 'd':
            print("Discarded.")  # 🖨️ Se scarti il prefisso
        elif choice == 'p':
            if pre not in dictionary:
                dictionary.append(pre)
            selected.append(pre)
        else:
            ok = True
            j = 0
            while j < len(choice):
                if choice[j] < '0' or choice[j] > '9':
                    ok = False
                j = j + 1

            if ok:
                idx = int(choice)
                if idx >= 1 and idx <= len(suggestions):
                    selected.append(suggestions[idx - 1])
                    print("Added:", suggestions[idx - 1])
                    # 🖨️ Esempio: Added: dot
                else:
                    print("Invalid number.")
            else:
                print("Invalid input.")
    else:
        print("No match.")  # 🖨️ Nessun suggerimento

print("Selected:", ' '.join(selected))  # 🖨️ Esempio finale: Selected: dot dove
#-------------------------------------------------------------------------------------------------------------------------
# Lista predefinita di ingredienti
ingredienti = ["pane", "pasta", "passata", "parmigiano", "patate", "pollo"]
spesa = []

while True:
    print("Aggiungi ingrediente (vuoto per uscire):", end=' ')
    item = input().strip().lower()
    if item == "":
        break

    trovato = False
    i = 0
    while i < len(ingredienti):
        if item == ingredienti[i]:
            trovato = True
        i = i + 1

    if trovato:
        print("✔️ Aggiunto:", item)
        spesa.append(item)
    else:
        suggeriti = []
        i = 0
        while i < len(ingredienti):
            if len(item) <= len(ingredienti[i]):
                j = 0
                ok = True
                while j < len(item):
                    if item[j] != ingredienti[i][j]:
                        ok = False
                    j = j + 1
                if ok:
                    suggeriti.append(ingredienti[i])
            i = i + 1

        if len(suggeriti) > 0:
            print("Suggerimenti:")
            i = 0
            while i < len(suggeriti):
                print(str(i+1) + ". " + suggeriti[i])
                i = i + 1

            print("Scegli numero, 'p'=proponi nuova parola, 'd'=scarta:", end=' ')
            scelta = input().strip().lower()
            if scelta == 'd':
                print("Scartato.")
            elif scelta == 'p':
                spesa.append(item)
                ingredienti.append(item)
                print("➕ Aggiunto nuovo:", item)
            else:
                if scelta.isdigit():
                    num = int(scelta)
                    if num >= 1 and num <= len(suggeriti):
                        parola = suggeriti[num - 1]
                        spesa.append(parola)
                        print("✔️ Aggiunto:", parola)
                    else:
                        print("Numero non valido.")
                else:
                    print("Input non valido.")
        else:
            print("Nessuna corrispondenza. Vuoi aggiungerlo? (y/n):", end=' ')
            risposta = input().strip().lower()
            if risposta == 'y':
                spesa.append(item)
                ingredienti.append(item)
            else:
                print("Scartato.")

    print("Spesa attuale:", ' '.join(spesa))
#-------------------------------------------------------------------------------------------------------------------------
# Inizializzo un dizionario vuoto per memorizzare parole e definizioni
glossario = {}

# Loop principale
while True:
    print("Inserisci una parola da definire (vuoto per uscire):", end=' ')
    parola = input().strip().lower()

    if parola == "":
        break  # esce dal ciclo

    # Verifica se la parola è già presente nel dizionario
    if parola in glossario:
        print("⚠️ La parola esiste già!")
        print("Definizione attuale:", glossario[parola])
        print("Vuoi sovrascrivere? (y/n):", end=' ')
        risposta = input().strip().lower()
        if risposta != 'y':
            print("Ok, lasciata invariata.")
            continue  # salta il resto del ciclo

    # Verifica se esistono parole simili (stesso prefisso)
    suggeriti = []
    for altra in glossario:
        if altra.startswith(parola) and altra != parola:
            suggeriti.append(altra)

    if len(suggeriti) > 0:
        print("Attenzione: parole simili già presenti:")
        i = 0
        while i < len(suggeriti):
            print("- " + suggeriti[i])
            i = i + 1

    # Chiede la definizione all'utente
    print("Inserisci la definizione per '" + parola + "':", end=' ')
    definizione = input().strip()

    # Salva la nuova parola nel glossario
    glossario[parola] = definizione
    print("✅ Definizione salvata!")

    # Stampa il glossario aggiornato
    print("--- Glossario attuale ---")
    for chiave in glossario:
        print("* " + chiave + ":", glossario[chiave])
      
# .strip().lower() → per pulire spazi e normalizzare il testo
# if parola in glossario → per evitare duplicati o sovrascrivere senza conferma
# startswith() → per trovare parole simili già presenti
# glossario[chiave] = valore → per assegnare coppie nel dizionario
# for chiave in dizionario → per stampare tutte le definizioni
