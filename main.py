# Collects subject name and weekly study hours from the user,
# validates the input, and returns the data as a dictionary
def get_subject():
    name = input("Enter subject name: ")

    # Ensures the user enters a valid positive number of hours
    while True:
        try:
            hours = int(input("Enter hours per week: "))
            if hours <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid, please try again.")

    return {
        "name": name,
        "hours": hours
    }


# Stores all subject data as dictionaries inside a list
subjects = []

# Repeatedly collects subject data until the user chooses to stop
while True:
    subject = get_subject()
    subjects.append(subject)

    # Appends subject data to a file for persistent storage
    with open("data.txt", "a") as file:
        file.write(f"{subject['name']},{subject['hours']}\n")

    choice = input("Add another subject? (y/n): ").lower()
    if choice != "y":
        break


# Calculates the total weekly study load across all subjects
sum_all_hours = 0
for s in subjects:
    sum_all_hours += s["hours"]

print(f"\nTotal weekly load: {sum_all_hours} hours")

# Flags potential overload if total weekly hours exceed a threshold
if sum_all_hours > 40:
    print("Overload detected")


# Calculates the average study hours per subject
average_hours = sum_all_hours / len(subjects)
print(f"Average hours per subject: {average_hours}")

# Identifies subjects that significantly exceed the average workload
for s in subjects:
    if s["hours"] > 1.5 * average_hours:
        print(f"Imbalance detected: {s['name']} ({s['hours']} hours)")


# Finds and displays the subject with the highest weekly workload
max_hours = max(subjects, key=lambda s: s["hours"])
print(f"Heaviest subject: {max_hours['name']} ({max_hours['hours']} hours)")
