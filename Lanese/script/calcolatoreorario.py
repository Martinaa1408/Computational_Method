def analyze_time(time_str):
    # 1. Controllo formato (deve esserci il :)
    parts = time_str.strip().split(':')
    if len(parts) != 2:
        return "Error"
    
    h_str, m_str = parts
    
    # 2. Controllo lunghezza rigorosa (es. "1:30" è errore, serve "01:30")
    if len(h_str) != 2 or len(m_str) != 2:
        return "Error"
    
    try:
        hours = int(h_str)
        minutes = int(m_str)
        
        # 3. Controllo range semantico
        if not (0 <= hours <= 23) or not (0 <= minutes <= 59):
            return "Error"
            
        # 4. Calcolo totale minuti dalla mezzanotte
        total_minutes = (hours * 60) + minutes
        return str(total_minutes)
        
    except ValueError:
        return "Error"

# Test veloci
print(analyze_time("02:00"))  # Output: 120
print(analyze_time("1:30"))   # Output: Error
