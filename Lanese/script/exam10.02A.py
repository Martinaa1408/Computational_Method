#EXERCISE A
#write a python program that takes from the user strings containing comma-separated integers. 
#The program takes a command line parameters an integer threshold and the name of a destination file to write teh results. For each line, the program prints on the destination file the number of pairs of integers in the line whose product is strictly greater than the threshold.
#sample execution:
#threshold: 18
#input:     #output file
#3,4,5      1
#4,4,23,1   3
#-3,8,1     0
from sys import argv

def count_pairs_above_threshold(numbers, threshold):
    count = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] * numbers[j] > threshold:
                count += 1
    return count

def pairs_integers():
    if len(sys.argv) != 3:
        print("Uso: python script.py output_file threshold")
        sys.exit(1)
    
    output_file = sys.argv[1]
    try:
        threshold = int(sys.argv[2])
    except ValueError:
        print("Errore: la soglia deve essere un numero intero.")
        sys.exit(1)
    
    try:
        writer = open(output_file, 'a')
        while True:
            line = input("Inserisci numeri separati da virgola (oppure premi invio per terminare): ").strip()
            if not line:
                break
            
            numbers = []
            elements = line.split(',')
            for num in elements:
                num = num.strip()
                try:
                    numbers.append(int(num))
                except ValueError:
                    print("Errore: Inserisci solo numeri separati da virgola.")
                    numbers = []  # Svuota la lista per non scrivere nulla
                    break
            
            if numbers:
                count = count_pairs_above_threshold(numbers, threshold)
                writer.write(str(count) + '\n')
                print("Coppie con prodotto sopra", threshold, ":", count)
        
        writer.close()
        print("Risultati aggiunti al file", output_file)
    
    except Exception as e:
        print("Errore durante l'elaborazione:", str(e))

pairs_integers()
