from sys import argv

# ============================================================
# 1) READ MODES
# ============================================================

def read_lines(filename):
    """Ritorna lista di righe non vuote (stringhe)."""
    lines = []
    try:
        with open(filename) as reader:
            for line in reader:
                line = line.strip()
                if line == "":
                    continue
                lines.append(line)
    except FileNotFoundError:
        print("warning")
        exit()
    return lines


def read_dict_3cols(filename):
    """
    File: CODE NAME SOMETHING
    -> dict[code] = (name, something)
    """
    data = {}
    try:
        with open(filename) as reader:
            for line in reader:
                line = line.strip()
                if line == "":
                    continue
                parts = line.split()
                if len(parts) < 3:
                    continue
                code = parts[0]
                name = parts[1]
                something = parts[2]
                data[code] = (name, something)
    except FileNotFoundError:
        print("warning")
        exit()
    return data


def read_products(filename):
    """
    File: CODE NAME PRICE
    -> dict[int] = (name:str, price:float)
    """
    products = {}
    try:
        with open(filename) as reader:
            for line in reader:
                line = line.strip()
                if line == "":
                    continue
                parts = line.split()
                if len(parts) < 3:
                    continue
                if not parts[0].isdigit():
                    continue
                code = int(parts[0])
                name = parts[1]
                try:
                    price = float(parts[2])
                except ValueError:
                    continue
                products[code] = (name, price)
    except FileNotFoundError:
        print("warning")
        exit()
    return products


def read_numbers_flat(filename):
    """Tutti i numeri (spazio-separati) in una lista unica."""
    numbers = []
    try:
        with open(filename) as reader:
            for line in reader:
                line = line.strip()
                if line == "":
                    continue
                parts = line.split()
                for p in parts:
                    if p.lstrip("-").isdigit():
                        numbers.append(int(p))
    except FileNotFoundError:
        print("warning")
        exit()
    return numbers


def read_rows_of_ints(filename):
    """Ogni riga -> lista di int; ritorna lista di liste."""
    rows = []
    try:
        with open(filename) as reader:
            for line in reader:
                line = line.strip()
                if line == "":
                    continue
                parts = line.split()
                row = []
                ok = True
                for p in parts:
                    if not p.lstrip("-").isdigit():
                        ok = False
                        break
                    row.append(int(p))
                if ok:
                    rows.append(row)
    except FileNotFoundError:
        print("warning")
        exit()
    return rows


def read_numbers_from_input_comma():
    """Numeri inseriti da utente separati da virgola."""
    line = input("insert numbers separated by comma: ").strip()
    numbers = []
    parts = line.split(",")
    for p in parts:
        p = p.strip()
        if p.lstrip("-").isdigit():
            numbers.append(int(p))
    return numbers


# ============================================================
# 2) WRITE MODES
# ============================================================

def write_one_value(filename, result):
    """Scrive un singolo risultato (stringa o numero)."""
    with open(filename, "w") as writer:
        writer.write(str(result) + "\n")


def write_list(filename, results):
    """Scrive una lista (una riga per elemento)."""
    with open(filename, "w") as writer:
        for r in results:
            writer.write(str(r) + "\n")


def write_csv(filename, rows, sep=","):
    """Scrive lista di liste/tuple come csv semplice."""
    with open(filename, "w") as writer:
        for row in rows:
            line = sep.join(str(x) for x in row)
            writer.write(line + "\n")


# ============================================================
# 3) LOGIC MATEMATICA (pattern esami)
# ============================================================

def sum_all(numbers):
    tot = 0
    for x in numbers:
        tot += x
    return tot


def sum_each_row(rows):
    """rows = lista di liste di int -> lista somme per riga."""
    out = []
    for row in rows:
        tot = 0
        for x in row:
            tot += x
        out.append(tot)
    return out


def count_above_threshold(numbers, threshold):
    c = 0
    for x in numbers:
        if x > threshold:
            c += 1
    return c


def min_value(numbers):
    if len(numbers) == 0:
        return None
    m = numbers[0]
    for x in numbers[1:]:
        if x < m:
            m = x
    return m


def max_value(numbers):
    if len(numbers) == 0:
        return None
    m = numbers[0]
    for x in numbers[1:]:
        if x > m:
            m = x
    return m


def eval_plus_minus(expr):
    """
    Valuta espressione intera con + e - (solo interi positivi nel testo).
    "34+12-2" -> 44
    """
    s = "".join(expr.strip().split())
    if s == "":
        return None

    tot = 0
    num = ""
    sign = 1

    for ch in s:
        if ch.isdigit():
            num += ch
        elif ch in "+-":
            if num == "":
                return None
            tot += sign * int(num)
            num = ""
            sign = 1 if ch == "+" else -1
        else:
            return None

    if num == "":
        return None
    tot += sign * int(num)
    return tot


