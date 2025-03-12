# main.py
from app.algorithms import modular_exponentiation, gcd_extended, modular_inverse

def get_int_input(mpt, min_value=None):
    """Функция для безопасного ввода целого числа."""
    while True:
        try:
            value = int(input(mpt))
            if min_value is not None and value < min_value:
                print(f"Ошибка: число должно быть не меньше {min_value}.")
                continue
            return value
        except ValueError:
            print("Ошибка: введите целое число.")

def main():
    while True:
        print("\nВыберите операцию:")
        print("1. Возведение в степень по модулю (a^x mod p)")
        print("2. Вычисление НОД (a, b)")
        print("3. Вычисление инверсии (e mod z)")
        print("4. Выход")

        choice = input("Введите номер операции: ").strip()

        if choice == '1':
            a = get_int_input("Введите a: ")
            x = get_int_input("Введите x (неотрицательное число): ", min_value=0)
            p = get_int_input("Введите p (больше 0): ", min_value=1)
            result = modular_exponentiation(a, x, p)
            print(f"{a}^{x} mod {p} = {result}")

        elif choice == '2':
            a = get_int_input("Введите a: ")
            b = get_int_input("Введите b (не должно быть 0): ")
            while b == 0:
                print("Ошибка: b не может быть 0.")
                b = get_int_input("Введите b: ")
            gcd, x, y = gcd_extended(a, b)
            print(f"НОД({a}, {b}) = {gcd}, x = {x}, y = {y}")

        elif choice == '3':
            e = get_int_input("Введите e: ")
            z = get_int_input("Введите z (больше 1): ", min_value=2)
            try:
                inverse = modular_inverse(e, z)
                print(f"Инверсия {e} по модулю {z} = {inverse}")
            except ValueError as ve:
                print(f"Ошибка: {ve}")

        elif choice == '4':
            print("Выход из программы.")
            break

        else:
            print("Ошибка: неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()
