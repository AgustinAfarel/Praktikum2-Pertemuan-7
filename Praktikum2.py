# INPUT 3 BUAH BILANGAN, MENGGUNAKAN STATMENT IF
print("menentukan bilangan terbesar dari 3 bilangan")

print("Masukan Bilangan Ke-1 : ")
bilangan1=int(input())
print("Masukan Bilangan Ke-2 : ")
bilangan2=int(input())
print("Masukan Bilangan Ke-3 : ")
bilangan3=int(input())

print('\n')

if ( bilangan1>bilangan2 ) and ( bilangan1 > bilangan3 ) :
    print("bilangan 1 lebih besar dari bilangan 2 dan 3")
elif ( bilangan2 > bilangan1 ) and ( bilangan2 > bilangan3 ) :
    print("bilangan 2 lebih besar dari bilangan 1 dan 3")
elif ( bilangan3 > bilangan1 ) and ( bilangan3 > bilangan2 ) :
    print ("bilangan 3 lebih besar dari bilangan 1 dan 2")
else :
    print("semua bilangan sama besarnya")
