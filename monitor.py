import psutil
import time
import sys

def find_excellent_process():
    # Çalışan Excellent uygulamasını bul
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            # frontend-sidebar.py çalıştıran python sürecini bul
            if 'python' in proc.info['name'].lower() and proc.info['cmdline'] and 'frontend-sidebar.py' in ' '.join(proc.info['cmdline']):
                return proc
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    return None

process = find_excellent_process()

if not process:
    print("HATA: Excellent uygulaması çalışmıyor! Önce arayüzü başlatın.")
    sys.exit()

print(f"--- EXCELLENT PERFORMANS MONİTÖRÜ BAŞLADI (PID: {process.pid}) ---")
print("Kaydı durdurmak için CTRL+C yapabilirsiniz.\n")

try:
    for i in range(60):  # 60 saniye boyunca ölçecek
        cpu = process.cpu_percent(interval=1)
        # Belleği MB cinsinden al
        mem = process.memory_info().rss / 1024 / 1024 
        print(f"[{i+1}. Saniye] CPU Kullanımı: %{cpu:.1f} | RAM Kullanımı: {mem:.1f} MB")
except KeyboardInterrupt:
    print("\nİzleme manuel olarak durduruldu.")