import sys

def count_side(side):
    counts = {}

    for term in side.split("+"):
        term = term.strip().replace(" ", "")
        i = 0

        coef = ""
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

                counts[elem] = counts.get(elem, 0) + coef * num
            else:
                i += 1

    return counts


def check_reaction(line):
    left, right = line.split("->")
    left_counts = count_side(left)
    right_counts = count_side(right)

    balanced = left_counts == right_counts
    diffs = {}

    if not balanced:
        all_elems = set(left_counts) | set(right_counts)
        for e in all_elems:
            r = left_counts.get(e, 0)
            p = right_counts.get(e, 0)
            if r != p:
                diffs[e] = (r, p, r - p)

    return balanced, diffs


def main():
    if len(sys.argv) != 2:
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
            else:
                print("Status: unbalanced")
                print("Element Reactants Products Difference")
                for e in diffs:
                    r, p, d = diffs[e]
                    print(e, r, p, d)
            print()


if __name__ == "__main__":
    main()
