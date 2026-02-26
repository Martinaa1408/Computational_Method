import sys

def count_side(side):
    elems = []
    counts = []

    for term in side.split("+"):
        term = term.strip()
        coef = ""
        i = 0

        while i < len(term) and term[i].isdigit():
            coef += term[i]
            i += 1
        coef = int(coef) if coef else 1
        formula = term[i:]

        i = 0
        while i < len(formula):
            if formula[i].isupper():
                elem = formula[i]
                i += 1
                if i < len(formula) and formula[i].islower():
                    elem += formula[i]
                    i += 1

                num = ""
                while i < len(formula) and formula[i].isdigit():
                    num += formula[i]
                    i += 1
                num = int(num) if num else 1

                total = coef * num

                if elem in elems:
                    counts[elems.index(elem)] += total
                else:
                    elems.append(elem)
                    counts.append(total)
            else:
                i += 1

    return elems, counts


def check_reaction(line):
    left, right = line.split("->")
    e1, c1 = count_side(left)
    e2, c2 = count_side(right)

    all_elems = sorted(set(e1 + e2))
    balanced = True
    diffs = []

    for e in all_elems:
        r = c1[e1.index(e)] if e in e1 else 0
        p = c2[e2.index(e)] if e in e2 else 0

        if r != p:
            balanced = False
            diffs.append((e, r, p, r - p))

    return balanced, diffs


def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py reactions.txt")
        return

    filename = sys.argv[1]

    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            print("Reaction:", line)

            balanced, diffs = check_reaction(line)

            if balanced:
                print("Status: balanced")
                print()
            else:
                print("Status: unbalanced")
                print("Element Reactants Products Difference")
                for d in diffs:
                    print(d[0], d[1], d[2], d[3])
                print()


if __name__ == "__main__":
    main()