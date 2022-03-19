#таблица умножения элементов массива
my_list = [1, 3, 5, 7, 8, 9]
def multiplication (li):
    for i in range(2, len(li)+2):
        for n in li:
            print (n*i)
        print('************')        


multiplication(my_list)
