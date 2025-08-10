subjects = ("Calculus with Analysis", "Basic Electronics",
            "Communication Skills")

students = {}


def calculate_grade(avg):
    if avg >= 70:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 50:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"


add_more = True
while add_more:
    
    while True:
        name = input("Enter student name: ").strip()
        if name.replace(" ", "").isalpha():
            break
        else:
            print("Please enter letters only for the name.")

    scores = []
    for subject in subjects:
        while True:
            try:
                score = float(input(f"Enter score for {subject}: "))
                if 0 <= score <= 100:
                    grade = calculate_grade(score)  
                    scores.append((score, grade))
                    break
                else:
                    print("Score must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")

    
    total = sum(s[0] for s in scores)
    average = total / len(subjects)
    overall_grade = calculate_grade(average)

 
    students[name] = {
        "Scores": scores,  
        "Total": total,
        "Average": average,
        "Grade": overall_grade
    }

  
    while True:
        choice = input("Add another student? (yes/no): ").lower().strip()
        if choice in ("yes", "no"):
            break
        else:
            print("Please enter only 'yes' or 'no'.")
    if choice == "no":
        add_more = False


while True:
    search_name = input("\nSearch student performance by name (or type 'done' to finish): ").strip()
    if search_name.lower() == "done":
        break
    elif search_name in students:
        details = students[search_name]
        print(f"\nPerformance for {search_name}:")
        for i, subject in enumerate(subjects):
            score, grade = details['Scores'][i]
            print(f"  {subject}: {score} ({grade})")
        print(f"  Total: {details['Total']}")
        print(f"  Average: {details['Average']:.2f}")
        print(f"  Overall Grade: {details['Grade']}")
    else:
        print("Student not found.")

print("\n=== Students Performance Summary (Sorted by Average Score) ===")
sorted_students = sorted(students.items(), key=lambda x: x[1]['Average'], reverse=True)

for name, details in sorted_students:
    print(f"{name}: Total={details['Total']}, Average={details['Average']:.2f}, Grade={details['Grade']}")
