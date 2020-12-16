# Case-study #3
# Developers: Marinkin O. (85%),
# Seledtsov A. (%),
# Evdischenko M. (%)

from decimal import Decimal

print('Вы хотите открыть вклад на год или более? (да/нет)')
answer = input().lower().replace(' ', '')
if answer == 'да':
    n = int(input('Срок размещения капитала (лет):'))
else:
    n = int(input('Срок размещения капитала (мес.):'))
    if n == 12:
        answer = 'да'
        n = 1
d = input('Период, по итогам которого происходит начисление процентов (месяц/год):').lower().replace(' ', '')
s = float(input('Начальный капитал ($):'))
percent = input('Процентная ставка (%):').replace(',', '.')

percent = float(int(percent) / 100)
dop = int(input('Инвестиционные вливания ($/мес.):'))
capital = 0

if d == 'месяц':
    if answer == 'да':
        for i in range(1,n+1):
            print(i, 'год')
            print('''-----------------------------------------------------
|          |    основа    |  сумма %    |            |
|  месяц   |  инвестиций  |  за месяц   |  капитал   |
------------------------------------------------------''')
            for i in range(1,13):
                if i >= 10:
                    print('|    ', i, '    |', Decimal(s).quantize(Decimal("1.00")), '          |', Decimal(s * percent).quantize(Decimal("1.00")), '  |', Decimal(s * percent + s).quantize(Decimal("1.00")), '  |', sep='')
                    capital = s * percent + s
                    s = capital + dop
                else:
                    print('|    ', i, '     |', Decimal(s).quantize(Decimal("1.00")), '          |', Decimal(s * percent).quantize(Decimal("1.00")), '  |', Decimal(s * percent + s).quantize(Decimal("1.00")), '  |', sep='')
                    capital = s * percent + s
                    s = capital + dop
            print('''------------------------------------------------------
         ''')
    else:
        print(1, 'год')
        print('''-----------------------------------------------------
    |          |    основа    |  сумма %    |            |
    |  месяц   |  инвестиций  |  за месяц   |  капитал   |
    ------------------------------------------------------''')
        for i in range(1,n+1):
            if i >= 10:
                print('|    ', i, '    |', Decimal(s).quantize(Decimal("1.00")), '  |', Decimal(s * percent).quantize(Decimal("1.00")), '  |', Decimal(s * percent + s).quantize(Decimal("1.00")), '  |', sep='')
                capital = s * percent + s
                s = capital + dop
            else:
                print('|    ', i, '     |', Decimal(s).quantize(Decimal("1.00")), '  |', Decimal(s * percent).quantize(Decimal("1.00")), '  |', Decimal(s * percent + s).quantize(Decimal("1.00")), '  |', sep='')
                capital = s * percent + s
                s = capital + dop
            print('''------------------------------------------------------
         ''')
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
