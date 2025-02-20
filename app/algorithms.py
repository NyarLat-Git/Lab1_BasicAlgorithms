# algorithms.py
def modular_exponentiation(a, x, p):
    """Возведение в степень по модулю. Бинарное возведение в степень
    https://www.youtube.com/watch?v=2V_zU4DNdvU&ab_channel=IgorMamay """
    result = 1
    while x > 0:
        if x % 2 == 1:  # Если x нечетное
            result = (result * a) % p
        a = (a * a) % p
        x //= 2  # Делим x на 2
    return result

def gcd_extended(a, b):
    """Обобщенный алгоритм Евклида для нахождения НОД и коэффициентов."""
    U = [a, 1, 0]
    V = [b, 0, 1]

    while V[0] != 0:
        q = U[0] // V[0]
        U, V = V, [U[0] - q * V[0]] + [U[i] - q * V[i] for i in range(1, 3)]
    
    return U[0], U[1], U[2]  # НОД, x, y

def modular_inverse(e, z):
    """Вычисление инверсии e по модулю z."""
    gcd, x, _ = gcd_extended(e, z)
    if gcd != 1:
        raise ValueError("Инверсия не существует, e и z не взаимно простые")
    return x % z  # Возвращаем положительное значение