# DDP LAB-3

# SOAL 1 - Gunting-Batu-Kertas
# Tuliskan program untuk Soal 1 di bawah ini
print("BATU, KERTAS, GUNTING")
print("Untuk Batu, Input 0")
print("Untuk Kertas, Input 1")
print("Untuk Gunting, Input 2")
suit = ["Batu", "Gunting", "Kertas"]
player1 = int(input("Masukkan pilihan Player-1 : "))
player2 = int(input("Masukkan pilihan Player-2 : "))
if player1 == 0 and player2 == 0:
  print("Pertandingan Seri")
elif player1 == 0 and player2 == 1:
  print("Player-1 Menang")
elif player1 == 0 and player2 == 2:
  print("Player-2 Menang")
elif player1 == 1 and player2 == 0:
  print("Player-2 Menang")
elif player1 == 1 and player2 == 1:
  print("Pertandingan Seri")
elif player1 == 1 and player2 == 2:
  print("Player-1 Menang")
elif player1 == 2 and player2 == 0:
  print("Player-1 Menang")
elif player1 == 2 and player2 == 1:
  print("Player-2 Menang")
elif player1 == 2 and player2 == 2:
  print("Pertandingan Seri")



# SOAL 2 - Toko Buku Bekas
# Tuliskan program untuk Soal 2 di bawah ini
buku = int(input("Masukkan total buku : "))
harga=0
if(buku<=10):
  harga=20000*buku
elif(buku >= 11) and (buku < 25):
  harga=18000*buku
elif(buku >= 26) and (buku < 50):
  harga=18000*buku  
elif(buku>50):
  harga=10000*buku

print ("Harga yang harus dibayar = ", harga, "rupiah")





# SOAL 3 - Mencetak Persegi
# Tuliskan program untuk Soal 3 di bawah ini
x = int(input("Masukkan sebuah bilangan bulat : "))
for i in range(x):
  if i % 2 == 0:
    print("# "*x)
  else:
    print("$ "*x)



