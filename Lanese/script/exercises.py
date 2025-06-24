from sys import argv

def read_lines(filename):
    """Reads all lines of the file and returns a list of lists of integers."""
    try:
        file = open(filename, "r")
        lines = []
        for line in file:
            line = line.strip()
            parts = line.split()
            numbers = []
            for item in parts:
                numbers.append(int(item))  # conversione elemento per elemento
            lines.append(numbers)
        file.close()
        return lines
    except FileNotFoundError:
        print("Error: file not found.")
        exit(1)

def check_sum_pairs():
    """For each line, asks user input and checks if two elements sum up to that number."""
    if len(argv) != 2:
        print("Usage: python script.py inputfile")
        exit(1)

    lines = read_lines(argv[1])

    for line in lines:
        print("Line:", line)
        try:
            n = int(input("Enter a number: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        found = False
        for i in range(len(line)):
            for j in range(i + 1, len(line)):
                if line[i] + line[j] == n:
                    found = True
                    break  # esce dal ciclo interno
            if found:
                break  # esce anche dal ciclo esterno

        print(found)

# Avvia il programma
check_sum_pairs()


------------------------------------------------------------------------------------------------


from sys import argv  # Per leggere i parametri da riga di comando

def computation_sum(expr):
    """
    Data una stringa con + e - (es. "34+12-2"),
    calcola il risultato aritmetico.
    """
    numbers = "0123456789"
    operations = "+-"
    list_numbers = []         # Lista dei numeri estratti
    list_operations = []      # Lista dei simboli + o -
    temp = ""                 # Costruisce i numeri cifra per cifra

    for char in expr:
        if char in numbers:
            temp += char      # Accumula il numero
        elif char in operations:
            list_numbers.append(int(temp))     # Aggiunge il numero alla lista
            list_operations.append(char)       # Aggiunge l’operazione alla lista
            temp = ""         # Resetta per costruire il prossimo numero

    list_numbers.append(int(temp))  # Aggiunge l’ultimo numero rimasto

    result = list_numbers[0]        # Parte dal primo numero

    # Applica tutte le operazioni una alla volta
    for i in range(len(list_operations)):
        if list_operations[i] == "+":
            result += list_numbers[i + 1]
        elif list_operations[i] == "-":
            result -= list_numbers[i + 1]

    return result


def process_lines(source_file, output_file=None):
    """
    Legge ogni riga del file sorgente, calcola il risultato e
    lo scrive nel file di output oppure lo stampa.
    """
    for line in source_file:
        line = line.strip()  # Rimuove \n e spazi
        result = computation_sum(line)
        full_line = line + "=" + str(result)

        if output_file:
            output_file.write(full_line + "\n")
        else:
            print(full_line)


# MAIN PROGRAM
if __name__ == "__main__":
    if len(argv) == 3:
        # Due argomenti: input + output file
        with open(argv[1], "r") as source_file:
            with open(argv[2], "w") as output_file:
                process_lines(source_file, output_file)

    elif len(argv) == 2:
        # Solo input file → stampa sullo schermo
        with open(argv[1], "r") as source_file:
            process_lines(source_file)

    else:
        print("Usage: python script.py input_file [output_file]")
