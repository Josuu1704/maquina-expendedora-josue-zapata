name_prod = ["Agua", "Refresco", "Zumo"]
num_prod = [1, 2, 3]
price_prod = [0.50, 0.75, 0.95]
machine_coins = [20, 20, 20, 20, 20, 20]
types_coins = [0.05, 0.1, 0.2, 0.5, 1, 2]


def menu(name_prod, price_prod):
    for i in range(len(name_prod)):
        print(f"{i + 1}. {name_prod[i]}: {price_prod[i]}")
    print("4. Salir")


def calcularCambio(money_sum, machine_coins, types_coins, price_prod, choice):
    change_sum = 0
    change_needed = money_sum - price_prod[choice - 1]
    for i in range(len(types_coins) - 1, -1, -1):
        while change_sum + types_coins[i] <= change_needed and machine_coins[i] > 0:
            change_sum += types_coins[i]
            machine_coins[i] -= 1
    return change_sum


while True:
    menu(name_prod, price_prod)
    choice = int(input("ELIJA PRODUCTO (o 4 para salir): "))

    if choice == 4:
        print("Saliendo del sistema...")
        break

    while choice not in num_prod:
        choice = int(input("LA OPCIÓN NO EXISTE, intente nuevamente: "))

    money_sum = 0
    if machine_coins.count(0) < 2 and machine_coins[0] != 0:
        while money_sum < price_prod[choice - 1]:
            money = float(input("Introduzca monedas: "))
            if money in types_coins:
                machine_coins[types_coins.index(money)] += 1
                money_sum += money
            else:
                print("Moneda no válida.")
        print(f"El cambio es: {calcularCambio(money_sum, machine_coins, types_coins, price_prod, choice)}")
    else:
        while money_sum != price_prod[choice - 1]:
            money = float(input("Introduzca importe exacto: "))
            money_sum += money
