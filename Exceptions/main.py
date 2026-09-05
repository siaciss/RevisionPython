# For creer our exception, we need to create a new class that inherits from the
# built-in Exception class. This allows us to define our own custom exception 
# with a specific name and behavior.
class InvalidAgeError(Exception):
    pass

def get_age():
    age_inp = input("Please enter your age: ")
    # return int(age_inp)
    age = int(age_inp)
    if age < 0 or age > 120:
        raise InvalidAgeError("Age must be between 0 and 120.")
    return age

def get_file_content(file_path):
    with open(file_path, "r") as file:
        return file.read()

# age_inp = input("Please enter your age: ")
# age = int(age_inp)

# age = get_age()
# print("You are", age, "years old.")
# print("You are {} years old.".format(age))
# print("You are %d years old." % age)

# age = None
# while age is None:
#     try:
#         age = get_age()
#         print("You are", age, "years old.")
#     except ValueError as ex:
#         print(ex)
#         print("Invalid input. Please enter a valid integer for your age.")

path = "Exceptions/input/simple.txt"
try:
    age = get_age()
    if age >= 18:
        content = get_file_content(path)
        print(content)
    else:
        print("You are not old enough to access the file.")

# except FileNotFoundError as ex:
#     print(ex)
#     print("The specified file was not found.")
# except ValueError as ex2:
#     print(ex2)
#     print("Invalid input. Please enter a valid integer for your age.")  

except(ValueError, FileNotFoundError) as ex:
    # print(ex)
    print("An error occurred. Please check your input and the file path.")  

except InvalidAgeError as ex2:
    print(ex2)
except Exception as ex3:
    print(ex3)
    # print("An unexpected error occurred.")
else:
    print("No errors occurred. The program executed successfully.")
finally:
    print("Execution completed. Thank you for using the program.")
