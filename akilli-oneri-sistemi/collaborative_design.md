👥 5. Hafta: İşbirlikçi Filtreleme (Collaborative Filtering) Tasarımı

Sorumlu: Mehmet Ali Kırımlı

Seçilen Yöntem: Matrix Factorization (SVD)Kütüphane: Scikit-learn

📑 1. Yaklaşım KarşılaştırmasıSistem gereksinimleri doğrultusunda yapılan araştırmada; kullanıcılar arası benzerliğin hesaplanmasının (User-based) veri seti büyüdüğünde yavaşlayacağı, matris ayrıştırmanın (SVD) ise gizli özellikleri daha iyi yakaladığı saptanmıştır.

📐 2. Matematiksel ModelKullanıcı-Ürün matrisi ($R$), üç alt matrise ayrılarak analiz edilmiştir:$$R \approx U \Sigma V^T$$Burada $U$ kullanıcı özelliklerini, $V$ ise ürün özelliklerini temsil eden gizli vektörleri ifade eder.

📈 3. Performans DeğerlendirmesiModelin doğruluğunu ölçmek için RMSE (Root Mean Square Error) metriği kullanılmıştır. Yapılan prototip testlerinde elde edilen düşük RMSE değeri, sistemin kullanıcı tercihlerini tahmin etme yeteneğinin yüksek olduğunu kanıtlamaktadır.