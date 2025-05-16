import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# IMDB veri setini yükleme (veri setinin bulunduğu yolu kendi dosya yolunuzla değiştirin)
imdb_df = pd.read_csv('IMDB Dataset.csv')

# Duygu etiketlerini sayısal değerlere dönüştürme (positive: 1, negative: 0)
imdb_df['sentiment'] = imdb_df['sentiment'].map({'positive': 1, 'negative': 0})

# Metin ve duygu etiketlerini ayırma
metinler = imdb_df['review']
duygular = imdb_df['sentiment']

# Veri setini eğitim ve test kümelerine ayırma
egitim_metin, test_metin, egitim_duygu, test_duygu = train_test_split(metinler, duygular, test_size=0.2, random_state=42)

# TF-IDF vektörleştiricisini oluşturma ve eğitim verisine uygulama
tfidf_vektorizator = TfidfVectorizer(max_features=5000, stop_words='english') # Daha fazla özellik
egitim_vektorler = tfidf_vektorizator.fit_transform(egitim_metin)
test_vektorler = tfidf_vektorizator.transform(test_metin)

# Lojistik Regresyon modelini oluşturma ve eğitme
model = LogisticRegression(random_state=42)
model.fit(egitim_vektorler, egitim_duygu)

# Test kümesi üzerinde tahmin yapma
tahminler = model.predict(test_vektorler)

# Modelin doğruluğunu değerlendirme
dogruluk = accuracy_score(test_duygu, tahminler)
print(f"Modelin Doğruluğu (IMDB Veri Seti): {dogruluk:.2f}")

def duygu_analizi_yap_imdb(metin, vektorizator, model):
    """Verilen metnin duygusunu tahmin eder (IMDB modeli)."""
    metin_vektor = vektorizator.transform([metin])
    tahmin = model.predict(metin_vektor)[0]
    return 'pozitif' if tahmin == 1 else 'negatif'

if __name__ == "__main__":
    print("\nIMDB Duygu Analizi Uygulaması")
    print("------------------------------")
    while True:
        girilen_metin = input("Analiz etmek istediğiniz film yorumunu girin (çıkmak için 'q'): ")
        if girilen_metin.lower() == 'q':
            break
        duygu = duygu_analizi_yap_imdb(girilen_metin, tfidf_vektorizator, model)
        print(f"Yorumun Duygusu: {duygu}")