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


🗄️ 3. Hafta: Veritabanı Mimarisi ve Veri Modelleme Raporu 📊
Sorumlu: Mehmet Ali Kırımlı (Öğrenci No: 250542027)
Son Teslim Tarihi: 28 Mart 2026
Öncelik Durumu: 🟡 Orta

🎯 1. Görevin Amacı ve Kapsamı
Bu hafta odak noktamız, akıllı e-ticaret öneri sisteminin temelini oluşturacak olan veritabanı yapısının tasarlanmasıdır. Sistem; kullanıcı davranışlarını analiz edip kişiselleştirilmiş öneriler sunabilmek için yüksek performanslı ve ilişkisel bir veri modeline ihtiyaç duymaktadır.

📐 2. Veri Modeli ve Tablo Yapıları (ER Tasarımı)
Sistemimiz, etkili bir öneri motoru için üç ana tablo üzerine inşa edilmiştir:

👤 Kullanıcılar (Users) Tablosu
Sisteme kayıtlı kullanıcıların demografik ve tercih verilerini tutar.

user_id (Primary Key): Benzersiz kullanıcı numarası.

user_name: Kullanıcı adı/tanımlayıcı.

location: Bölgesel öneriler için lokasyon verisi.

joined_at: Kullanıcı kayıt tarihi.

📦 Ürünler (Products) Tablosu
Katalogdaki tüm ürünlerin detaylarını içerir.

product_id (Primary Key): Benzersiz ürün numarası.

product_name: Ürün ismi.

category: Nisanur'un veri setiyle uyumlu kategori bilgisi.

price: Ürün fiyatı.

🔄 Etkileşimler (Interactions) Tablosu
Sistemin "zekasını" oluşturan, kullanıcı ve ürün arasındaki bağı kuran tablodur.

interaction_id: İşlem numarası.

user_id (Foreign Key): İşlemi yapan kullanıcı.

product_id (Foreign Key): Etkileşime girilen ürün.

interaction_type: Etkileşim türü (View, Add to Cart, Purchase).

timestamp: İşlemin gerçekleştiği an.

⚡ 3. Teknik Entegrasyon ve Performans Planı
Veritabanı tasarımı, kurduğumuz teknoloji yığınıyla (Spark, Elasticsearch) tam uyumlu olacak şekilde planlanmıştır:

İndeksleme (Indexing): Arama hızını optimize etmek için user_id ve product_id sütunları üzerinde indeksleme yapılarak sorgu süreleri minimize edilmiştir.

Spark Entegrasyonu: PySpark 4.1.1 kullanılarak, veritabanındaki büyük etkileşim tabloları "Batch" veya "Stream" yöntemiyle işlenerek algoritma eğitimine hazır hale getirilecektir.

Elasticsearch Senkronizasyonu: Ürün tablosu, milisaniyeler içinde arama ve filtreleme yapılabilmesi için Elasticsearch'e "Index" olarak aktarılacaktır.

✅ 4. 3. Hafta Çıktıları ve Mevcut Durum
Veritabanı Şeması: Tamamlandı.

İlişki Tanımlamaları: Tamamlandı.

Veri Entegrasyon Planı: Hazırlandı.

Not: Bu veritabanı yapısı, Muhammed Emir'in araştırdığı "Collaborative Filtering" ve "Content-based Filtering" algoritmalarının ihtiyaç duyduğu tüm veri tiplerini desteklemektedir.

Durum: 🟢 Veritabanı tasarımı aşaması, yazılım geliştirme sürecine entegre edilmeye hazırdır.
