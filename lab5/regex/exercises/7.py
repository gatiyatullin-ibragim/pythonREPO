def snake_to_camel(str):
    words = str.split('_')
    camel_str = words[0] + ''.join(word.capitalize() for word in wrds[1:])
    return camel_str

snake_case_str = str(input())
print(snake_to_camel(snake_case_str))