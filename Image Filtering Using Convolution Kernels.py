import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

print("Silahkan pilih efek yang diinginkan...","\n")
print("a. Tanpa efek","\n")
print("b. Penentuan tepi pada gambar","\n")
print("c. Penajaman gambar","\n")
print("d. Pengaburan gambar","\n")
jawaban=(input('Masukkan pilihan efek yang diinginkan : '))
jawaban=jawaban.lower()


if jawaban!='a' and jawaban!='b' and jawaban!='c' and jawaban!='d':
    print('Tidak ada efek yang tersedia')
    jawaban=(input('Masukkan pilihan efek yang diinginkan : '))

print("Silahkan pilih bagian gambar yang akan dikenakan efek...","\n")
print("1. Seluruh gambar","\n")
print("2. Satu bagian gambar","\n")
sisi=(input('Masukkan nomor bagian yang diinginkan : '))

if sisi!='1' and sisi!='2':
    print('Input tidak valid!')
    sisi=(input('Masukkan nomor bagian yang diinginkan : '))
    
im=Image.open('cadbury.jpg')
im.convert("RGB")
matriksgambar=np.array(im)
(Nx,Ny,M)=matriksgambar.shape

if jawaban=='a':
    kernel=np.array([[0,0,0],[0,1,0],[0,0,0]])
elif jawaban=='b':
    kernel=np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
elif jawaban=='c':
    kernel=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
elif jawaban=='d':
    kernel=np.array([[1,1,1],[1,1,1],[1,1,1]])

div=np.sum(kernel)

if div==0:
   div=1
imfil = matriksgambar.copy()

if sisi== '1':
    for j in range(0, M):
        for row in range(1, Nx - 1):
            for column in range(1, Ny - 1):
                a = 0
                for b in range(-1, 2):
                    for k in range(-1, 2):
                        a += matriksgambar[row + b, column + k, j] * kernel[b + 1, k + 1]
                        imfil[row, column, j] = max(min(round(a / div), 255), 0)
                       

elif sisi == '2':
    for j in range(0, M):
        for row in range(1, Nx//3):
            for column in range(1, Ny//3):
                a = 0
                for b in range(-1, 2):
                    for k in range(-1, 2):
                        a += matriksgambar[row + b, column + k, j] * kernel[b + 1, k + 1]
                        imfil[row, column, j] = max(min(round(a / div), 255), 0)
                

plt.imshow(imfil)
plt.show()