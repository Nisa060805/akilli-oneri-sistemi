import pandas as pd
import numpy as np
import requests  # 1. ÖNEMLİ: Bu kütüphaneyi ekledik (Hortumumuz bu)
import os

class DataCleaner:
    def __init__(self):
        self.df = None

    # --- API LİNKİNİ KULLANAN ASIL FONKSİYON ---
    def load_from_api(self, api_url):
        print(f"🌐 Veri çekiliyor: {api_url}")
        try:
            # İnternete gidip veriyi alıyoruz
            response = requests.get(api_url)
            if response.status_code == 200:
                json_data = response.json()
                # DummyJSON veriyi 'products' listesi içinde gönderir
                self.df = pd.DataFrame(json_data['products']) 
                print(f"✅ Başarılı! İnternetten {len(self.df)} adet gerçek ürün verisi çekildi.")
            else:
                print(f"❌ API Hatası! Kod: {response.status_code}")
        except Exception as e:
            print(f"❌ Bağlantı kurulamadı: {e}")

    def clean_data(self):
        """Görevdeki temizleme adımları: Eksik veri, veri türü ve aykırı değer."""
        if self.df is None: return None
        
        print("🧹 Temizlik ve analiz başlıyor...")
        
        # 1. Eksik Veri İşleme
        self.df.fillna({'brand': 'Bilinmiyor', 'category': 'Genel'}, inplace=True)
        
        # 2. Veri Türü Dönüşümü
        self.df['price'] = self.df['price'].astype(float)
        
        # 3. Aykırı Değer Tespiti (Outlier)
        # Fiyatı 2000'den büyük olan "uçuk" ürünleri (outlier) traşlayalım
        self.df['price'] = np.where(self.df['price'] > 2000, 2000, self.df['price'])
        
        print("✨ Veri tertemiz hale getirildi!")
        return self.df

# --- BURASI API LİNKİNİ EKLEDİĞİMİZ VE ÇALIŞTIRDIĞIMIZ YER ---
if __name__ == "__main__":
    cleaner = DataCleaner()
    
    # İŞTE O API LİNKİ BURADA:
    # Bu link gerçek bir e-ticaret test servisidir (DummyJSON)
    api_linki = "https://dummyjson.com/products" 
    
    # 1. İnternetten veriyi çek
    cleaner.load_from_api(api_linki)
    
    # 2. Veriyi temizle
    temiz_veri = cleaner.clean_data()
    
    # 3. Sonucu Gör (Düzgün çalışıyor mu kontrolü)
    if temiz_veri is not None:
        print("\n--- İNTERNETTEN GELEN VE TEMİZLENEN VERİLERİN ÖZETİ ---")
        # Sadece ilk 5 ürünü ve önemli sütunları gösterelim
        print(temiz_veri[['id', 'title', 'price', 'category']].head())