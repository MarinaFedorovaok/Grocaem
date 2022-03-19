n = int( input( 'n = ' ) )
k = int( input( 'k = ' ) )
m, rem = divmod( n, k )
print (m)
print (rem)
res = []
for i in range(rem):
    res.append( m+1 )
    print(res)
for i in range( k-rem ):
    res.append(m)
    print(res)
print( f'Разбиение массива длиной {n} на {k} подмассивов с длинами:' )
print(res)