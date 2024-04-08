import math

print("=====================================================")
print("============== Matematika Menyenangkan ==============")
print("=====================================================")
print("       ")
print("Matematika merupakan mata pelajaran yang menyenangkan")
print("       ")
print("Hallo semuanya, apa kabar kalian?")
print("Semoga kalian baik-baik saja yah,....")

Nama_peserta = str(input("Nama anda siapa? "))
Nama_panggilan = str(input("Nama panggilannya bre/sis? "))
tanggal_lahir = input("Masukkan tanggal lahir (dd-mm-yyyy) : ")
hari, bulan, tahun = tanggal_lahir.split("-")
Kelas = str(input("Kelas anda? "))
Jurusan = str(input("Jurusan anda apa bre/sis? "))

print("     ")

print("Oke,", str(Nama_panggilan))
print("Sekarang kita akan belajar mengenai bangun datar yah, ", str(Nama_panggilan))
print("      \n ")
print("Lihat materi pembelajaran yang ada di bawah ini. Pilih salah satu: ")
print("1. Segitiga")
print("2. Persegi panjang")
print("3. Persegi")
print("4. Lingkaran")
print("5. Trapesium")
print("6. Layang-layang")

materi_pembelajaran = str(input("Pilihlah materi mathlab di sini : "))

if materi_pembelajaran == "Segitiga":
   print("       ")
   print("Oke, saatnya belajar tentang segitiga")
   print("       ")
   print("Apakah kamu tahu mengenai segitiga? ")
   pertanyaan = str(input("Jawab (iya/tidak) : "))
   if pertanyaan == "iya":
      print("Oke, kamu sudah mengetahui dari awal yah, bagus untukmu")
      print("Baiklah, apa yang kamu ketahui tentang segitiga? ")
      pertanyaan_2 = str(input("Silahkan jawab di sini : "))
   elif pertanyaan == "tidak":
      print("      ")
      print("Sudah saatnya anda harus memahami bangun datar. Hari ini kita akan mempelajari tentang segitiga ")

      print("      ")
      print("Apa itu segitiga? ")
      print("Segitiga merupakan salah satu dari tiap bangun datar yang memiliki 3 sudut, memiliki")
      print("siku-siku dan berbentuk sudut lancip. Untuk menghitung luas segitiga perlu diketahui")
      print("bahwa segitiga memiliki alas dan tinggi. Dengan 2 unsur tersebut, dapat diketahui bahwa")
      print("untuk menghitung luas segitiga, kalkulasi antara alas dan tinggi dan dibagi 2, sehingga")
      print("menghasilkan setengah dikali alas dikali tinggi. ")
      print("Rumusnya adalah : ")
      print("0.5 * alas * tinggi atau alas * tinggi / 2")
      print("       ")
   
      pertanyaan_3 = str(input("Apakah anda mengerti? "))
      if pertanyaan_3 == "iya":                      
         input("Bagus, kamu sudah bisa menguasainya, sekarang cobalah memasukkan nilai di bawah ini")
      elif pertanyaan_3 == "tidak":
         input("Coba pelajari lagi")
   
   input("Saatnya memasukkan data mengenai alas dan tingginya suatu segitiga, cobalah di sini : ")

   class bangun_datar: 
      def Segitiga(Alas, Tinggi): 
         return Alas * Tinggi / 2
      Alas = int(input("Masukkan nilai alas : "))
      Tinggi = int(input("Masukkan nilai tinggi : "))
      Luas = int(Alas) * int(Tinggi) / 2
      print("Jadi, Luas segitiga adalah", float(Luas), "cm")
      print("Baiklah, kita cukupkan sampai di sini, terima kasih atas interaksinya yah,...")

