def numeral_noun_declension(
    number,
    nominative_singular,    # существительное в именительном падеже
    genetive_singular,      # существительное в родительном падеже единственного числа
    nominative_plural       # существительное в родительном падеже множественного числа
):
    return (
        (number in range(5, 20)) and nominative_plural or
        (1 in (number, (diglast := number % 10))) and nominative_singular or
        ({number, diglast} & {2, 3, 4}) and genetive_singular or nominative_plural
    )

print("В строке", a:=len(input("Введите строку: ")), numeral_noun_declension(a, 'символ', 'символа', 'символов'))