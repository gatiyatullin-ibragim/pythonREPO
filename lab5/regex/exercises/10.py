import re

def camel_to_snake(camel_str):
    pattern = r'(?<!^)(?=[A-Z])'
    snake_case_str = re.sub(pattern, '_', camel_str).lower()
    return snake_case_str

camel_case_str = "thisIsACamelCaseString"
snake_case_str = camel_to_snake(camel_case_str)
print("Camel case:", camel_case_str)
print("Snake case:", snake_case_str)
