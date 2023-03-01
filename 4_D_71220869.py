a = input('Masukkan sekumpulan bilangan (pisahkan dengan koma): ')
def bilangan(b):
    b = (a).split(',')
    b.sort(key = lambda abc: int(abc))
    return b
c = bilangan(a)
print(f'Bilangan terbesar dari kumpulan bilangan yang di input adalah {c[-1]}')
print(f'Bilangan terkecil dari kumpulan bilangan yang di input adalah {c[0]}')