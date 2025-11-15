def generate_profile(age):
    if age >= 0 and age <= 12:
        return ('Child')
    elif age >= 13 and age <= 19:
        return ('Teenager')
    elif age >= 20:
        return ('Adult')


user_name = input("Enter your full name:")
birth_year_str = input("Enter your birth year:")
birth_year = int(birth_year_str)
current_age = 2025 - birth_year
hobbies = []
while True:
    hobby = input("Enter a favorite hobby оr type 'stop' to finish: ")
    if hobby.strip().lower() == "stop":
        break
    hobbies.append(hobby)
life_stage = generate_profile(current_age)
user_profile = {"name": user_name,
                "age": current_age,
                "stage": life_stage,
                "hobbies": hobbies}
profile_summary = """---
Profile Summary:"""
for key, value in user_profile.items():
    match key:
        case "name":
            profile_summary += f"\nName: {value}\n"
        case "age":
            profile_summary += f"Age: {value}\n"
        case "stage":
            profile_summary += f"Life Stage: {value}\n"
        case "hobbies":
            num_hobby = len(value)
            if num_hobby == 0:
                profile_summary += "You didn't mention any hobbies.\n"
            else:
                profile_summary += f"Favorite Hobbies ({num_hobby}):\n"
                for h in value:
                    profile_summary += f"- {h}\n"
profile_summary += "---"
print(profile_summary)
