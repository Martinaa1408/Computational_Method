from sys import argv

# Giorni per ciascun mese (anno NON bisestile)
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Apertura file di input e output tramite argv
fin = open(argv[1], 'r')
fout = open(argv[2], 'w')

# Leggiamo il file di input riga per riga
for line in fin:

    # Rimuoviamo il newline finale
    line = line.strip()

    try:
        # Separiamo la data nel formato dd/mm/yyyy
        parts = line.split('/')

        # Controllo formato base: devono esserci 3 campi
        if len(parts) != 3:
            result = 'Error'
        else:
            day_s, month_s, year_s = parts

            # Giorno e mese devono avere almeno 2 cifre
            if len(day_s) < 2 or len(month_s) < 2:
                result = 'Error'
            else:
                # Conversione in interi
                day = int(day_s)
                month = int(month_s)
                year = int(year_s)

                # Controlli di validità della data
                if (
                    year < 2000 or
                    month < 1 or month > 12 or
                    day < 1 or day > months[month - 1]
                ):
                    result = 'Error'
                else:
                    # Calcolo giorni trascorsi dal 01/01/2000
                    #
                    # - (year - 2000) * 365 → anni completi
                    # - sum(months[:month-1]) → mesi completi dell'anno corrente
                    # - (day - 1) → giorni del mese corrente
                    #
                    # Il 01/01/2000 deve dare 0
                    result = (
                        (year - 2000) * 365 +
                        sum(months[:month - 1]) +
                        (day - 1)
                    )

    except:
        # Qualsiasi errore (conversione, indice, ecc.)
        result = 'Error'

    # Scriviamo il risultato nel file di output
    fout.write(str(result) + '\n')

# Chiusura file
fin.close()
fout.close()