def longest_contiguous_run(numbers, decreasing=False):
    """
    Longest strictly increasing contiguous run (default).
    If decreasing=True -> strictly decreasing.
    If tie, keeps the first (so update only if >).
    """
    if len(numbers) == 0:
        return []

    best = [numbers[0]]
    current = [numbers[0]]

    for i in range(1, len(numbers)):
        prev = numbers[i - 1]
        x = numbers[i]

        if not decreasing:
            ok = (x > prev)
        else:
            ok = (x < prev)

        if ok:
            current.append(x)
        else:
            if len(current) > len(best):
                best = current
            current = [x]

    if len(current) > len(best):
        best = current

    return best


# ============================================================
# 4) LOGIC SU STRUTTURE DATI (pattern esami)
# ============================================================

def freq_dict(items):
    """Conteggio occorrenze."""
    d = {}
    for x in items:
        d[x] = d.get(x, 0) + 1
    return d


def argmax_dict(d):
    """Ritorna la chiave con valore massimo."""
    best_k = None
    best_v = None
    for k, v in d.items():
        if best_k is None or v > best_v:
            best_k = k
            best_v = v
    return best_k


# ============================================================
# 5) INTERAZIONE UTENTE (menu) — daily activities / supermarket
# ============================================================

def overlaps(e_start, e_end, start, end):
    return start <= e_end and end >= e_start


def add_activity(activities):
    name = input("insert activity: ").strip()
    s_start = input("insert starting time (0-23): ").strip()
    s_end = input("insert ending time (1-24): ").strip()

    if not s_start.isdigit() or not s_end.isdigit():
        print("warning")
        return activities

    start = int(s_start)
    end = int(s_end)

    if start < 0 or start > 23 or end < 1 or end > 24 or start >= end:
        print("warning")
        return activities

    for act in activities:
        e_name, e_start, e_end = act
        if overlaps(e_start, e_end, start, end):
            print("warning: overlaps with", e_name)

    activities.append((name, start, end))
    return activities


def add_student(students):
    name = input("student name: ").strip()
    sid = input("student id: ").strip()

    if not sid.isdigit():
        print("warning")
        return students

    if sid in students:
        print("warning")
        return students

    students[sid] = name
    return students


def add_to_basket(products, basket):
    code_str = input("Enter product code (0 to stop): ").strip()
    if not code_str.isdigit():
        print("warning")
        return basket
    code = int(code_str)
    if code == 0:
        return basket
    if code not in products:
        print("warning")
        return basket
    basket[code] = basket.get(code, 0) + 1
    return basket


def print_bill(products, basket):
    total = 0
    for code in basket:
        qty = basket[code]
        name, price = products[code]
        subtotal = qty * price
        total += subtotal
        print(qty, "|", name, "|", subtotal)
    print("TOTAL =", total)


def run_menu_example():
    students = {}
    activities = []
    products = {101: ("Apple", 1.5), 330: ("Milk", 2.0)}
    basket = {}

    menu_str = (
        "\n1) add activity\n"
        "2) add student\n"
        "3) add to basket\n"
        "4) print bill\n"
        "5) exit\n"
    )

    while True:
        print(menu_str)
        choice = input("choice: ").strip()

        if choice == "1":
            activities = add_activity(activities)
        elif choice == "2":
            students = add_student(students)
        elif choice == "3":
            basket = add_to_basket(products, basket)
        elif choice == "4":
            print_bill(products, basket)
        elif choice == "5":
            break
        else:
            continue


# ============================================================
# 6) BATCH EXAMPLES (argv: file -> output on screen)
# ============================================================

def run_expressions_file(filename):
    lines = read_lines(filename)
    for expr in lines:
        val = eval_plus_minus(expr)
        if val is None:
            print(expr + "=ERROR")
        else:
            print(expr + "=" + str(val))


def run_longest_run_file(filename, decreasing=False):
    numbers = read_numbers_flat(filename)
    best = longest_contiguous_run(numbers, decreasing=decreasing)
    print(" ".join(str(x) for x in best))


# ============================================================
# 7) MAIN DISPATCH
# ============================================================

def main():
    # Qui scegli cosa lanciare a seconda dell’esame.
    # Esempi:
    # - run_expressions_file(filename)
    # - run_longest_run_file(filename, decreasing)
    # - run_menu_example()
    pass


if __name__ == "__main__":
    # esempio: longest run exam
    # python3 prog.py numbers
    # python3 prog.py -d numbers
    if len(argv) == 2:
        filename = argv[1]
        decreasing = False
        run_longest_run_file(filename, decreasing)
    elif len(argv) == 3 and argv[1] == "-d":
        filename = argv[2]
        decreasing = True
        run_longest_run_file(filename, decreasing)
    else:
        # oppure, per menu:
        # run_menu_example()
        exit()
