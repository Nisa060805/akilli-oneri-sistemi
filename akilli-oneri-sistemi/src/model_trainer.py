import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from data_cleaner import DataCleaner # Daha önce yazdığımız temizleyiciyi çağırıyoruz

class RecommendationModel:
    def __init__(self):
        self.cleaner = DataCleaner()
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.df = None
        self.cosine_sim = None

    def prepare_data(self):
        """API'den veriyi çeker ve analiz için hazırlar."""
        api_url = "https://dummyjson.com/products"
        self.cleaner.load_from_api(api_url)
        self.df = self.cleaner.clean_data()
        
        if self.df is not None:
            # Ürün başlığı ve kategorisini birleştirerek bir 'özellik' metni oluşturuyoruz
            self.df['features'] = self.df['title'] + " " + self.df['category']
            print("✅ Veri modelleme için hazırlandı.")

    def train(self):
        """TF-IDF ve Cosine Similarity kullanarak modeli eğitir."""
        if self.df is None: return
        
        print("🧠 Model eğitiliyor (Vektörleştirme ve Benzerlik Analizi)...")
        # Metinleri sayılara (vektörlere) dönüştürüyoruz
        tfidf_matrix = self.vectorizer.fit_transform(self.df['features'])
        
        # Ürünler arasındaki benzerlik puanlarını hesaplıyoruz
        self.cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
        print("✨ Model başarıyla eğitildi!")

    def get_recommendations(self, product_title, top_n=3):
        """Belirli bir ürüne benzeyen en iyi N ürünü getirir."""
        try:
            # Aranan ürünün listedeki yerini (index) bul
            idx = self.df[self.df['title'] == product_title].index[0]
            
            # Bu ürünün diğer tüm ürünlerle olan benzerlik puanlarını al
            sim_scores = list(enumerate(self.cosine_sim[idx]))
            
            # Puanlara göre büyükten küçüğe sırala (kendisini listeden çıkar)
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
            sim_scores = sim_scores[1:top_n+1]
            
            # En benzer ürünlerin isimlerini getir
            product_indices = [i[0] for i in sim_scores]
            return self.df['title'].iloc[product_indices]
        except Exception as e:
            return f"❌ Hata: Ürün bulunamadı veya model eğitilmedi. {e}"

# --- TEST ETME ---
if __name__ == "__main__":
    rec_sys = RecommendationModel()
    rec_sys.prepare_data()
    rec_sys.train()
    
    # Örnek: 'Essence Mascara Lash Princess' alan birine ne önerelim?
    target_product = "Essence Mascara Lash Princess"
    print(f"\n🔎 '{target_product}' için öneriler:")
    oneriler = rec_sys.get_recommendations(target_product)
    print(oneriler)