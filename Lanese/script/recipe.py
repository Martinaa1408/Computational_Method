from sys import argv, exit

# ============================================================
# LETTURA FILE (ADERENTE AGLI ESAMI)
# ============================================================

def read_numbers_per_line(f):
    """
    File con numeri interi separati da spazi.
    Ritorna: list[list[int]]
    """
    rows = []
    for line in f:
        line = line.strip()
        if line == "":
            continue
        rows.append([int(x) for x in line.split()])
    return rows


def read_words(f):
    """
    File con una parola per riga.
    Ritorna: list[str]
    """
    words = []
    for line in f:
        w = line.strip()
        if w != "":
            words.append(w)
    return words


def read_key_value(f):
    """
    File con righe 'key value'.
    Ritorna: dict[key] = value
    """
    d = {}
    for line in f:
        parts = line.strip().split()
        if len(parts) >= 2:
            key = parts[0]
            value = " ".join(parts[1:])
            d[key] = value
    return d


# ============================================================
# LOGICA ESAME — SCEGLI UN CASO (UNO SOLO ALLA VOLTA)
# ============================================================

def solve_numbers(rows):
    """
    rows: list[list[int]]
    CASI TIPICI SU NUMERI
    """
    output = []

    for nums in rows:

        # -------------------------------
        # CASO A — ESISTE? (boolean)
        # two-sum / proprietà su coppie
        # -------------------------------
        # n = int(input("Insert n: "))
        # found = False
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == n:
        #             found = True
        #             break
        #     if found:
        #         break
        # output.append(found)

        # -------------------------------
        # CASO B — TUTTI? (boolean)
        # -------------------------------
        # k = int(input("Insert k: "))
        # ok = True
        # for x in nums:
        #     if x % k != 0:
        #         ok = False
        #         break
        # output.append(ok)

        # -------------------------------
        # CASO C — CONTA
        # -------------------------------
        # t = int(input("Insert threshold: "))
        # count = 0
        # for x in nums:
        #     if x > t:
        #         count += 1
        # output.append(count)

        # -------------------------------
        # CASO D — MAX / MIN
        # -------------------------------
        # if len(nums) == 0:
        #     output.append(None)
        # else:
        #     best = nums[0]
        #     for x in nums[1:]:
        #         if x > best:   # cambia > / < per max/min
        #             best = x
        #     output.append(best)

        # -------------------------------
        # CASO E — CONSECUTIVI (finestra)
        # -------------------------------
        # k = int(input("Insert k: "))
        # found = False
        # for i in range(len(nums) - 2):   # finestra di 3
        #     if nums[i] < k and nums[i+1] == k and nums[i+2] > k:
        #         found = True
        #         break
        # output.append(found)

        pass  # ← attiva UNO dei casi sopra

    return output


def solve_spellchecker(text_words, dict_words):
    """
    CASO RESTART CHECK (spellchecker)
    """
    output = []

    for w in text_words:
        current = w

        while True:
            if current in dict_words:
                output.append(current)
                break

            ans = input(f'Is "{current}" correct? (y/n): ').strip().lower()
            if ans == 'y':
                dict_words.append(current)   # valido da ora in poi
                output.append(current)
                break
            else:
                current = input("Insert correct word: ").strip()

    return output


def interactive_session():
    """
    CASO SESSIONE INTERATTIVA CON SENTINELLA
    """
    log = []
    while True:
        s = input("Enter value (empty to exit): ").strip()
        if s == "":
            break
        log.append(s)
    return log


# ============================================================
# BLOCCO DELLE CLASSI — AVVIO UNICO
# ============================================================

if __name__ == "__main__":

    # --------------------------------------------------------
    # CONFIGURAZIONE ESAME (modifica SOLO qui)
    # --------------------------------------------------------
    MODE = "numbers"       # "numbers" | "spellcheck" | "interactive"
    # --------------------------------------------------------

    try:
        if MODE == "numbers":
            if len(argv) != 3:
                print("Usage: python script.py input.txt output.txt")
                exit(1)

            f_in = open(argv[1], "r")
            f_out = open(argv[2], "w")

            rows = read_numbers_per_line(f_in)
            f_in.close()

            result = solve_numbers(rows)

            for x in result:
                f_out.write(str(x) + "\n")

            f_out.close()

        elif MODE == "spellcheck":
            if len(argv) != 4:
                print("Usage: python script.py text.txt dict.txt output.txt")
                exit(1)

            f_text = open(argv[1], "r")
            f_dict = open(argv[2], "r")
            f_out = open(argv[3], "w")

            text_words = read_words(f_text)
            dict_words = read_words(f_dict)

            f_text.close()
            f_dict.close()

            result = solve_spellchecker(text_words, dict_words)

            for w in result:
                f_out.write(w + "\n")

            f_out.close()

        elif MODE == "interactive":
            log = interactive_session()
            for x in log:
                print(x)

        else:
            print("Unknown MODE")
            exit(1)

    except FileNotFoundError:
        print("Error: file not found")
        exit(1)

    except ValueError:
        print("Error: invalid integer in input")
        exit(1)
