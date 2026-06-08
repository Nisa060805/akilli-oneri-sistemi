# model_evaluation.py
# Hazırlayan: Nisanur Kırtepe

import numpy as np

def calculate_metrics(actual_purchases, recommended_items):
    """
    Öneri sistemi için Precision, Recall ve F1-Score hesaplayan fonksiyon.
    
    actual_purchases: Kullanıcının gerçekten satın aldığı/beğendiği ürün ID listesi
    recommended_items: Modelimizin kullanıcıya önerdiği ilk N ürün ID listesi
    """
    # Kesişim kümesi: Önerilen ürünlerden kaç tanesi gerçekten satın alındı?
    true_positives = len(set(actual_purchases) & set(recommended_items))
    
    # 1. Precision (Kesinlik): Önerilen ürünlerin ne kadarı başarılı?
    if len(recommended_items) == 0:
        precision = 0.0
    else:
        precision = true_positives / len(recommended_items)
        
    # 2. Recall (Duyarlılık): Alınan ürünlerin ne kadarını tahmin edebildik?
    if len(actual_purchases) == 0:
        recall = 0.0
    else:
        recall = true_positives / len(actual_purchases)
        
    # 3. F1-Score: Precision ve Recall'un harmonik ortalaması
    if (precision + recall) == 0:
        f1_score = 0.0
    else:
        f1_score = 2 * (precision * recall) / (precision + recall)
        
    return precision, recall, f1_score

# --- ÖRNEK SİMÜLASYON VE TEST VERİSİ ---
if __name__ == "__main__":
    print("==================================================")
    print("  AKILLI E-TİCARET ÖNERİ SİSTEMİ MODEL DEĞERLENDİRME ")
    print("==================================================\n")

    # Senaryo: Kullanıcı gerçekte 5 ürün almış olsun.
    # Modelimiz de bu kullanıcıya 5 tane ürün önersin.
    gercek_alinanlar = [101, 102, 105, 108, 110]
    model_onerileri  = [101, 103, 105, 107, 109] # 101 ve 105 başarılı eşleşme

    print(f"Kullanıcının Gerçekte Satın Aldığı Ürünler : {gercek_alinanlar}")
    print(f"Sistemin Kullanıcıya Önerdiği Ürünler    : {model_onerileri}\n")

    # Metrikleri Hesapla
    p, r, f1 = calculate_metrics(gercek_alinanlar, model_onerileri)

    # Sonuçları Ekrana Yazdır
    print("-" * 50)
    print(f"🎯 Precision (Kesinlik) : %{p * 100:.1f}")
    print(f"🔍 Recall (Duyarlılık)  : %{r * 100:.1f}")
    print(f"⚖️  F1-Score            : %{f1 * 100:.1f}")
    print("-" * 50)

    # Kısa Bir Yorumlama Metni (Hocanın rapor beklentisi için)
    print("\n📝 METRİK YORUMLARI:")
    print(f"1. Precision (%{p * 100:.1f}): Model tarafından önerilen her 5 üründen {int(p*5)} tanesi kullanıcı tarafından ilgi görmüştür.")
    print(f"2. Recall (%{r * 100:.1f}): Kullanıcının satın alacağı ürünlerin %{r * 100:.1f}'ini modelimiz önceden yakalamayı başarmıştır.")
    print(f"3. F1-Score (%{f1 * 100:.1f}): Dengeli başarı oranımız %{f1 * 100:.1f} seviyesindedir. Model eşikleri optimize edilmelidir.")
    

