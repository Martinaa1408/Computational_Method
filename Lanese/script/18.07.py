from sys import argv

def add_activity(activities):
    print("\n-- Add New Activity --")
    name = input("Enter activity name: ").strip()
    start = int(input("Enter start time (0-23): "))
    end = int(input("Enter end time (1-24): "))

    if start < 0 or start > 23 or end < 1 or end > 24 or start >= end:
        print("Invalid times.")
        return
        
    for act in activities:
        old_name, s, e = act
        if start < e and end > s:
            print("Warning: overlaps with", old_name, "(", s, "-", e, ")")

    activities.append((name, start, end))
    print("Activity added.")

def print_activities(activities):
    print("\n-- Your Daily Activities --")
    if len(activities) == 0:
        print("No activities.")
        return

    i = 0
    while i < len(activities):
        name, start, end = activities[i]
        print(i + 1, "-", name, "from", start, "to", end)
        i += 1

def save_activities(activities, filename):
    f = open(filename, "w")
    for act in activities:
        name, start, end = act
        line = name + "," + str(start) + "," + str(end) + "\n"
        f.write(line)
    f.close()
    print("Activities saved in file:", filename)

def load_activities(filename):
    activities = []
    try:
        f = open(filename, "r")
        for line in f:
            line = line.strip()
            if line == "":
                continue
            parts = line.split(",")
            name = parts[0]
            start = int(parts[1])
            end = int(parts[2])
            activities.append((name, start, end))
        f.close()
        print("Activities loaded from file.")
    except FileNotFoundError:
        print("File not found. Starting with empty list.")
    return activities

def main():
    if len(argv) != 2:
        print("Usage: python activities.py <file>")
        return

    filename = argv[1]
    activities = []

    while True:
        print("\n===== Daily Activity Manager =====")
        print("1. Add activity")
        print("2. Print activities")
        print("3. Save to file")
        print("4. Load from file")
        print("5. Exit")

        choice = input("Choice: ").strip()

        if choice == "1":
            add_activity(activities)
        elif choice == "2":
            print_activities(activities)
        elif choice == "3":
            save_activities(activities, filename)
        elif choice == "4":
            activities = load_activities(filename)
        elif choice == "5":
            print("Bye!")
            break
        else:
            print("Invalid choice.")

main()
