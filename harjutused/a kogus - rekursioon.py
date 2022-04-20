def count_a(text):
    if len(text) == 0:
        return 0
    first_char = text[0]
    rest_of_the_text = text[1:]
    first_char_result = 0
    if first_char == 'a':
        first_char_result = 1
    return first_char_result + count_a(rest_of_the_text)

print(count_a("alberoaam"))