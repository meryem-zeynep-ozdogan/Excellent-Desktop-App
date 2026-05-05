import sqlite3

print("Temizlik başlıyor...")
conn = sqlite3.connect('Database/invoices.db')
cursor = conn.cursor()

# Sadece en son eklenen 3000 gelir ve 3000 gider kalsın, gerisini sil (Toplam 6000 kayıt)
cursor.execute("DELETE FROM income_invoices WHERE id NOT IN (SELECT id FROM income_invoices ORDER BY id DESC LIMIT 3000)")
cursor.execute("DELETE FROM expense_invoices WHERE id NOT IN (SELECT id FROM expense_invoices ORDER BY id DESC LIMIT 3000)")
conn.commit()

print("Silme işlemi tamam. Dosya boyutu küçültülüyor (VACUUM)...")
cursor.execute("VACUUM") # Bu komut veritabanı dosyasının MB boyutunu da gerçekten küçültür
conn.close()

print("İşlem başarılı! Veritabanı tam 6000 kayda düşürüldü.")