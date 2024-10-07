from rembg import remove
from PIL import Image
import io
import os

def remove_background(input_image_path, output_image_path):
    """Menghapus latar belakang dari gambar."""
    with open(input_image_path, 'rb') as input_file:
        input_data = input_file.read()

    output_data = remove(input_data)

    with open(output_image_path, 'wb') as output_file:
        output_file.write(output_data)
    print(f"Hasil gambar disimpan di: {output_image_path}")

def main():
    # Meminta pengguna untuk memasukkan path gambar
    input_image_path = input("Masukkan path gambar yang ingin dihapus latar belakangnya: ")
    
    # Cek apakah file ada
    if not os.path.isfile(input_image_path):
        print("File tidak ditemukan. Silakan masukkan path yang valid.")
        return

    # Menentukan path untuk menyimpan gambar hasil
    output_image_path = os.path.splitext(input_image_path)[0] + "_no_bg.png"

    # Menghapus latar belakang
    remove_background(input_image_path, output_image_path)

if __name__ == "__main__":
    main()
