from sys import argv

def load_activities(filename):
    activities = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    name = parts[0]
                    start = int(parts[1])
                    end = int(parts[2])
                    activities.append((name, start, end))
    except FileNotFoundError:
        pass
    return activities

def save_activities(filename, activities):
    with open(filename, 'w') as f:
        for act in activities:
            line = act[0] + "," + str(act[1]) + "," + str(act[2]) + "\n"
            f.write(line)

def activity_manager(activities, filename):
    while True:
        print("\n===== Daily Activity Manager =====")
        print("1. Add a new activity")
        print("2. Print all activities")
        print("3. Save activities to file")
        print("4. Load activities from file")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            print("\n— Add New Activity —")
            name = input("Enter activity name: ")
            start = int(input("Enter start time (0-23): "))
            end = int(input("Enter end time (1-24): "))
            new_act = (name, start, end)

            for act in activities:
                if max(act[1], start) < min(act[2], end):
                    print("Warning: This activity overlaps with existing activity '" + act[0] + " (" + str(act[1]) + " - " + str(act[2]) + ")'")
                    break

            activities.append(new_act)
            print("Activity '" + name + "' added!")

        elif choice == "2":
            print("\n— Your Daily Activities —")
            for i in range(len(activities)):
                act = activities[i]
                print(str(i + 1) + ". " + act[0] + " from " + str(act[1]) + " to " + str(act[2]))

        elif choice == "3":
            save_activities(filename, activities)
            print("Activities saved to file.")

        elif choice == "4":
            activities.clear()
            activities.extend(load_activities(filename))
            print("Activities loaded from file.")

        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")

def main():
    try:
        filename = argv[1]
        activities = load_activities(filename)
        activity_manager(activities, filename)
    except IndexError:
        print("Please provide the input filename as argument.")

main()
