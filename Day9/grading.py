student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
for student in student_scores:
    score = student_scores[student]
    if score <= 70:
        print(f"{student} Fail")
    elif 71 <= score <= 80:
        print(f"{student} Acceptable")
    elif 81 <= score <= 90:
        print(f"{student} Exceeds Expectations")
    else:
        print(f"{student} Outstanding")

student_grades = {}
