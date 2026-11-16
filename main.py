Znishka = 10
MIN_SUM = 1000

# Введення даних
name: str = input("Введіть своє ім'я: ")
product: str = input("Введіть назву товару: ")

price: float = float(input("Введіть ціну товару: "))
count: int = int(input("Введіть кількість товару: "))

# Перевірка даних
if price <= 0 or count <= 0:
    print("Помилка! Введіть правильні дані.")

else:
    # Розрахунок вартості
    total: float = price * count

    print("Загальна сума:", total, "грн")

    # Перевірка знижки
    if total >= MIN_SUM:
        discount: float = total * Znishka / 100
        print("Вам надано знижку 10%")
    elif total >= 500:
        discount: float = total * 5 / 100
        print("Вам надано знижку 5%")
    else:
        discount: float = 0.0
        print("Знижки немає")

    # Розрахунок кінцевої суми
    result: float = total - discount

    # Перевірка покупки
    status: str = "Є знижка" if discount > 0 else "Без знижки"

    has_discount: bool = discount > 0

    if has_discount:
        if result < total:
            print("Знижку застосовано!")

    # Вибір оплати
    print("\nОберіть спосіб оплати:")
    print("1 - Готівка")
    print("2 - Картка")
    print("3 - Онлайн")

    payment: int = int(input("Ваш вибір: "))

    match payment:
        case 1:
            method = "Готівка"
        case 2:
            method = "Картка"
        case 3:
            method = "Онлайн"
        case _:
            method = "Не вибрано"

    # Виведення результату
    print("\n----- ЧЕК -----")
    print(f"Покупець: {name}")
    print(f"Товар: {product}")
    print(f"Ціна: {price} грн")
    print(f"Кількість: {count}")
    print(f"Загальна сума: {total} грн")
    print(f"Знижка: {discount} грн")
    print(f"До сплати: {result} грн")
    print(f"Оплата: {method}")
    print(f"Статус: {status}")
    print("---------------")
