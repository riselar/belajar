try:
    skor = int(input("Masukkan skor (0-100): "))

    if skor < 0 or skor > 100:
        print("Skor tidak valid!")
    else:
        if skor >= 90:
            nilai = "A"
            predikat = "Kerja bagus, pertahankan!"
        elif skor >= 80:
            nilai = "B"
            predikat = "Sangat Memuaskan"
        elif skor >= 70:
            nilai = "C"
            predikat = "Memuaskan"
        elif skor >= 60:
            nilai = "D"
            predikat = "Tidak Memuaskan"
        else:
            nilai = "E"
            predikat = "Tidak LULUS"

        print(f"Nilai   : {nilai}")
        print(f"Predikat: {predikat}")

except ValueError:
    print("Input harus berupa angka bulat (integer)!")
