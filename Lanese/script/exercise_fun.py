'''
Write a python program that takes a source file containing in each line an arithmetic integer
expression with only sums and subtractions, and computes the results. The name of the
source file is taken as command line parameter. If there is an additional command line
parameter then this is the name of the file where the results will be written, otherwise the
results are printed on the screen.
Input
34+12-2
10-23+1
100+3+12+2
2
Output
34+12-2=44
10-23+1=-12
100+3+12+2=117
2=2   '''

from sys import argv


def read_file(filename):
    """Legge le righe del file pulendole dagli spazi."""
    lines = []
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if line != "":
                    lines.append(line)
    except FileNotFoundError:
        print(f"Error: file '{filename}' not found")
        exit()
    return lines


def write_file(filename, results):
    """Scrive i risultati in un file di output."""
    with open(filename, "w") as f:
        for line in results:
            f.write(line + "\n")


def main():
    # argv è ora visibile perché importato globalmente
    lines = read_file(argv[1])
    results = []

    for expr in lines:
        total = 0
        num_str = ""
        op = "+"  # Operatore corrente (applica il numero precedente)

        # Iteriamo sui caratteri dell'espressione
        for ch in expr:
            if ch.isdigit():
                num_str += ch
            elif ch in "+-":
                # Quando trovo un segno, elaboro il numero accumulato finora
                if num_str != "":
                    if op == "+":
                        total += int(num_str)
                    else:
                        total -= int(num_str)

                # Il segno corrente diventa l'operatore per il PROSSIMO numero
                op = ch
                num_str = ""
            # Ignoriamo eventuali spazi o altri caratteri

        # Elaborazione dell'ultimo numero accumulato dopo la fine del ciclo
        if num_str != "":
            if op == "+":
                total += int(num_str)
            else:
                total -= int(num_str)

        results.append(f"{expr}={total}")

    return results


if __name__ == "__main__":
    # Controllo argomenti
    if len(argv) < 2 or len(argv) > 3:
        print("Usage: python3 calculator.py source.txt [output.txt]")
        exit()

    processed_results = main()

    # Se c'è il terzo argomento, scrivi su file, altrimenti stampa
    if len(argv) == 3:
        write_file(argv[2], processed_results)
    else:
        for res in processed_results:
            print(res)
