def analyze_gps(gps_str):
    gps_str = gps_str.strip()
    # Esempio: 045°30'15"N (lunghezza totale 11 caratteri)
    if len(gps_str) != 11:
        return "Error"
    
    # Controllo simboli nelle posizioni corrette
    if gps_str[3] != '°' or gps_str[6] != "'" or gps_str[9] != '"':
        return "Error"
    
    try:
        # Estrazione e conversione
        deg = int(gps_str[0:3])
        minu = int(gps_str[4:6])
        sec = int(gps_str[7:9])
        cardinal = gps_str[10].upper()
        
        # Validazione range
        if not (0 <= deg <= 180): return "Error"
        if not (0 <= minu <= 59): return "Error"
        if not (0 <= sec <= 59): return "Error"
        if cardinal not in ['N', 'S', 'E', 'W']: return "Error"
        
        # Calcolo secondi totali
        total_seconds = (deg * 3600) + (minu * 60) + sec
        return str(total_seconds)
        
    except ValueError:
        return "Error"

print(analyze_gps("045°30'15" + '"' + "N")) # Output: 163815
