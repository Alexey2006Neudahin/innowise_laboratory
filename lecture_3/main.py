def main():
    # Initialize an empty list to store all students
    students = []

    def new_student(students):
        """Add a new student to the system with validation"""
        while True:
            try:
                raw_name = input("Enter student's name: ").strip()
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
                        raise ValueError(
                            f"Name '{name}' already exists. Choose another name.")

                # If all validations pass, exit the input loop
                break
            except ValueError as e:
                print(f'Error: {e}')

        new_student_dict = {name: []}
        # Add the new student to the students list
        students.append(new_student_dict)

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

        except Exception as e:
            print(f'ошибка {e}')


if __name__ == '__main__':
    main()
