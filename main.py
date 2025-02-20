# main.py
from app.algorithms import modular_exponentiation, gcd_extended, modular_inverse

def main():
    while True:
        print("Выберите операцию:")
        print("1. Возведение в степень по модулю (a^x mod p)")
        print("2. Вычисление НОД (a, b)")
        print("3. Вычисление инверсии (e mod z)")
        print("4. Выход")

        choice = input("Введите номер операции: ")

        if choice == '1':
            a = int(input("Введите a: "))
            x = int(input("Введите x: "))
            p = int(input("Введите p: "))
            result = modular_exponentiation(a, x, p)
            print(f"{a}^{x} mod {p} = {result}")

        elif choice == '2':
            a = int(input("Введите a: "))
            b = int(input("Введите b: "))
            gcd, x, y = gcd_extended(a, b)
            print(f"НОД({a}, {b}) = {gcd}, x = {x}, y = {y}")

        elif choice == '3':
            e = int(input("Введите e: "))
            z = int(input("Введите z: "))
            try:
                inverse = modular_inverse(e, z)
                print(f"Инверсия {e} по модулю {z} = {inverse}")
            except ValueError as ve:
                print(ve)

        elif choice == '4':
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()
