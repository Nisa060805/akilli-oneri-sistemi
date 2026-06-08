# VERİ TOPLAMA PLANI VE KAFKA ENTEGRASYONU TEKNİK NOTU

**Proje Adı:** Akıllı E-Ticaret Öneri Sistemi  
**Modül:** Veri Kaynakları ve Ham Veri Toplama Altyapısı  
**Görevi Hazırlayan:** Nisanur Kırtepe  

---

## 1. Potansiyel Açık Kaynak Veri Kaynakları
Sistemin başlangıç aşamasında eğitilmesi ve test edilmesi amacıyla aşağıdaki açık kaynaklı popüler e-ticaret veri setleri kullanılacaktır:
* **Amazon Product Reviews Dataset:** Kullanıcıların ürünlere verdiği puanlar, yazılı metin yorumları ve meta verileri (kategori, marka, fiyat vb.) içeren, öneri sistemlerinin eğitimi ve NLP (Doğal Dil İşleme) tabanlı analizler için sıkça kullanılan kapsamlı bir veri setidir.
* **UCI Machine Learning Repository (Online Retail):** Gerçek bir e-ticaret sitesinin fatura bazlı İngiltere merkezli satış verilerini içeren; sepet analizi (Market Basket Analysis), kullanıcı satın alım eğilimleri ve işbirlikçi filtreleme algoritmaları için ideal bir veri setidir.

---

## 2. Kullanıcı-Ürün Etkileşim Verisi Veri Şeması (Data Schema)
Gerçek zamanlı olarak toplanacak ham verilerin içermesi gereken minimum alanlar (fields) ve JSON formatı standartlaştırılmıştır:

```json
{
  "event_id": "evt_987654321",
  "timestamp": "2026-06-08T17:15:00Z",
  "user_id": "usr_45012",
  "product_id": "prod_8832",
  "category": "Elektronik > Aksesuar",
  "event_type": "click",
  "event_properties": {
    "rating": null,
    "price": 450.00,
    "duration_seconds": 12
  }
}
