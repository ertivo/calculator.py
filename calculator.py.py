def add(a, b):
    """Dodawanie"""
    return a + b

def subtract(a, b):
    """Odejmowanie"""
    return a - b

def multiply(a, b):
    """Mnożenie"""
    return a * b

def divide(a, b):
    """Dzielenie"""
    if b != 0:
        return a / b
    else:
        return "Błąd: Dzielenie przez zero"

def main():
    print("Witaj w Prostej Kalkulatorze!")
    num1 = float(input("Podaj pierwszą liczbę: "))
    num2 = float(input("Podaj drugą liczbę: "))

    print("\nDostępne operacje:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    choice = int(input("Wybierz operację (1/2/3/4): "))

    if choice == 1:
        result = add(num1, num2)
    elif choice == 2:
        result = subtract(num1, num2)
    elif choice == 3:
        result = multiply(num1, num2)
    elif choice == 4:
        result = divide(num1, num2)
    else:
        result = "Nieprawidłowy wybór"

    print(f"Wynik: {result}")

if __name__ == "__main__":
    main()
