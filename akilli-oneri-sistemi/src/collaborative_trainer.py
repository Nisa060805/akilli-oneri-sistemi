import pandas as pd
import numpy as np
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics import mean_squared_error
from math import sqrt

# 1. Veri Setini Hazırlama (Simüle Edilmiş Kullanıcı Etkileşimleri)
# Gerçek projede bu veri API veya Veritabanından gelir.
data = {
    'user_id': [1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5],
    'product_id': [101, 102, 105, 101, 103, 102, 104, 101, 104, 105, 103, 105],
    'rating': [5, 4, 1, 4, 5, 2, 4, 5, 5, 4, 4, 5]
}

df = pd.DataFrame(data)

# 2. Kullanıcı-Ürün Matrisini Oluşturma (Pivot Table)
interaction_matrix = df.pivot_table(index='user_id', columns='product_id', values='rating').fillna(0)
print("--- Kullanıcı-Ürün Etkileşim Matrisi ---")
print(interaction_matrix)

# 3. Matrix Factorization (SVD) Uygulama
# n_components: Gizli özellikleri temsil eder (Örn: ürünün fiyatı, popülerliği vb.)
svd = TruncatedSVD(n_components=2, random_state=42)
matrix_low_dim = svd.fit_transform(interaction_matrix)

# Matrisi geri oluşturarak eksik puanları tahmin etme
predicted_ratings = np.dot(matrix_low_dim, svd.components_)
df_predictions = pd.DataFrame(predicted_ratings, columns=interaction_matrix.columns, index=interaction_matrix.index)

print("\n--- Tahmin Edilen Puan Matrisi ---")
print(df_predictions.round(2))

# 4. Performans Değerlendirme (RMSE)
# Gerçek puanlar ile tahmin edilenler arasındaki hata payı
mse = mean_squared_error(interaction_matrix, predicted_ratings)
rmse = sqrt(mse)
print(f"\n📊 Model Performansı (RMSE): {rmse:.4f}")

def get_cf_recommendations(user_id, top_n=2):
    user_row = df_predictions.loc[user_id]
    # Kullanıcının daha önce etkileşime girdiği ürünleri eleyebiliriz
    recommendations = user_row.sort_values(ascending=False).head(top_n)
    return recommendations

# Test: 2 numaralı kullanıcı için öneri üret
print(f"\n🚀 Kullanıcı 2 için Öneriler:\n{get_cf_recommendations(2)}")