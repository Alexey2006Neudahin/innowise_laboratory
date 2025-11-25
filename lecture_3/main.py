def main():
    # Initialize an empty list to store all students
    students = []

    def new_student(students: list):
        """Add a new student to the system with validation"""
        while True:
            raw_name = input("Enter student's name: ").strip()
            try:
                # Validation: Check for empty input
                if not raw_name:
                    raise ValueError('Name cannot be empty.')

                # Validation: Check if name contains any digits
                if any(char.isdigit() for char in raw_name):
                    raise ValueError('The name must not contain numbers')

                # Validation: Check for punctuation and special characters
                forbidden_chars = set('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
                if any(char in forbidden_chars for char in raw_name):
                    raise ValueError(
                        ' The name must not contain punctuation marks or special characters')

                # Normalize the name: Capitalize first letter of each word
                name = ''.join(word.capitalize() for word in raw_name.split())

                for student in students:
                    if name in student:
                        print(
                            f"Name '{name}' already exists. Choose another name.")
                        break
                else:
                    students.append({name: []})
                    print(f'{name} has been added.')
                    break

            except ValueError as e:
                print(f'Error: {e}')

    def add_grade(students: list):
        while True:
            raw_name = input("Enter student's name: ").strip()
            try:
                # Validation: Check for empty input
                if not raw_name:
                    raise ValueError('Name cannot be empty.')

                # Validation: Check if name contains any digits
                if any(char.isdigit() for char in raw_name):
                    raise ValueError('The name must not contain numbers')

                # Validation: Check for punctuation and special characters
                forbidden_chars = set('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
                if any(char in forbidden_chars for char in raw_name):
                    raise ValueError(
                        ' The name must not contain punctuation marks or special characters')

                # Normalize the name: Capitalize first letter of each word
                name = ''.join(word.capitalize() for word in raw_name.split())

                student_found = None
                for student in students:
                    if name in student:
                        while True:
                            grade_input = input(
                                "Enter a grade or 'done' to finish ").strip().lower()
                            if grade_input == 'done':
                                return
                            try:
                                if any(char.isalpha() for char in grade_input):
                                    raise ValueError(
                                        'The name must not contain numbers\n')
                                if not grade_input.isdigit():
                                    raise ValueError(
                                        'The grade must be a number\n')
                                grade_val = int(grade_input)
                                if grade_val < 0 or grade_val > 100:
                                    raise ValueError(
                                        'Invalid input. Please enter a number between 0 and 100\n')
                                student[name].append(grade_val)

                            except ValueError as error:
                                print(error)

                        return

                else:
                    print('Student is not found')
                    return
            except ValueError as e:
                print(f'Error: {e}')

    while True:
        try:
            # Display menu options
            print('1. Add a new student')
            print('2. Add a grades for a student')
            print('3. Show report(all students)')
            print('4. Find a top performer')
            print('5. Exit')

            choice = int(input('Enter option:'))

            if choice == 1:
                new_student(students)
            elif choice == 2:
                add_grade(students)

        except Exception as e:
            print(f'ошибка {e}')


if __name__ == '__main__':
    main()
