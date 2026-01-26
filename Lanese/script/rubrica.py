from sys import argv

# 1) LETTURA FILE
input_file = open(argv[1], 'r')
rubric = []

for line in input_file:
    parts = line.strip().lower().split()
    if parts != []:
        name = parts[0]
        number = parts[1]          # lascialo stringa (meglio di int)
        rubric.append((name, number))

input_file.close()

current_text = []

while True:
    user = input('Enter name or prefix (empty to exit): ').strip().lower()
    if user == '':
        print('Bye bye')
        break

    # CASE A: exact name exists
    found = False
    for (name, number) in rubric:
        if user == name:
            print('Found:', name, number)
            current_text.append(name)
            found = True
            break

    if found:
        print('Current Searches:', " ".join(current_text))
        continue

    # CASE B: prefix suggestions
    suggestions = []
    for (name, number) in rubric:
        if name[:len(user)] == user:
            suggestions.append((name, number))

    if len(suggestions) > 0:
        print('Suggestions:')
        for i in range(len(suggestions)):
            print(str(i+1) + ".", suggestions[i][0], suggestions[i][1])  # nome e numero stessa riga

        choice = input("Choose a suggestion (number), or 'p' for the proposed name, or 'd' to discard: ").strip().lower()

        if choice == 'd':
            print('Discarded.')

        elif choice == 'p':
            # add the prefix as a new contact with UNKNOWN
            current_text.append(user)
            print('Added new name:', user, 'UNKNOWN')

            exists = False
            for (name, number) in rubric:
                if name == user:
                    exists = True
                    break
            if not exists:
                rubric.append((user, 'UNKNOWN'))

        else:
            try:
                idx = int(choice) - 1
                chosen = suggestions[idx]
                print('Selected:', chosen[0], chosen[1])
                current_text.append(chosen[0])
            except:
                print('Invalid choice.')

    # CASE C: not found
    else:
        choice = input('Not found. Add new contact? (y/n): ').strip().lower()
        if choice == 'y':
            number = input('Enter phone number: ').strip()
            rubric.append((user, number))
            current_text.append(user)
            print('Added:', user, number)

    print('Current Searches:', " ".join(current_text))

# 3) UPDATE FILE
output_file = open(argv[1], 'w')
for (name, number) in rubric:
    output_file.write(name + " " + str(number) + "\n")
output_file.close()
