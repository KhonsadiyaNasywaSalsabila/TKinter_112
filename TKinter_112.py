#Import Libraries
import tkinter as tk
from tkinter import messagebox

#Fungsi untuk memeriksa hasil input dan menampilkan hasil prediksi
def hasil_prediksi():
    try:
        for entry in entries:
            nilai = int(entry.get())
            if not (0 <= nilai <= 100):
                raise ValueError("Nilai harus antara 0 dan 100.")
        hasil_label.config(text="Prediksi Prodi: Teknologi Informasi")
    except ValueError as ve:
        messagebox.showerror("Input Error", "Pastikan semua input adalah angka antara 0 dan 100.")

#Membuat jendela utama aplikasi termasuk judul jendela, ukuran, dan warna latar belakang
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("500x600")
root.configure(bg="#A4DDED")

#Membuat label judul beserta dengan formatnya
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 17, "bold"), bg="#A4DDED")
judul_label.pack(pady=20)

#Membuat frame untuk menyimpan entri input beserta dengan formatnya
frame_input = tk.Frame(root, bg="#A4DDED")   
frame_input.pack(pady=10)

#Membuat 10 label dan entri input untuk memasukkan nilai mata pelajaran beserta dengan formatnya
entries = []
for i in range(10):
    label = tk.Label(frame_input, text=f"Nilai Mata Pelajaran {i + 1}:", font=("Arial", 12, "bold"), bg="#A4DDED")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
    entry = tk.Entry(frame_input, width=10, font=("Arial", 12))
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

#Membuat button hasil prediksi yang akan memunculkan isi dari fungsi hasil prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi, font=("Arial", 12), bg="#4A83A1")
prediksi_button.pack(pady=30)

#membuat label kosong untuk menampilkan hasil prediksi
hasil_label = tk.Label(root, text="", font=("Arial", 14, "italic", "bold"), fg="white", bg="#4A83A1")
hasil_label.pack(pady=20)

#Memulai loop untuk menjalankan GUI
root.mainloop()

