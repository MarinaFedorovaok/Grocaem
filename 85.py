
# Рекурсивная функция. Определить максимальный элемент списка
def GetMaxList(L):
    #print(len(L))
    if len(L)>1:
        # Получить максимум из следующих рекурсивных вызовов
        Max = GetMaxList(L[1:])
        # Сравнить максимум с первым элементом списка
        if L[0]<Max:
            return Max
        else:
            return L[0]
    if len(L)==1: # последний элемент в списке
        return L[0] # вернуть этот элемент

# Демонстрация использования функции Power()
L = [1, 3, 5]
res = GetMaxList(L)
print("res = ", res)

