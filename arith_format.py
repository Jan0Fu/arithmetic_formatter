import re

user_input = str(input("Input up to 5 arithmetic problems: "))
if len(user_input) > 65 or user_input.count(",") > 4:
    print("Error: Too many problems.")
elif bool(re.search('[/*&$@#|:.;!?]', user_input)):
    print("Error: Operator must be '+' or '-'.")
elif bool(re.search('[a-zA-Z]', user_input)):
    print("Error: Numbers must only contain digits.")
elif bool(re.search())
problems = user_input.split(", ")
print(problems)
