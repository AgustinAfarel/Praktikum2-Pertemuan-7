# Praktikum2-Pertemuan-7
Dibuat untuk memenuhi tugas Bahasa Pemrograman

Nama  :Agustin Afarel

NIM   :312010081

Kelas :TI.20.B.1.

Matkul:Bahasa Pemrograman

### Menentukan Bilangan Terbesar dari 3 nilai yang diinputkan

Pada repository ini saya akan menjelaskan alur dalam *Flowchart* yang telah saya buat. File *Flowchart* bisa dilihat pada Link berikut ini :
[Flowchart-Pertemuan7.pdf](Flowchart-Pertemuan7.pdf)

Berikut source code yang saya tulis untuk menjadikan aplikasi tersebut. 

``` python
print("Masukan Angka ke-1 : ")
angka1 = int(input())
print("Masukan Angka ke-2 : ")
angka2 = int(input())
print("Masukan Angka ke-3 : ")
angka3 = int(input())

print("\n")

if (angka1 > angka2) and (angka1 > angka3) :
    print(f"Bilangan Pertama ({angka1}) Lebih Besar Dari Bilangan Kedua ({angka2}) dan Ketiga ({angka3})")

elif (angka2 > angka1) and (angka2 > angka3) :
    print(f"Bilangan Kedua ({angka2}) Lebih Besar Dari Bilangan Pertama ({angka1}) dan Ketiga ({angka3}) ")

elif (angka3 == angka1) and (angka3 == angka2) and (angka2 == angka3) :
    print("Bilangan Yang dimasukan sama besar ")
