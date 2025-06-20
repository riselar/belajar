import os


folder_name = "muhamad_rifki"
os.makedirs(folder_name, exist_ok=True)


file_name = "muhamad_rifki.txt"
file_path = os.path.join(folder_name, file_name)


biodata = """Nama               : Muhamad Rifki Maulana
NIM                : 20240040166
Jurusan            : Teknik Informatika
Universitas        : Universitas Nusa Putra
tanggal lahir      : 15 juni 2005
"""


with open(file_path, "w", encoding="utf-8") as file:
    file.write(biodata)

print(f"File '{file_name}' berhasil dibuat di folder '{folder_name}'")
