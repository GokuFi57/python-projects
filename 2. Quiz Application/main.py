questions = {
    "Python is a ___ language? ": "programming",
    "2 + 2 = ? ": "4",
    "Capital of India? ": "delhi"
}

score = 0

for q, ans in questions.items():
    user = input(q).lower()
    if user == ans:
        score += 1

print("Your score is:", score)