
Algoritma Yaklaşımı: İçerik Tabanlı Filtreleme (Content-Based Filtering)

📊 1. Modelin Çalışma Prensibi ve Matematiksel AltyapıSistem, ürünlerin metinsel özelliklerini analiz ederek kullanıcıya en alakalı sonuçları sunmak üzere tasarlanmıştır. Eğitim sürecinde şu teknik adımlar uygulanmıştır:TF-IDF Vektörleştirme: Ürün başlıkları ve kategorileri, kelime frekanslarına dayalı sayısal vektörlere dönüştürülmüştür.Kosinüs Benzerliği (Cosine Similarity): İki ürün arasındaki anlamsal yakınlığı belirlemek için vektörler arasındaki açı hesaplanmıştır:$$\text{similarity} = \cos(\theta) = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\| \|\mathbf{B}\|}$$

✅ 2. Eğitim Sonuçları ve Doğrulama (Success Evidence)model_trainer.py üzerinden yapılan testlerde, sistemin çapraz kategori etkileşimlerini ve anlamsal benzerlikleri başarıyla kavradığı kanıtlanmıştır.

Girdi Ürün (Input)ㅤㅤㅤÖnerilen Ürün-1ㅤㅤㅤÖnerilen Ürün-2ㅤㅤㅤㅤÖnerilen Ürün-3

Essence MascaraㅤㅤㅤRed LipstickPowderㅤㅤCanisterEyeshadowㅤㅤㅤㅤPalette

Performans Notları:Veri Kaynağı: Canlı API üzerinden 30 adet gerçek e-ticaret ürünü işlenmiştir.Uyum Oranı: Önerilen tüm ürünler "Beauty" kategorisinde kalmış ve makyaj seti tamamlayıcı ürünler olarak seçilmiştir.Hız: Model eğitimi ve öneri üretimi milisaniyeler seviyesinde gerçekleşmiştir.

📈 3. Gelecek Planı ve MetriklerModelin başarısını daha bilimsel verilerle desteklemek için bir sonraki aşamada şu metrikler takip edilecektir:Precision@K: Önerilen ilk 3 ürünün doğruluk oranı.RMSE (Root Mean Square Error): Tahmin edilen ilgi düzeyi ile gerçek veri arasındaki sapma miktarı.

Durum: 🟢 Model eğitildi, doğrulandı ve üretim ortamına (production) aktarılmaya hazır hale getirildi.
