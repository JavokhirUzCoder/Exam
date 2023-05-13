

numbers = "123465789"

letters = "qwrtypsdfghjklmnbvcxzaeuio"


word = input("")

letters_result = 0
numbers_result = 0

def unli_undosh_simvol_aniqla(text):
    global numbers_result, letters_result

    text = text.lower()
    for i in text:
        if i in letters:
            letters_result += 1
        if i in numbers:
            numbers_result += 1


unli_undosh_simvol_aniqla(word)

print("LETTERS ", letters_result)
print("NUMBERS ", numbers_result)
