# Case-study #3
# Developers: Marinkin O. (85%),
# Seledtsov A. (%),
# Evdischenko M. (%)

from decimal import Decimal
from prettytable import PrettyTable
tb = PrettyTable()



print('Вы хотите открыть вклад на год или более? (да/нет)')
answer = input().lower().replace(' ', '')
if answer == 'да':
    n = int(input('Срок размещения капитала (лет):'))
    d = input('Период, по итогам которого происходит начисление процентов (месяц/год):').lower().replace(' ', '')
else:
    n = int(input('Срок размещения капитала (мес.):'))
    if n == 12:
        answer = 'да'
        n = 1
s = float(input('Начальный капитал ($):'))
percent = input('Процентная ставка (%):').replace(',', '.')
percent = float(int(percent) / 100)
dop = int(input('Инвестиционные вливания ($/мес.):'))
capital = 0


tb.field_names = ['месяц', 'основа инвестиций', 'сумма % за месяц', 'капитал']
tb.add_row([1, Decimal(s).quantize(Decimal("1.00")), Decimal(s * percent).quantize(Decimal("1.00")), Decimal(s * percent + s).quantize(Decimal("1.00"))])

if d == 'месяц':
    if answer == 'да':
        for i in range(1,n+1):
            print(i, 'год')
            tb.columns.header = ['месяц', 'основа\nинвестиций', 'сумма %\nза месяц', 'капитал']
            for i in range(1,13):
                if i >= 10:
                    print(i, Decimal(s).quantize(Decimal("1.00")), Decimal(s * percent).quantize(Decimal("1.00")), Decimal(s * percent + s).quantize(Decimal("1.00")))
                    capital = s * percent + s
                    s = capital + dop
                else:
                    print(i, Decimal(s).quantize(Decimal("1.00")), Decimal(s * percent).quantize(Decimal("1.00")), Decimal(s * percent + s).quantize(Decimal("1.00")))
                    capital = s * percent + s
                    s = capital + dop

    else:
        print(1, 'год')
        for i in range(1,n+1):
            tb.add_row([i, Decimal(s).quantize(Decimal("1.00")), Decimal(s * percent).quantize(Decimal("1.00")), Decimal(s * percent + s).quantize(Decimal("1.00"))])
            capital = s * percent + s
            s = capital + dop
        print(tb)




else:
    print('''-----------------------------------------------------
|         |    основа    |  сумма %    |            |
|   год   |  инвестиций  |  за год     |  капитал   |
------------------------------------------------------''')
    for i in range(1, n + 1):
        if i >= 10:
            print('|    ', i, '    |', Decimal(s).quantize(Decimal("1.00")), '  |',
                  Decimal(s * percent).quantize(Decimal("1.00")), '  |',
                  Decimal(s * percent + s).quantize(Decimal("1.00")), '  |', sep='')
            capital = s * percent + s
            s = capital + dop
        else:
            print('|    ', i, '    |', Decimal(s).quantize(Decimal("1.00")), '  |',
                  Decimal(s * percent).quantize(Decimal("1.00")), '  |',
                  Decimal(s * percent + s).quantize(Decimal("1.00")), '  |', sep='')
            capital = s * percent + s
            s = capital + dop
    print('''------------------------------------------------------
     ''')
