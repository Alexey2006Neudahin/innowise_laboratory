def generate_profile(age):
    if age >= 0 and age <= 12:
        return ('Child')
    elif age >= 13 and age <= 19:
        return ('Teenager')
    elif age >= 20:
        return ('Adult')


user_name = input("Enter your name:")
birth_year_str = input("Enter your birth year:")
birth_year = int(birth_year_str)
print(type(birth_year))
generate_profile(5)
