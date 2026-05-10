import streamlit as st
from model_trainer import RecommendationModel

# 1. Sayfa Ayarları
st.set_page_config(page_title="Akıllı Öneri Sistemi", layout="wide")
st.title("🛍️ Akıllı E-Ticaret Öneri Sistemi")

# 2. Modeli Başlat (Önbelleğe alarak hızı artırıyoruz)
@st.cache_resource
def load_system():
    rec_sys = RecommendationModel()
    rec_sys.prepare_data()
    rec_sys.train()
    return rec_sys

system = load_system()

# 3. Kullanıcı Arayüzü
st.sidebar.header("Kullanıcı Paneli")
product_list = system.df['title'].values
selected_product = st.selectbox("Bir ürün seçin veya aratın:", product_list)

if st.button("Önerileri Getir"):
    with st.spinner('Sizin için en uygun ürünler seçiliyor...'):
        oneriler = system.get_recommendations(selected_product)
        
        st.subheader(f"'{selected_product}' Ürününü Sevenler Bunları da Beğendi:")
        
        # Önerileri yan yana sütunlar halinde göster
        cols = st.columns(3)
        for i, urun in enumerate(oneriler):
            with cols[i]:
                st.success(urun)
                # Buraya gerçek bir e-ticaret sitesinde ürün görseli ve fiyatı gelirdi