while True:
    print("===== Program Kalkulator Sederhana =======")
    print("Menu")
    print("1. Hitung Luas Segitiga")
    print("2. Hitung Luas Persegi Panjang")
    print("3. Tentukan number ganjil/genap")
    print("4. Quit")
    
    pilihan = input("Masukkan pilihan: ")
    
    if pilihan == "1":
        alas = float(input("Masukkan alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))
        luas = 0.5 * alas * tinggi
        print(f"Luas segitiga adalah: {luas}\n")

    elif pilihan == "2":
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))
        luas = panjang * lebar
        print(f"Luas persegi panjang adalah: {luas}\n")

    elif pilihan == "3":
        angka = int(input("Masukkan angka: "))
        if angka % 2 == 0:
            print(f"{angka} adalah bilangan genap.\n")
        else:
            print(f"{angka} adalah bilangan ganjil.\n")

    elif pilihan == "4":
        print("Terima kasih")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi\n")