elif materi_pembelajaran == "Persegi panjang":
   print("Oke, kita akan belajar mengenai persegi panjang")
   print("    ")
   question_1 = str(input("Apakah kamu tahu mengenai persegi panjang? "))
   if question_1 == "iya":
      print("Baiklah, kamu sudah mempelajari mengenai persegi panjang")
      print("Apa yang anda ketahui mengenai persegi panjang? ")
      question_2 = str(input("Jawaban : "))
      print("Baiklah, anda sudah mempelajari tentang persegi panjang.")
      print("Sekarang, anda coba masukkan nilai panjang dan lebar di bawah ini : ")
   elif question_1 == "tidak":
      print("Baiklah, di sini akan menjelaskan pemabahasan mengenai persegi panjang.")
      print("     ")
      print("Persegi panjang merupakan  salah satu bangun datar yang memiliki 4 sudut")
      print("yang di mana, 2 sudutnya mewakili sisi panjang, sedangkan 2 sudut lainnya")
      print("mewakili sis lebarnya. Apabila kita ingin mencari luasnya, cukup gampang,")
      print("caranya dengan mengalikan sisi lebar dan panjang. Kita bisa memaparkan rumus ini: ")
      print("     ")
      print("Luas Persegi panjang : panjang * lebar")
      question_3 = str(input("Apakah anda sudah mengerti? "))
      if question_3 == "iya":
         input("oke, bagus. Saatnya anda memasuki nilai panjang dan lebar di bawah ini : ")
      elif question_3 == "tidak":
         input("Baca lagi dann pahami lagi")
      else: 
         print("Mohon kembali")
      
      class bangun_datar:
         def Persegi_panjang(Panjang, Lebar):
            return Panjang * Lebar 
   
         Panjang = int(input("Masukkan nilai Panjang : "))
         Lebar = int(input("Masukkan nilai lebar : "))
         Luas = int(Panjang) * int(Lebar)
         print("Jadi, luasnya adalah", str(Luas), "cm")
         print("Begitulah luasnya persegi panjang, semoga bermanfaat")

elif materi_pembelajaran == "Persegi":
   print("Oke, kita akan belajar mengenai persegi")
   print("      ")
   print("Apakah kamu tahu mengenai persegi? ")
   tanya_jawab = str(input("Jawab (iya/tidak) : "))
   if tanya_jawab == "iya":
      print("Oke, bagus untukmu")
      print("    ")
      tanya_jawab_1 = str("Apa yang kamu tau tentang persegi? ")
   elif tanya_jawab == "tidak":
      print("Oke, di sini anda akan mempelajari tentang persegi")
      print("    ")
      print("Persegi merupakan salah satu bangun datar yang memiliki sisi yang sama")
      print("walaupun memiliki 4 sudut. Luas dari persegi adalah hasil perkalian antar sisi. ")
      print("Persegi memiliki rumus luasnya tersendir, yakni: ")
      print("    ")
      print("Rumus luas persegi: sisi * sisi")
      print("     ")
      tanya_jawab_2 = str(input("Apakah anda paham? "))
      if tanya_jawab_2 == "iya":
         print("Baiklah, langsung ke intinya aja, mari coba memasukkan nilai sis di sini: ")
      elif tanya_jawab_2 == "tidak":
         print("Silahkan coba pelajari kembali yah,...")
      print("Silahkan mencoba")

   class bangun_datar:
      def Persegi(sisi):
         return sisi * sisi
      sisi = int(input("Masukkan nilai sisi : "))
      Luas = int(sisi) * int(sisi)
      print("Jadi, luasnya adalah", str(Luas), "cm")
      print("Begitulah persegi, dengan sisi yang sama membuat orang dapat mencari luasnya ddengan mudah")

elif materi_pembelajaran == "Lingkaran":
   print("oke, kita akan belajar mengenai lingkaran")
   print("      ")
   print("Apakah kamu tahu tentang lingkaran? ")
   QNA_0 = str(input("Jawab (iya/tidak) : "))
   if QNA_0 == "iya":
      print("Oke, itu nilai yang bagus untukmu")
      Jawaban = str(input("Apa yang kamu ketahui mengenai lingkaran? "))
   elif QNA_0 == "tidak":
      print("Oke, di sini akan menampilkan dan mengajarkan tentang lingkaran dan luasnya.")
      print("     ")
      print("Lingkaran adalah salah satu abngun datar yang tidak memiliki sudut dan sisi, ")
      print("namun memiliki jari-jari dan diameter. Lingkaran sendiri membentuk 360 derajat")
      print("dan memiliki titik pusat di dalamnya. Di dalam bangun ruang, lingkaran ini terpakai")
      print("juga dengan kerucut dan silinder(tabung). Untuk mengetahui rumusnya, kita menggunakan unsur")
      print("pi yang diartikan ke dalam angka berarti sekitar 3.14 atau 22/7, mengalikan jari-jari 2 kali lipat ")
      print("      ")
      print("Rumus luas lingkaran : 3.14 * r * r")
      print("    ")

      QNA_1 = str(input("Apakah anda sudah mengerti? "))
      if QNA_1 == "iya":
         print("Kamu hebat sekali memahami rumus luas lingkaran.")
         print("Tidak jarang orang salah-salah dalam merepresentasikan rumus ini")
         input("Baiklah, sistem ini meminta anda untuk mencoba memasukkan nilai jari-jari berikut ini: ")
      else: 
         input("Oke, pelajari kembali")
   
   input("Saatnya menghitung luas lingkaran : ")
         
   class bangun_datar:
      def Lingkaran(r):
         return 3.14 * r * r
      r = int(input("Masukkan nilai r atau jari-jari: "))
      Luas = 3.14 * int(r) * int(r) 
      print("Jadi, luas lingkaran adalah", float(Luas), "cm")
   
   print("Begitulah luas lingkaran, tanpa sudut pun lingkaran memiliki luas dengan adanya diameternya")

