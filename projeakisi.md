

# GEREKSİNİM ANALİZİ DÖKÜMANI

**Proje Adı:** Akıllı E-Ticaret Öneri Sistemi

**Modül:** A/B Test Platformu ve Performans İzleme Araçları

**Görevi Hazırlayan:** Nisanur Kırtepe

---

## 1. A/B Test Platformu Fonksiyonel Gereksinimleri (FR)

Bu modül, sistemdeki öneri algoritmalarının (Collaborative Filtering vs. Content-Based Filtering) gerçek kullanıcılar üzerindeki başarısını ölçmek ve kıyaslamak amacıyla tasarlanacaktır.

* **FR-1.1: Kullanıcı Segmentasyonu (Segmentation)**
* Sistem, sisteme gelen kullanıcıları belirli kriterlere göre (coğrafi konum, geçmiş alışveriş sıklığı, cihaz tipi veya rastgele atanmış ID'ler) segmentlere ayırabilmelidir.


* **FR-1.2: Test Grupları Oluşturma (Dynamic Group Allocation)**
* Gelen trafik dinamik ve adil bir şekilde **Grup A (Kontrol Grubu - Eski Algoritma)** ve **Grup B (Varyant Grubu - Yeni Algoritma)** olarak ikiye bölünmelidir (Örn: %50 - %50 veya %80 - %20).
* Bir kullanıcı test süreci boyunca hep aynı grupta kalmalıdır (Session/Cookie veya User ID bazlı kalıcılık).


* **FR-1.3: Sonuç Analizi ve Metrik Takibi (A/B Analytics)**
* Her iki grubun **Tıklama Oranı (CTR - Click-Through Rate)**, **Sepete Ekleme Oranı** ve **Dönüşüm Oranı (Conversion Rate)** hesaplanmalıdır.
* Elde edilen sonuçların istatistiksel olarak anlamlı olup olmadığını doğrulamak için **p-value (p-değeri)** hesabı yapılmalıdır.



---

## 2. Performans İzleme Araçları Gereksinimleri (Monitoring)

Sistemin mikroservis mimarisinde (Kafka, Spark, Elasticsearch) stabil çalışıp çalışmadığını anlamak için kritik sistem metrikleri sürekli izlenmelidir.

### 2.1. İzlenecek Kritik Metrikler

* **Yanıt Süresi (Latency):** Öneri motorunun bir kullanıcıya öneri listesi üretirken harcadığı süre (milisaniye - ms cinsinden). Hedef: < 200ms.
* **Hata Oranları (Error Rates):** HTTP 500 hataları, Kafka veri kaybı/gecikmesi veya veri tabanı zaman aşımı (timeout) oranları.
* **Kaynak Kullanımı (Resource Utilization):** Spark ve Python uygulamalarının anlık CPU, RAM ve Disk kullanımı.
* **Veri Akış Hızı (Throughput):** Kafka üzerinden anlık akan log/etkinlik sayısı (event/second).

### 2.2. Verilerin Görselleştirilmesi (Data Visualization)

* Toplanan metrikler, sistem yöneticisinin görebileceği **Grafana** tarzı anlık grafiklere (Line Chart, Bar Chart) dönüştürülmelidir.
* Hata oranları belirli bir eşiği (%5) geçtiğinde sistem otomatik olarak **Alert (Uyarı)** üretmelidir.

---

## 3. UI/UX (Kullanıcı Arayüzü ve Deneyimi) Gereksinimleri

* **UI-3.1: Kontrol Paneli (Dashboard):** Yönetici paneli temiz, minimalist ve koyu/açık tema desteğine uygun olmalıdır. Sol menüde "A/B Testleri" ve "Sistem Performansı" sekmeleri yer almalıdır.
* **UI-3.2: Canlı Grafik Akışı:** Performans metrikleri sayfayı yenilemeye gerek kalmadan (WebSocket veya kısa aralıklı polling ile) canlı olarak güncellenmelidir.
* **UX-3.3: Kolay Test Yönetimi:** Yönetici, yeni bir A/B testi başlatırken karmaşık kodlar yazmak yerine, sadece bir buton yardımıyla trafik oranlarını (%50 - %50 vb.) kaydırıcı (slider) ile ayarlayabilmelidir.
* **UX-3.4: Hata Bildirimleri:** Kritik bir sistem hatası veya çökme durumunda, ekranın sağ üst köşesinde net ve kırmızı renkli (Pop-up/Toast) uyarı pencereleri belirmelidir.


