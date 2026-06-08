Teknolojiler: Apache Kafka, Elasticsearch, PySpark Streaming

🏗️ 1. Mimari Tasarımı ve Bileşenler
Sistem, verinin oluştuğu andan öneriye dönüştüğü ana kadar dört ana katmandan oluşmaktadır:

Veri Toplama Katmanı (Kafka): Kullanıcının web sitesindeki her tıklaması, sepete eklemesi veya satın alımı bir "Event" (Olay) olarak Kafka Topic'lerine gönderilir.

Veri İşleme Katmanı (Spark Streaming): Kafka'dan gelen canlı veri akışı Spark tarafından anlık olarak yakalanır. Burada Muhammed Emir'in algoritmaları kullanılarak "Kullanıcı X ürününe baktı, o zaman Y ürününü sevebilir" hesaplaması yapılır.

Depolama ve Arama Katmanı (Elasticsearch): Hesaplanan öneriler ve ürün katalog verileri Elasticsearch üzerinde indekslenir. Elasticsearch'ün "Vector Search" yetenekleri sayesinde benzer ürünler milisaniyeler içinde bulunur.

Sunum Katmanı (API): Kullanıcı sayfayı yenilediğinde veya yeni bir ürüne baktığında, Elasticsearch'ten gelen en güncel öneriler kullanıcıya gösterilir.

🔄 2. Veri Akış Yönetimi (Data Pipeline)
Toplama: Kullanıcı etkileşimleri Kafka "User-Interactions" topic'inde toplanır.

İşleme: Spark, bu topic'i dinler; gelen veriyi temizler (Nisanur'un modülüyle uyumlu) ve anlık model tahmini yapar.

Depolama: Tahmin sonuçları Elasticsearch'te recommendations indeksine yazılır.

Sunma: Sistem, Elasticsearch'ten gelen veriyi kullanarak "Senin İçin Seçtiklerimiz" listesini anlık olarak günceller.

Gereksinim,Çözüm Yaklaşımı
Ölçeklenebilirlik,"Kafka ve Elasticsearch ""Distributed"" (Dağıtık) yapıda olduğu için veri miktarı arttıkça sisteme yeni düğümler (nodes) eklenerek kapasite kolayca artırılabilir."
Güvenilirlik,"Kafka'nın ""Replication"" özelliği sayesinde veri kaybı önlenir. Bir sunucu çökse bile veri diğer sunucularda saklanmaya devam eder."
Performans,"Elasticsearch'ün ""In-memory indexing"" yeteneği sayesinde, milyonlarca ürün arasından öneri getirme süresi 100ms'nin altında tutulur."
