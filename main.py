# Case-study #3
# Developers: Marinkin O. (30%),
# Seledtsov A. (30%),
# Evdischenko M. (85%)

from decimal import Decimal
from prettytable import PrettyTable

tb = PrettyTable()

quest = input('Вы хотите открыть вклад? (да/нет):').lower().replace(' ', '')
if quest == 'да':
    print('Отлично!')
else:
    print('Очень грустно...')
    exit()
answer = input('Вы хотите открыть вклад на год или более? (да/нет):').lower().replace(' ', '')
d = input('Период, по итогам которого происходит начисление процентов (месяц/год):').lower().replace(' ', '')
if answer == 'да':
    n = int(input('Срок размещения капитала (лет):'))
else:
    n = int(input('Срок размещения капитала (мес.):'))
    if d == 'год' and n < 12:
        print('Мы можем предложить вам только начисление по месяцам, т.к. срок вашего вклада меньше года.')
    if n == 12:
        answer = 'да'
        n = 1
s = float(input('Начальный капитал ($):'))
percent = input('Процентная ставка (%):').replace(',', '.')
percent = float(int(percent) / 100)
dop = int(input('Инвестиционные вливания ($/мес.):'))
capital = 0

if d == 'месяц':
    if answer == 'да':
        for i in range(1, n + 1):
            print(i, 'год')
            tb.field_names = ['месяц', 'основа инвестиций', 'сумма % за месяц', 'капитал']
            for j in range(1, 13):
                tb.add_row([j, Decimal(s).quantize(Decimal("1.00")), Decimal(s * percent).quantize(Decimal("1.00")),
                            Decimal(s * percent + s).quantize(Decimal("1.00"))])
                capital = s * percent + s
                s = capital + dop
            print(tb)
            tb.clear_rows()
    else:
        print(1, 'год')
        tb.field_names = ['месяц', 'основа инвестиций', 'сумма % за месяц', 'капитал']
        for i in range(1, n + 1):
            tb.add_row([i, Decimal(s).quantize(Decimal("1.00")), Decimal(s * percent).quantize(Decimal("1.00")),
                        Decimal(s * percent + s).quantize(Decimal("1.00"))])
            capital = s * percent + s
            s = capital + dop
        print(tb)
else:
    tb.field_names = ['год', 'основа инвестиций', 'сумма % за год', 'капитал']
    for i in range(1, n + 1):
        tb.add_row([i, Decimal(s).quantize(Decimal("1.00")), Decimal(s * percent).quantize(Decimal("1.00")),
                    Decimal(s * percent + s).quantize(Decimal("1.00"))])
        capital = s * percent + s
        s = capital + dop
    print(tb)