elif materi_pembelajaran == "Trapesium":
   print("Oke kita akan belajar mengenai trapesium")
   tanya_1 = str(input("Apakah anda mengenal bangun datar yang satu ini? "))
   if tanya_1 == "iya":
      print("Oke, kamu mengetahui atau mengenalnya dengan baik.")
      print("    ")
      input("Apa yang kamu ketahui tentang Trapesium")
   elif tanya_1 == "tidak":
      print("Oke, kamu belum mengetahuinya dengan baik. Di sini akan menjelaskan tentang trapesium")
      print("    ")
      kalimat_1 = "Trapesium adalah salah satu dari banyaknya bangun ruang yang memiliki alas dan tinggi yang memiliki 4 sudut. "
      kalimat_2 = "Untuk menemukan luas, kita tinggal menambahakan 2 alas dan mengalikan tinggi trapesium, lalu dibagi 2."
      kalimat_3 = "Rumusnya yaitu 0.5 * (Alas_a + Alas_b) * tinggi"
      kombinasi_kalimat = kalimat_1 + "\n" + kalimat_2 + "\n" + "\n" + kalimat_3
      print(kombinasi_kalimat)
      tanya_2 = str(input("Apakah anda mengerti? "))
      if tanya_2 == "iya":
         input("Bagus, sekarang kita akan mencoba memasukkan nilai berikut ini: ")
      else: 
         print("Belajar lah lagi")

   class bangun_datar:
      def Trapesium(Tinggi, A1, A2):
         return 0.5 * (A1 + A2) * Tinggi
      Tinggi = int(input("Masukkan nilai tinggi = "))
      A1= int(input("Masukkan nilai alas-a = "))
      A2 = int(input("Masukkan nilai alas b = "))
      Luas_trapesium = 0.5 * (A1 + A2) * Tinggi 
      print("Luas trapesium adalah", str(Luas_trapesium), "cm")
      print("Begitulah cara kerja untuk mencari luas trapesium, semoga bermanfaat")

elif materi_pembelajaran == "Layang-layang":
   print("Oke, kita akan belajar mengenai layang-layang \n")
   pengenalan = str(input("Apakah anda pernah bermain layang-layang? "))
   if pengenalan == "iya":
      gambaran = input("Bagus, layang-layang yang kamu mainkan seperti apa bentuknya? ")
      print("Oke, kamu sudah mengerti yah, sekarang kita akan mencoba memasukkan data-datanya : ")
   elif pengenalan == "tidak":
      print("Baiklah, di sini akan menjelaskan mengenai layang-layang itu sendiri. \n")
      print("Layang-layang adalahayang-layang adalah bangun datar yang dibentuk oleh dua pasang sisi yang sama panjang dan saling berpotongan membentuk sudut \n ")
      print("Layang-layang juga merupakan turunan dari segi empat, dengan ciri khusus memiliki dua sisi yang sama panjang dan sudut yang berhadapan memiliki ukuran sama besar. ")
      print("Layang-layang ini memiliki 2 sisi diagonal dan memiliki 2 sisi yang sama panjang. ")
      print("Rumus luas layang-layang : 0.5 * D1 * D2")

      gambaran_1 = str(input("Apakah anda sudah mengerti? "))
      if gambaran_1 == "iya":
         print("oke kita lanjutkan memasukkan nilai-nilainya : ")
      elif gambaran_1 == "tidak":
         print("Belajarlah lagi")
         breakpoint
      
   class bangun_datar:
      def Layang_layang(AB, CD):
         return 0.5 * AB * CD
      AB = int(input("Masukkan nilai AB (diagonal-1) : "))
      CD = int(input("Masukkan nilai CD (diagonal-2) : "))
      input("Setelah kita dapatkan nilainya, kita eksekusi semua : ")
      input("0.5 * D1 * D2")
      Luas = 0.5 * int(AB) * int(CD)
      print("Jadi, luasnya adalah",  int(Luas), "cm")
else: 
   input("Pilihan anda salah, silahkan akses kembali")
    
print(breakpoint)
 