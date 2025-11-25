from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time
import os

os.system("cls" if os.name == "nt" else "clear")

print("\033[92m")  # warna hijau terang
print(r"""
  ___  ___ _  _  ___   ___  _      ___  ___ ___    _   ___ ___ ___ ___ 
 / __|/ __| || |/ _ \ / _ \| |    / __|/ __| _ \  /_\ | _ \ _ \ __| _ \
 \__ \ (__| __ | (_) | (_) | |__  \__ \ (__|   / / _ \|  _/  _/ _||   /
 |___/\___|_||_|\___/ \___/|____| |___/\___|_|_\/_/ \_\_| |_| |___|_|_\
""")

print("\033[91m[ CODED BY TSUNA ALEXANDRA ]\033[0m")  # merah
print("\033[94mComplete Scraper Tool :)\033[0m\n")  # biru

URL = "https://script.google.com/macros/s/AKfycbylN9rNXwLf9yBFj_qKCfhSuciNNeHYY-tVSsB_W-tgQzu-YcV2t5-zPwwregQJjjLWfA/exec"


def ambil_field(driver, name):
    """Ambil value dari input field berdasarkan atribut NAME"""
    try:
        return driver.find_element(By.NAME, name).get_attribute("value")
    except:
        return ""


def scrape_akun(nis, pw):
    print(f"\n=== Memproses NIS: {nis} ===")
    
    driver = webdriver.Chrome()
    driver.set_window_size(400, 500)
    driver.get(URL)

    wait = WebDriverWait(driver, 15)

    try:
        wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "sandboxFrame")))
        print("✔ Masuk iframe sandboxFrame")

        wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "userHtmlFrame")))
        print("✔ Masuk iframe userHtmlFrame")

    except Exception as e:
        print("❌ Gagal masuk iframe:", e)
        driver.quit()
        return

    time.sleep(5)

    try:
        driver.find_element(By.ID, "nis").send_keys(nis)
        driver.find_element(By.ID, "pasw").send_keys(pw)
    except:
        print("❌ Input NIS/PW gagal.")
        driver.quit()
        return

    try:
        driver.execute_script("cekData()")
        time.sleep(10)
    except:
        print("❌ Gagal menjalankan cekData()")
        driver.quit()
        return

    # ambil data
    data = {
        "Nama Lengkap": ambil_field(driver, "Nama Lengkap"),
        "Jenis Kelamin": ambil_field(driver, "Jenis Kelamin (L/P)"),
        "Tempat Lahir": ambil_field(driver, "Tempat Lahir"),
        "Tanggal Lahir": ambil_field(driver, "tgl_lahir"),
        "Bulan Lahir": ambil_field(driver, "bln_lahir"),
        "Tahun Lahir": ambil_field(driver, "thn_lahir"),

        "Status Dalam Keluarga": ambil_field(driver, "Status Dlm Keluarga"),
        "Anak ke": ambil_field(driver, "Anak ke-berapa (berdasarkan KK)"),
        "Jumlah Saudara Kandung": ambil_field(driver, "Jumlah Saudara Kandung"),
        "Asal SMP": ambil_field(driver, "Asal Sekolah SMP"),
        "Nomor Seri Ijazah": ambil_field(driver, "Nomor Seri Ijazah SMP"),
        "No.HP": ambil_field(driver, "No. HP"),

        "Email Aktif": ambil_field(driver, "Email Aktif"),
        "Hobi": ambil_field(driver, "Hobby"),
        "Cita-Cita": ambil_field(driver, "Cita-cita"),
        "NISN": ambil_field(driver, "NISN"),
        "NIK": ambil_field(driver, "NIK"),
        "NKK": ambil_field(driver, "No.KK"),

        "ABK": ambil_field(driver, "Berkebutuhan Khusus"),
        "Agama": ambil_field(driver, "Agama dan Kepercayaan"),
        "Alamat": ambil_field(driver, "Alamat Jalan"),
        "RT": ambil_field(driver, "RT"),
        "RW": ambil_field(driver, "RW"),
        "Dusun": ambil_field(driver, "Nama Dusun"),

        "Desa/Kelurahan": ambil_field(driver, "Desa/Kelurahan"),
        "Tinggal": ambil_field(driver, "Tempat Tinggal"),
        "Transportasi": ambil_field(driver, "Moda Transportasi"),
        "Penerima Bantuan": ambil_field(driver, "Penerima KPS/PKH"),
        "KIP": ambil_field(driver, "Apakah Punya KIP"),
        "PIP": ambil_field(driver, "Apakah menerima PIP (Ya/Tidak)"),

        "Tinggi": ambil_field(driver, "Tinggi Badan (cm)"),
        "Berat": ambil_field(driver, "Berat Badan (kg)"),
        "Lingkar Kepala": ambil_field(driver, "Lingkar Kepala"),
        "Jarak Rumah ke Sekolah": ambil_field(driver, "Jarak Rumah Ke Sekolah (m/km)"),
        "Waktu Tempuh Rumah ke Sekolah": ambil_field(driver, "Waktu Tempuh ke Sekolah (menit/jam)"),
        "Nama Ayah": ambil_field(driver, "Nama Ayah"),

        "NIK Ayah": ambil_field(driver, "NIK Ayah"),
        "Tahun Lahir Ayah": ambil_field(driver, "Tahun Lahir Ayah"),
        "Pendidikan Ayah": ambil_field(driver, "Pendidikan Terakhir Ayah"),
        "Pekerjaan Ayah": ambil_field(driver, "Pekerjaan Ayah"),
        "Penghasilan Ayah": ambil_field(driver, "Penghasilan Ayah"),
        "Ayah BK": ambil_field(driver, "Berkebutuhan Khusus Ayah"),

        "Nama Ibu": ambil_field(driver, "Nama Ibu"),
        "NIK Ibu": ambil_field(driver, "NIK Ibu"),
        "Tahun Lahir Ibu": ambil_field(driver, "Tahun Lahir Ibu"),
        "Pekerjaan Ibu": ambil_field(driver, "Pekerjaan Ibu"),
        "Penghasilan Ibu": ambil_field(driver, "Penghasilan Ibu"),
        "Pendidikan Ibu": ambil_field(driver, "Pendidikan Terakhir Ibu"),

        "Ibu BK": ambil_field(driver, "Ibu ( Berkebutuhan Khusus )"),
        "Nama Wali": ambil_field(driver, "Nama Wali"),
        "NIK Wali": ambil_field(driver, "NIK Wali"),
        "Tahun Lahir Wali": ambil_field(driver, "Tahun Lahir Wali"),
        "Pendidikan Wali": ambil_field(driver, "Pendidikan Terakhir Wali"),
        "Pekerjaan Wali": ambil_field(driver, "Pekerjaan Wali"),

        "Wali BK": ambil_field(driver, "Berkebutuhan Khusus Wali"),
        "Penghasilan Wali": ambil_field(driver, "Penghasilan Wali"),
    }

    driver.quit()

    # nama file dari nama lengkap
    raw_name = data.get("Nama Lengkap", nis)
    safe_name = "".join(c for c in raw_name if c.isalnum() or c in " _-").strip()
    safe_name = safe_name.replace(" ", "_")
    filename = f"{safe_name}.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"✔ Selesai → {filename}")



print("Input Path (contoh: C:/Users/kamu/akun.txt)")
path = input("Path file: ").strip()

if not os.path.exists(path):
    print("❌ File tidak ditemukan! Pastikan path benar.")
    exit()

with open(path, "r", encoding="utf-8") as f:
    akun_list = [line.strip().split(",") for line in f if "," in line]

print(f"\nTotal akun ditemukan: {len(akun_list)}")

for nis, pw in akun_list:
    scrape_akun(nis, pw)

print("\n=== Semua akun selesai di-scrape ===")
