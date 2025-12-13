from sys import argv

import sys

# Costanti per il calcolo (NO LIBRERIE DATE)
DAYS_IN_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
DAYS_PER_YEAR = 365
REF_YEAR = 2000

# -----------------------------------------------------------
# 1. FUNZIONE DI ANALISI (analyze_date)
# Corrisponde alla tua funzione di analisi. Contiene la logica centrale.
# -----------------------------------------------------------

def _get_days_in_month(month):
    """Restituisce i giorni massimi per un mese (non bisestile)."""
    if 1 <= month <= 12:
        return DAYS_IN_MONTH[month]
    return 0

def analyze_date(date_str):
    """
    Analizza la data (dd/mm/yyyy), convalida il formato/range e calcola i giorni 
    trascorsi dal 01/01/2000, restituendo una stringa ('numero giorni' o 'Error').
    """
    # 1. Controllo formato rigoroso (dd/mm/yyyy)
    parts = date_str.strip().split('/')
    if len(parts) != 3:
        return "Error"
        
    d_str, m_str, y_str = parts
    
    # Rifiuta formati non rigorosi (es. "1/2/2001") o formati non corretti
    if len(d_str) != 2 or len(m_str) != 2 or len(y_str) != 4:
        return "Error"
    
    try:
        # Conversione in interi
        day = int(d_str)
        month = int(m_str)
        year = int(y_str)
    except ValueError:
        return "Error" # Cattura '0A/01/2001'

    # 2. Controllo Validità Semantica e Range
    # Data di riferimento: 01/01/2000
    if year < REF_YEAR or (year == REF_YEAR and month == 1 and day == 1) and (year == REF_YEAR and month < 1 and day < 1):
        # La data deve essere >= 01/01/2000
        if year < REF_YEAR:
             return "Error"
        if year == REF_YEAR and (month < 1 or (month == 1 and day < 1)):
             return "Error"
             
    if not (1 <= month <= 12):
        return "Error"
    
    max_days = _get_days_in_month(month)
    if not (1 <= day <= max_days):
        return "Error" # Cattura '32/01/2000'

    # 3. Calcolo giorni trascorsi
    
    # Anni completi trascorsi (dal 2000 al (anno - 1))
    days_from_years = (year - REF_YEAR) * DAYS_PER_YEAR
    
    # Mesi completi trascorsi nell'Anno corrente (fino al mese - 1)
    days_from_months = sum(DAYS_IN_MONTH[1:month])
    
    # Giorni nel Mese corrente (01/01/2000 = giorno 0)
    days_in_current_month = day - 1
    
    total_days = days_from_years + days_from_months + days_in_current_month
    
    return str(total_days)


# -----------------------------------------------------------
# 2. FUNZIONE DI LETTURA E SCRITTURA (read_process_write_dates)
# Corrisponde alla tua funzione di lettura/scrittura.
# -----------------------------------------------------------

def read_process_write_dates(input_filename, output_filename):
    """
    Gestisce l'I/O: legge il file di input, processa ogni riga con analyze_date
    e scrive i risultati nel file di output.
    """
    results = []
    
    try:
        # 1. Lettura
        with open(input_filename, 'r') as infile:
            input_lines = infile.readlines()
            
    except FileNotFoundError:
        print(f"Errore: File di input non trovato: {input_filename}")
        sys.exit(1)
        
    # 2. Processamento
    for line in input_lines:
        date_str = line.strip()
        if not date_str:
            continue
        
        output = analyze_date(date_str)
        results.append(output)

    # 3. Scrittura
    try:
        with open(output_filename, 'w') as outfile:
            for result in results:
                outfile.write(result + '\n')
        
    except IOError:
        print(f"Errore: Impossibile scrivere sul file di output: {output_filename}")
        sys.exit(1)


# -----------------------------------------------------------
# 3. FUNZIONE PRINCIPALE (main)
# Corrisponde alla tua funzione main/esecuzione.
# -----------------------------------------------------------

def main():
    """
    Controlla gli argomenti della linea di comando e avvia il processo.
    """
    if len(sys.argv) != 3:
        print("Uso: python nome_programma.py <file_input> <file_output>")
        sys.exit(1)
        
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    read_process_write_dates(input_file, output_file)
    print(f"Elaborazione completata. Risultati scritti in {output_file}")


if __name__ == '__main__':
    main()
