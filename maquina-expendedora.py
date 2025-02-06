name_prod = ["Agua", "Refresco", "Zumo"]
num_prod = [1, 2, 3]
price_prod = [0.50, 0.75, 0.95]
machine_coins = [20, 20, 20, 20, 20, 20]
types_coins = [0.05, 0.1, 0.2, 0.5, 1, 2]

def menu(name_prod, price_prod):
    for i in range(len(name_prod)):
        print(f"{i+1}. {name_prod[i]}: {price_prod[i]}")
    print("Salir")

def calcularCambio(money_sum, machine_coins, type_coins, price_prod, choice):
    change_sum = 0
    for i in range(len(type_coins)-1, -1, -1):
        if change_sum + type_coins[i] <= money_sum - price_prod[choice - 1]:
            change_sum += type_coins[i]
            machine_coins[i] -= 1
    return change_sum

menu(name_prod, price_prod)
choice = int(input("ELIJA PRODUCTO"))
while choice not in num_prod:
    choice = int(input("LA OPCIÓN NO EXISTE"))
money = 0
money_sum = 0


if machine_coins.count(0) < 2 and machine_coins[0] != 0:
    while money_sum < price_prod[choice - 1]:
        money = float(input("Introduzca monedas"))
        machine_coins[types_coins.index(money) - 1]+=1
        money_sum += money
    print(f"El cambio es: {calcularCambio(money_sum, machine_coins, types_coins, price_prod, choice)}")
else:
    while money_sum != price_prod[choice - 1]:
        money = float(input("Introduzca importe exacto"))
        money_sum += money
