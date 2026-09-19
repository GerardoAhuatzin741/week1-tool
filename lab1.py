user_input = input("Enter a score from 0-100: ")

try:
    score = float(user_input)
except ValueError:
    print(f"'{user_input}' is not a valid number. Please enter a number between 0 and 100.")
else:
    if score < 0 or score > 100:
        print(f"{score} is out of range. Please enter a value between 0 and 100.")
    elif score >= 90:
        print(f"Score {score}: Grade A")
    elif score >= 80:
        print(f"Score {score}: Grade B")
    elif score >= 70:
        print(f"Score {score}: Grade C")
    elif score >= 60:
        print(f"Score {score}: Grade D")
    else:
        print(f"Score {score}: Grade F")