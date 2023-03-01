print('=============== BARIS ARITMATIKA ===============')
def aritmatika(a,b,c):
    hasil = float(c/2 * ((2*a) + (b*(c-1))))
    return hasil
a = int(input('Masukkan bilangan awal : '))
b = int(input('Masukkan selisih bilangan  : ')) 
c = int(input('Masukkan banyaknya suku  : ')) 

hasiltotal = aritmatika(a, b, c)
print(f'Total dari deret aritmatika tersebut adalah : {hasiltotal}')