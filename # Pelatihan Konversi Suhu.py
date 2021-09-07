# Tampilkan menu
print()
print("--Pelatihan Program Konversi Suhu--")
print("1. Celcius \t=> Fahrenheit")
print("2. Celcius \t=> Kelvin")
print("3. Celcius \t=> Reamur")
print("4. Fahrenheit \t=> Celcius")
print("5. Fahrenheit \t=> Kelvin")
print("6. Fahrenheit \t=> Reamur")
print("7. Kelvin \t=> Celcius")
print("8. Kelvin \t=> Fahrenheit")
print("9. Reamur \t=> Celcius")
print("10. Reamur \t=> Fahrenheit")
print()

# Terima pilihan user
pilihan = input("silahkan pilih menu diatas: ")

#kondisi berdasarkan pilihan user
if pilihan == "1":
    formatAwal = " C"
    formatAkhir = " F"
    nilaiAwal = int(input("masukan nilai celcius: "))
    nilaiAkhir = (nilaiAwal * 9/5) + 32
elif pilihan == "2":
    formatAwal = " C"
    formatAkhir = " K"
    nilaiAwal = int(input("masukan nilai celcius: "))
    nilaiAkhir = nilaiAwal + 273.15
elif pilihan == "3":
    formatAwal = " C"
    formatAkhir = " R"
    nilaiAwal = int(input("masukan nilai celcius: "))
    nilaiAkhir = nilaiAwal * 4/5
elif pilihan == "4":
    formatAwal = " F"
    formatAkhir = " C"
    nilaiAwal = int(input("masukan nilai Fahrenheit: "))
    niliAkhir = (nilaiAwal - 32) * 5/9
elif pilihan == "5":
    formatAwal = " F"
    formatAkhir = " K"
    nilaiAwal = int(input("masukan nilai Fahrenheit: "))
    nilaiAkhir = (nilaiAwal - 32)  * 5/9 + 273.15
elif pilihan == "6":
    formatAwal = " F"
    formatAkhir = " R"
    nilaiAwal = int(input("masukan nilai Fahrenheit: "))
    nilaiAkhir = (nilaiAwal - 32) * 4/9
elif pilihan == "7":
    formatAwal = " K"
    formatAkhir = " C"
    nilaiAwal = int(input("masukan nilai kelvin: "))
    nilaiAkhir = nilaiAwal - 273.15
elif pilihan == "8":
    formatAwal = " K"
    formatAkhir = " F"
    nilaiAwal = int(input("masukan nilai kelvin: "))
    nilaiAkhir = (nilaiAwal - 273.15) * 9/5 + 32
elif pilihan == "9":
    formatAwal = " R"
    formatAkhir = " C"
    nilaiAwal = int(input("masukan nilai Reamur: "))
    nilaiAkhir = nilaiAwal * 5/4
elif pilihan == "10":
    formatAwal = " R"
    formatAkhir = " F"
    nilaiAwal = int(input("masukan nilai Reamur: "))
    nilaiAkhir = (nilaiAwal + 32) * 9/4

# Tampilkan hasil
    print(str(nilaiAwal) + formatAwal + " = " + str(nilaiAkhir) +  formatAkhir)
