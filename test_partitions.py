import pytest
from datetime import datetime

# --- EXCELLENT UYGULAMASI MOCK (TAKLİT) FONKSİYONLARI ---

# 1. Tutar Kontrolü (Hatalı: Negatif değere izin veriyor)
def current_excellent_parse_amount(amount):
    return float(str(amount).replace(',', '.'))

# 2. Tarih Kontrolü (Doğru: Python datetime kütüphanesi hatalı tarihi affetmez)
def current_excellent_parse_date(date_str):
    return datetime.strptime(date_str, "%d/%m/%Y")

# 3. Kur Kontrolü (Doğru: TCMB'de olmayan bir kur gelirse hata fırlatır)
def current_excellent_check_currency(currency_code):
    valid_currencies = ["USD", "EUR", "TRY", "GBP"]
    if currency_code not in valid_currencies:
        raise ValueError(f"Bilinmeyen para birimi: {currency_code}")
    return True

# --- TEST SENARYOLARI (TC-EP-01'den TC-EP-08'e) ---

@pytest.mark.parametrize("test_id, domain, input_data, expected_result, should_raise_error", [
    # Tutar (Amount) Bölümlemeleri
    ("TC-EP-01", "amount", "500.00", 500.0, False),
    ("TC-EP-02", "amount", "-100", None, True),      # HATA BEKLİYORUZ (Ama kod hata vermeyecek -> FAILED)
    ("TC-EP-03", "amount", "0", 0.0, False),
    ("TC-EP-04", "amount", "abc", None, True),       # HATA BEKLİYORUZ (Kod hata verecek -> PASSED)
    
    # Tarih (Date) Bölümlemeleri
    ("TC-EP-05", "date", "15/04/2026", True, False), # Geçerli tarih
    ("TC-EP-06", "date", "31/02/2026", None, True),  # İmkansız tarih, hata bekliyoruz -> PASSED
    
    # Para Birimi (Currency) Bölümlemeleri
    ("TC-EP-07", "currency", "USD", True, False),    # Geçerli kur
    ("TC-EP-08", "currency", "XYZ", None, True),     # Geçersiz kur, hata bekliyoruz -> PASSED
])
def test_all_equivalence_partitions(test_id, domain, input_data, expected_result, should_raise_error):
    if should_raise_error:
        with pytest.raises(ValueError):
            if domain == "amount": current_excellent_parse_amount(input_data)
            elif domain == "date": current_excellent_parse_date(input_data)
            elif domain == "currency": current_excellent_check_currency(input_data)
    else:
        if domain == "amount":
            assert current_excellent_parse_amount(input_data) == expected_result
        elif domain == "date":
            assert bool(current_excellent_parse_date(input_data)) == expected_result
        elif domain == "currency":
            assert current_excellent_check_currency(input_data) == expected_result