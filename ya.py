n = int( input( 'n = ' ) )
k = int( input( 'k = ' ) )
m, rest = divmod( n, k )
#print (m)
#print (rest)
li = []
for i in range(rest):
    li.append( m+1 )
    #print(li)
for i in range( k-rest ):
    li.append(m)
    #print(li)
print( f'Разбиение массива длиной {n} на {k} подмассивов с длинами:' )
print(li)