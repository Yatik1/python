score = 10

if score >100:
    print("Verify your Score again")
    exit()

if score >= 90:
    grade="A"
elif score >= 80:
    grade="B"
elif score >= 70:
    grade="C"
elif score >=60:
    grade="D"
else:
    grade="F"

print("Your Grade is : " ,grade)