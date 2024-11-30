inventory = {
    "apple": {"quantity": 100, "price": 1},  # Словарь инвентаря: название товара - словарь с количеством и ценой
    "banana": {"quantity": 50, "price": 0.5},
    "orange": {"quantity": 75, "price": 0.75}
}

def restock(item, quantity, price, inventory):
    """Пополняет склад указанным товаром.  Обновляет количество и цену, если необходимо."""
    # TODO: Реализовать логику пополнения склада.
    #
    if item in inventory:
        inventory[item]['quantity'] += quantity
        inventory[item]['price'] = price
    else:
        print("Ощибка: Такого товара нету в базе данных, пожалуйста выберите другой товар")
    pass


def sell(item, quantity, inventory):
    """Продаёт указанный товар. Возвращает общую выручку."""
    # TODO: Реализовать логику продажи товара.
    #
    if item in inventory and inventory[item]['quantity'] >= quantity:
        inventory[item]['quantity'] -= quantity
        return inventory[item]['price'] * quantity
    else:
        return 0,'такого нет'


def generate_report(inventory):
    """Генерирует отчёт о текущем состоянии склада."""
    # TODO: Реализовать генерацию отчета.
    #       Отчет должен содержать информацию о каждом товаре: название, количество и цена.
    report = "Текущие запасы "
    for item, data in inventory.items():
        total_value = data['quantity'] * data['price']
        report += f"{item}: {data['quantity']} штук по {data['price']} ($). Общая стоимость: {total_value}\n"
    print(report)
    pass


# Main game loop (основной цикл игры)
while True:
    # TODO: Реализовать ввод данных пользователем и вызовы функций.
    #       Нужно предоставить пользователю меню для выбора действий (пополнение склада, продажа, отчет, выход).
    #       В зависимости от выбора пользователя, нужно вызывать соответствующие функции и обрабатывать ввод данных.
    action = input("Выберите действие (1)restock/(2)sell/(3)report/(4)exit): \n")
    if action == "1":
        item = input("Введите название товара: ")
        quantity = int(input("Введите количество: "))
        price = float(input("Введите цену: "))
        restock(item, quantity, price, inventory)
    elif action == "2":
        item = input("Введите название товара: ")
        quantity = int(input("Введите количество: "))
        revenue = sell(item, quantity, inventory)[0]
        if revenue > 0:
            print(f"Выручка от продажи: {revenue}")
        else:
            print(sell(item, quantity, inventory)[1])

    elif action == "3":
        generate_report(inventory)
    elif action == "4":
        break
    else:
        print("Некорректный ввод, попробуйте снова.")
    pass