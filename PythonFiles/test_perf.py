import pytest
from backend import Backend

# Backend motorunu test için ayağa kaldırıyoruz
backend_instance = Backend()

def test_fatura_kayit_hizi(benchmark):
    # Kaydedilecek sahte test faturası (TC-PT-02 için Input Data)
    test_faturasi = {
        'fatura_no': 'PERF-TEST-001',
        'tarih': '12.04.2026',
        'firma': 'Test A.Ş.',
        'malzeme': 'Benchmark Ölçümü',
        'miktar': '1',
        'toplam_tutar': 5000.0,
        'birim': 'TL',
        'kdv_yuzdesi': 20.0
    }

    # benchmark aracı, bu kayıt işlemini arka arkaya çalıştırıp süresini ölçecek
    sonuc = benchmark(backend_instance.handle_invoice_operation, 'add', 'outgoing', test_faturasi)
    
    # İşlemin gerçekten başarılı olup olmadığını kontrol et
    assert sonuc == True