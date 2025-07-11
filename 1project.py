def caching_fibonacci():
    #Створюємо словник для збереження вже обчислених значень
    cache={}
    def fibonacci(n):
        #Базові випадки
        if n <=0:
            return 0
        elif n==1:
            return 1
        
        # Повертаємо значеня з того кешу якщо воно вже є
        elif n in cache:
            return cache[n]
        #Обчислюємо це фібоначі та повертаємо саму функцію
        cache[n]= fibonacci(n-1) + fibonacci(n-2)
        return cache[n]
    return fibonacci

# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
