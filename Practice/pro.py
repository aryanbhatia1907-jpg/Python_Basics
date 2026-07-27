stud = {
    "Ramu":  [55, 63, 75],
    "Shyam": [88, 92, 79],
    "Geeta": [45, 38, 52],
    "Mohan": [72, 68, 74],
    "Priya": [91, 95, 88],
}

def get_average(marks):
    return sum(marks) / len(marks)

def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "F"

highest_name = ""
highest_avg = 0

for name, marks in stud.items():
    avg = get_average(marks)
    grade = get_grade(avg)
    print(f"{name} | Avg: {round(avg, 2)} | Grade: {grade}")

    if avg > highest_avg:
        highest_avg = avg
        highest_name = name

print(f"\nHighest: {highest_name} with {round(highest_avg, 2)}")