def analyze_transaction(trans_str, current_balance):
    line = trans_str.strip()
    
    # 1. Controllo lunghezza (es. "+100" sono 4 caratteri)
    if len(line) != 4:
        return current_balance, "Skip"
    
    sign = line[0]
    value_str = line[1:]
    
    # 2. Controllo segno e se il resto è numerico
    if sign not in ['+', '-'] or not value_str.isdigit():
        return current_balance, "Skip"
    
    value = int(value_str)
    
    # 3. Aggiornamento saldo
    if sign == '+':
        new_balance = current_balance + value
    else:
        new_balance = current_balance - value
        
    return new_balance, "OK"

# Esempio di loop come in un esame
transazioni = ["+100", "-020", "+5", "+010"]
saldo = 0
for t in transazioni:
    saldo, status = analyze_transaction(t, saldo)
    if status == "OK":
        print(f"Transazione {t} elaborata. Saldo attuale: {saldo}")
    else:
        print(f"Transazione {t} ignorata (formato errato).")
