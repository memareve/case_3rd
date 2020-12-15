# Case-study #3
# Developers: Marinkin O. (%),
# Seledtsov A. (%),
# Evdischenko M. (%)


s = int(input('начальные вложения '))
dop = int(input('Инвестиционные вливания '))
period = str(input('Месяц,год, день? '))
period.lower()
percent = input('процентная ставка ')
percent.replace(',', '.')
percent = float(percent)


n = int(input('количество периодов '))
a = 1
while a < n:
    if a == 1:
        sum = s * (1+ percent )
        print('меясц', a)
        print('капитал', sum)
    s = sum + dop
    print('месяц ', a)
    print('основа инвестиции', round(s, 2))
    sum = s * (1+ percent )
    print('month sum', round(sum - s, 2 ))
    print('capital', round(sum, 2))
    a += 1
