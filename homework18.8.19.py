tickets=int(input("Укажите количество билетов которое вы хотите купить: "))
summa=0
count=0
while count < tickets:
    age=int(input("Введите возраст: "))
    price=0
    if age < 18:
        pass
    elif 18 <= age < 25:
        price = 990
    elif age >= 25:
        price = 1390
    summa += price
    count += 1

if tickets <= 3:
    print(f'Сумма стоимости билетов {summa} руб.')
else:
    discount = summa * 0.1
    summa = summa * 0.9
    print(f'Сумма стоимости билетов {summa} руб. скидка: {discount} руб.')