

## 1) `len(argv)` + `open` con `try`

```python
from sys import argv, exit

if len(argv) != 2:
    print("usage: python3 script.py input.txt")
    exit(1)

try:
    f = open(argv[1], "r", encoding="utf-8")
except FileNotFoundError:
    print("file not found")
    exit(1)
```

---

## 2) File → righe → `strip()` → `split()` → lista di tuple

```python
items = []
for line in f:
    line = line.strip()
    if line == "":
        continue
    code, title = line.split(";", 1)
    items.append((code.strip(), title.strip()))
f.close()
```

---

## 3) `found` (esiste?) + `break`

```python
found = False
for x in L:
    if x == target:
        found = True
        break

if not found:
    print("not found")
```

---

## 4) “Trova e prendi il valore” (res = None)

```python
res = None
for (code, title) in items:
    if code == target:
        res = title
        break

if res is None:
    print("missing")
else:
    print(res)
```

---

## 5) Unpacking tuple in `for`

```python
students = [("123", "Mario"), ("456", "Anna")]
for sid, name in students:
    print(sid, name)
```

---

## 6) `while True` menu + `break` + `continue`

```python
while True:
    choice = input("1/2/3/4: ").strip()

    if choice == "4":
        break

    if choice not in ["1", "2", "3"]:
        print("invalid")
        continue

    print("ok:", choice)
```

---

## 7) `try/except` per `int(input())`

```python
try:
    n = int(input("number: ").strip())
except ValueError:
    print("not an int")
    n = None
```

---

## 8) Controllo range (es. voto 18–30)

```python
if not (18 <= grade <= 30):
    print("invalid grade")
    continue
```

---

## 9) Evitare duplicati in una lista di tuple (ID unico)

```python
ok = True
for sid, name in students:
    if sid == new_id:
        ok = False

if ok:
    students.append((new_id, new_name))
else:
    print("already exists")
```

---

## 10) Filtrare record per chiave (tutti gli esami di uno studente)

```python
# records = [(sid, code, grade, lode), ...]
for sid, code, grade, lode in records:
    if sid == target_id:
        print(code, grade, lode)
```

---

## 11) Media (somma + count) corretta

```python
somma = 0
count = 0

for x in values:
    somma += x
    count += 1

avg = 0.0
if count != 0:
    avg = somma / count

print(round(avg, 1))
```

---

## 12) Funzione utility (ritorna bool)

```python
def exists_student(students, sid):
    for i, name in students:
        if i == sid:
            return True
    return False
```

---

## 13) Funzione “get” (ritorna valore o None)

```python
def exam_title(exams, code):
    for c, title in exams:
        if c == code:
            return title
    return None
```

---

## 14) Funzione che aggiorna un contatore (ritorna il nuovo valore)

```python
def add_praise_if_needed(tot_praise, grade, ans):
    if grade == 30 and ans == "y":
        tot_praise += 1
    return tot_praise
```

No: **`found` non è un’alternativa al `while`**. Sono due cose diverse.

* `while` = *ripeti finché…* (menu, input finché valido, loop “interattivo”).
* `found` (boolean) = *ricordo se ho trovato qualcosa* mentre scorro una lista (di solito con `for`).

---

## 1) `found` vs `while`: quando uso cosa?

### Menu / input ripetuto → `while True`

```python
while True:
    choice = input("1-4: ").strip()
    if choice == "4":
        break
```

### Ricerca in una lista → `for` + `found` (+ spesso `break`)

```python
found = False
for x in L:
    if x == target:
        found = True
        break
if not found:
    print("not found")
```

Quindi: **`found` è un pattern dentro un ciclo (di solito `for`)**, non sostituisce i `while`.

---

## 2) Liste di tuple: unpacking vs indici (`collections[i][0]`)

Entrambi ok.

### Più chiaro (consigliato): unpacking

```python
for code, title in collections:
    print(code, title)
```

### Con indici (utile se ti serve l’indice)

```python
for i in range(len(collections)):
    code = collections[i][0]
    title = collections[i][1]
```

**Regola pratica:**

* se NON ti serve `i` → unpacking
* se ti serve confrontare “vicini” o aggiornare per indice → `range(len(...))`

---

## 3) Prefissi: `pre[:len(user)]` vs `startswith`

Quello che scrivi funziona, ma c’è un metodo più pulito.

### Metodo “manuale”

```python
if pre[:len(user)] == user:
    ...
```

### Metodo consigliato

```python
if pre.startswith(user):
    ...
```

**Perché meglio `startswith`:**

* è più leggibile
* evita errori se ti confondi con le lunghezze

---

## 4) “break indentato non dentro una condizione” che significa?

Il `break` **rompe il ciclo in cui si trova**.
Se lo metti “da solo” dentro il `for`, rompe **sempre al primo giro** (quasi sempre bug).

### Esempio BUG: break sempre

```python
for x in L:
    print(x)
    break   # esce subito: stampa solo il primo
```

### Esempio corretto: break SOLO se trovi

```python
for x in L:
    if x == target:
        found = True
        break
```

Quindi: `break` di solito sta **dentro `if`**, perché vuoi uscire **solo quando succede qualcosa**.

---

## 5) Dizionari migliori delle tuple per cercare?

Sì, per ricerca sono spesso migliori.

### Con lista di tuple (lento ma semplice)

```python
title = None
for code, t in exams:
    if code == wanted:
        title = t
        break
```

### Con dizionario (veloce e pulito)

```python
exams = {"B01": "Genetics", "B02": "Bioinformatics"}
if wanted in exams:
    title = exams[wanted]
```

**Regola:**

* se fai tante ricerche “per chiave” (ID/codice) → dict è perfetto
* se vuoi restare “semplice e lineare” → lista di tuple va bene

---

## 6) `try`, `if __name__ == "__main__"`, `len(argv)` — dove e quando?

### `len(argv)`

**Sempre all’inizio**, prima di usare `argv[1]`.

```python
if len(argv) != 2:
    exit(1)
```

### `try` per file

Subito dopo il controllo argv:

```python
try:
    f = open(argv[1])
except FileNotFoundError:
    exit(1)
```

### `try` per `int(input())`

Quando converti:

```python
try:
    grade = int(input())
except ValueError:
    continue
```

### `if __name__ == "__main__"`

Non è “solo con funzioni”, ma **ha senso soprattutto con funzioni**.

* Script piccolo inline: puoi anche non metterlo.
* Script con `main()` e funzioni: **mettilo**.

Pattern standard:

```python
def main():
    ...

if __name__ == "__main__":
    main()
```

---

## 7) “Per gli input non serve while?”

Dipende.

### Se l’utente deve inserire UNA volta sola → no while

```python
name = input("Name: ")
```

### Se devi ripetere finché l’input è valido → sì while

```python
while True:
    s = input("Grade: ")
    try:
        g = int(s)
    except ValueError:
        continue
    if 18 <= g <= 30:
        break
```

