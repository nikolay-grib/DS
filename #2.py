def numeral_noun_declension(
    number,
    nominative_singular,
    genetive_singular,
    nominative_plural
):
    return (
        (number in range(5, 20)) and nominative_plural or
        (1 in (number, (diglast := number % 10))) and nominative_singular or
        ({number, diglast} & {2, 3, 4}) and genetive_singular or nominative_plural
    )

print("В строке", a:=len(input("Введите строку: ")), numeral_noun_declension(a, 'символ', 'символа', 'символов'))