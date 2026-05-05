import sqlite3
import random
import os
from datetime import datetime, timedelta

def generate_mock_data():
    db_path = os.path.join(os.getcwd(), 'Database')
    if not os.path.exists(db_path):
        os.makedirs(db_path)
        
    invoices_db = os.path.join(db_path, 'invoices.db')
    
    conn = sqlite3.connect(invoices_db)
    cursor = conn.cursor()
    
    # Check tables exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS income_invoices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fatura_no TEXT,
            irsaliye_no TEXT,
            tarih TEXT,
            firma TEXT,
            malzeme TEXT,
            miktar TEXT,
            matrah REAL DEFAULT 0.0,
            toplam_tutar_tl REAL,
            toplam_tutar_usd REAL,
            toplam_tutar_eur REAL,
            birim TEXT,
            kdv_yuzdesi REAL,
            kdv_tutari REAL,
            kdv_dahil INTEGER DEFAULT 0,
            usd_rate REAL,
            eur_rate REAL,
            updated_at TEXT,
            created_at TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expense_invoices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fatura_no TEXT,
            irsaliye_no TEXT,
            tarih TEXT,
            firma TEXT,
            malzeme TEXT,
            miktar TEXT,
            matrah REAL DEFAULT 0.0,
            toplam_tutar_tl REAL,
            toplam_tutar_usd REAL,
            toplam_tutar_eur REAL,
            birim TEXT,
            kdv_yuzdesi REAL,
            kdv_tutari REAL,
            kdv_dahil INTEGER DEFAULT 0,
            usd_rate REAL,
            eur_rate REAL,
            updated_at TEXT,
            created_at TEXT
        )
    """)
    
    # Try adding matrah column if they were created before we checked
    try:
        cursor.execute("ALTER TABLE income_invoices ADD COLUMN matrah REAL DEFAULT 0.0")
    except:
        pass
        
    try:
        cursor.execute("ALTER TABLE expense_invoices ADD COLUMN matrah REAL DEFAULT 0.0")
    except:
        pass
        
    conn.commit()
    
    companies = ["Acme Corp", "Tech Solutions", "Global Trading", "Meka Inc.", "Atlas Lojistik", "Özkan A.Ş."]
    materials = ["Hizmet", "Lisans", "Danışmanlık", "Sunucu", "Donanım", "Hosting"]
    units = ["Adet", "Saat", "Paket", "Ay"]
    kdv_rates = [0.0, 1.0, 10.0, 20.0]
    
    start_date = datetime(2023, 1, 1)
    
    def generate_random_date():
        random_days = random.randint(0, 365*2) # Within last 2 years
        return (start_date + timedelta(days=random_days)).strftime("%Y-%m-%d")
        
    def generate_record(prefix, i):
        fatura_no = f"{prefix}2023{str(i).zfill(6)}"
        irsaliye_no = ""
        tarih = generate_random_date()
        firma = random.choice(companies)
        malzeme = random.choice(materials)
        miktar = str(random.randint(1, 100))
        matrah = round(random.uniform(100.0, 10000.0), 2)
        kdv_yuzdesi = random.choice(kdv_rates)
        kdv_tutari = round(matrah * (kdv_yuzdesi / 100.0), 2)
        toplam_tutar_tl = matrah + kdv_tutari
        usd_rate = round(random.uniform(28.0, 32.0), 4)
        toplam_tutar_usd = round(toplam_tutar_tl / usd_rate, 2)
        eur_rate = round(random.uniform(30.0, 34.0), 4)
        toplam_tutar_eur = round(toplam_tutar_tl / eur_rate, 2)
        birim = random.choice(units)
        kdv_dahil = 0
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        return (
            fatura_no, irsaliye_no, tarih, firma, malzeme, miktar, matrah,
            toplam_tutar_tl, toplam_tutar_usd, toplam_tutar_eur, birim,
            kdv_yuzdesi, kdv_tutari, kdv_dahil, usd_rate, eur_rate, now_str, now_str
        )
        
    print("Generating 20,000 Income Invoices...")
    income_records = [generate_record("GEL", i) for i in range(1, 20001)]
    cursor.executemany("""
        INSERT INTO income_invoices (
            fatura_no, irsaliye_no, tarih, firma, malzeme, miktar, matrah,
            toplam_tutar_tl, toplam_tutar_usd, toplam_tutar_eur, birim,
            kdv_yuzdesi, kdv_tutari, kdv_dahil, usd_rate, eur_rate, updated_at, created_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, income_records)
    
    print("Generating 20,000 Expense Invoices...")
    expense_records = [generate_record("GID", i) for i in range(1, 20001)]
    cursor.executemany("""
        INSERT INTO expense_invoices (
            fatura_no, irsaliye_no, tarih, firma, malzeme, miktar, matrah,
            toplam_tutar_tl, toplam_tutar_usd, toplam_tutar_eur, birim,
            kdv_yuzdesi, kdv_tutari, kdv_dahil, usd_rate, eur_rate, updated_at, created_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, expense_records)
    
    conn.commit()
    conn.close()
    print("Successfully inserted 40,000 mock records.")

if __name__ == '__main__':
    generate_mock_data()
