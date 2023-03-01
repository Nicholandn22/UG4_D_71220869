a = input('Masukkan sekumpulan bilangan (pisahkan dengan koma): ')
def bilangan(b):
    b = (a).split(',')
    b.sort(key = lambda x: int(x))
    return b
c = bilangan(a)
print(f'Bilangan terkecil dari kumpulan bilangan yang di input adalah {c[0]}')
print(f'Bilangan terbesar dari kumpulan bilangan yang di input adalah {c[-1]}')