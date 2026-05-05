import sqlite3
import glob

# Proje içindeki tüm .db uzantılı veritabanlarını bul
db_dosyalari = glob.glob('**/*.db', recursive=True)

if not db_dosyalari:
    print("Hiç .db dosyası bulunamadı!")

for db_yolu in db_dosyalari:
    print(f"\n--- Veritabanı Bulundu: {db_yolu} ---")
    try:
        conn = sqlite3.connect(db_yolu)
        cursor = conn.cursor()
        
        # Tablo isimlerini otomatik bul
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tablolar = cursor.fetchall()
        
        for tablo in tablolar:
            tablo_adi = tablo[0]
            # Satır sayılarını say
            cursor.execute(f"SELECT COUNT(*) FROM {tablo_adi}")
            sayi = cursor.fetchone()[0]
            print(f"Tablo: '{tablo_adi}' -> Kayıt Sayısı: {sayi}")
            
        conn.close()
    except Exception as e:
        print(f"Okunurken hata oluştu: {e}")