# Akıllı E-Ticaret Öneri Sistemi

## Proje Açıklaması
Bu projede kullanıcıların alışveriş davranışlarını analiz eden ve kişiselleştirilmiş ürün önerileri sunan bir öneri sistemi geliştirilecektir.

---

## Hafta 1 – Veri Seti Keşfi

### Yapılan Çalışmalar
- Kullanıcı verileri incelendi
- Ürün verileri analiz edildi
- Kullanıcı davranış verileri değerlendirildi

### Veri Analizi
- Veri seti büyüklüğü incelendi
- Eksik veriler kontrol edildi
- Aykırı değerler araştırıldı

### Veri Ön İşleme Planı
- Eksik verilerin düzenlenmesi
- Veri temizleme işlemleri
- Kategorik verilerin sayısallaştırılması

🛠️ 1. Hafta: Geliştirme Ortamı ve Altyapı Kurulum Raporu 🚀
Sorumlu: Mehmet Ali Kırımlı (Öğrenci No: 250542027)
Tarih: 11 Mart 2026

💻 1. Proje Başlatma ve Ortam Hazırlığı
Projenin ilk aşamasında, ekip üyelerinin farklı donanımlarda bile aynı kod çıktılarını alabilmesini sağlayan "izole ve standart bir geliştirme ortamı" hedeflenmiştir.

IDE Seçimi: Geliştirme arayüzü olarak VS Code tabanlı ve yapay zeka ajan desteğine sahip Antigravity tercih edilmiştir. Bu araç, karmaşık kurulum süreçlerini otomatize etmek için kullanılmıştır.

Klasör Mimarisi: Yazılım mühendisliği prensiplerine uygun, modüler bir dizin yapısı oluşturulmuştur:

📂 data/raw/: Nisanur'un bulacağı ham veri setleri için.

📂 src/models/: Muhammed Emir'in geliştireceği algoritmalar için.

📂 notebooks/: Deneysel analizler ve Jupyter çalışmaları için.

📂 venv/: Proje bağımlılıklarını izole eden sanal ortam.

📦 2. Kütüphaneler ve Bağımlılık Yönetimi
Sistem bağımlılıklarının çakışmaması ve "benim bilgisayarımda çalışıyor" sorununu önlemek için bir Python Sanal Ortamı (venv) yapılandırılmıştır. Temel teknolojiler şu sürümlerle sisteme entegre edilmiştir:

Kütüphane	Versiyon	Görev
Pandas 🐼	v2.3.3	Veri manipülasyonu ve Nisanur'un veri keşfi süreci için temel araçtır.
Scikit-learn 🧠	v1.7.2	Muhammed Emir'in araştıracağı makine öğrenimi modellerinin eğitilmesi için kurulmuştur.
PySpark ⚡	v4.1.1	Projenin "Gerçek Zamanlı Öneri Motoru" kısmındaki büyük veri işleme kapasitesini sağlar.

E-Tablolar'a aktar

✅ 3. Sistem Doğrulama (Smoke Test)
Kurulumun ardından sistemin uçtan uca (end-to-end) çalışabilirliğini denetlemek adına test_health.py isimli bir "Duman Testi" (Smoke Test) uygulanmıştır.

Veri Analizi Testi: Pandas DataFrame yapıları hatasız bir şekilde oluşturulmuş ve işlenmiştir.

Yapay Zeka Testi: Scikit-learn üzerinden örnek bir model başarıyla eğitilmiş ve doğru tahminler üretilmiştir.

Büyük Veri Testi: Spark Session sorunsuz bir şekilde başlatılmış ve veri sayımı (count) gerçekleştirilmiştir.

Sonuç: Terminal üzerinde "System Healthy" çıktısı alınarak tüm bileşenlerin entegre bir şekilde çalıştığı somut olarak kanıtlanmıştır.

🏁 4. Versiyon Kontrol ve İş Birliği
Proje, Nisanur Kırtepe tarafından yönetilen GitHub reposu üzerinden takip edilmektedir. Hazırlanan altyapı kodları ve bağımlılık listesi (requirements.txt), repo ile senkronize edilmeye hazır durumdadır.

Durum: 🟢 Geliştirme ortamı ekip arkadaşları için tamamen hazırdır.
