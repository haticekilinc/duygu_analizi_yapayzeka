# Basit Duygu Analizi Uygulaması (IMDB Yorumları)

Bu proje, IMDB film yorumlarını kullanarak metin verilerinin duygusal tonunu (pozitif veya negatif) sınıflandıran basit bir makine öğrenmesi uygulamasıdır. Scikit-learn kütüphanesi ve Lojistik Regresyon algoritması kullanılarak geliştirilmiştir.

## Giriş

Bu uygulama, verilen bir film yorumunun olumlu mu yoksa olumsuz mu olduğunu tahmin etmek için temel bir Doğal Dil İşleme (NLP) örneğidir. Amaç, makine öğrenmesi tekniklerini kullanarak metin verilerinden duygu çıkarımının nasıl yapılabileceğini göstermektir.

## Kullanım

1.  **Gerekli Bağımlılıkları Yükleyin:**
    ```bash
    pip install pandas scikit-learn
    ```

2.  **IMDB Veri Setini İndirin:**
    [IMDB Dataset of 50K Movie Reviews](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews) adresinden `IMDB Dataset.csv` dosyasını indirin ve scriptinizle aynı dizine kaydedin.

3.  **Scripti Çalıştırın:**
    ```bash
    python python_duygu_analizi_imdb.py
    ```

4.  **Yorum Girin:**
    Uygulama çalıştıktan sonra, analiz etmek istediğiniz film yorumunu girmeniz istenecektir. Sonucu ekranda göreceksiniz. Çıkmak için 'q' tuşuna basın.

    ```
    IMDB Duygu Analizi Uygulaması
    ------------------------------
    Analiz etmek istediğiniz film yorumunu girin (çıkmak için 'q'): This movie was fantastic!
    Yorumun Duygusu: pozitif
    Analiz etmek istediğiniz film yorumunu girin (çıkmak için 'q'): I really disliked this film.
    Yorumun Duygusu: negatif
    Analiz etmek istediğiniz film yorumunu girin (çıkmak için 'q'): q
    ```

## Teknolojiler

* Python 3
* Pandas
* Scikit-learn

## Veri Seti

Bu proje, 50.000 adet İngilizce film yorumu içeren IMDB veri setini kullanmaktadır. Veri seti, her yorum için duygu etiketini ('positive' veya 'negative') içerir.

* **Kaynak:** [IMDB Dataset of 50K Movie Reviews (Kaggle)](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)
* **İçerik:** `review` (film yorumu metni) ve `sentiment` (pozitif veya negatif).

## Geliştirme

Bu proje gelecekte aşağıdaki şekillerde geliştirilebilir:

* Farklı makine öğrenmesi modellerini (örneğin, Naive Bayes, SVM) denemek ve performanslarını karşılaştırmak.
* Metin ön işleme adımlarını (örneğin, stop words kaldırma, lemmatization) iyileştirmek.
* Modelin doğruluğunu artırmak için daha fazla özellik mühendisliği yapmak.
* Basit bir web arayüzü (örneğin, Flask veya Streamlit ile) ekleyerek kullanıcı etkileşimini artırmak.

## Katkıda Bulunma

Katkılarınız memnuniyetle karşılanır. Lütfen aşağıdaki adımları izleyerek projeye katkıda bulunmaktan çekinmeyin:

1.  Projeyi fork edin.
2.  Kendi branch'inizi oluşturun (`git checkout -b feature/yeni-ozellik`).
3.  Değişikliklerinizi commit edin (`git commit -m 'Yeni özellik eklendi'`).
4.  Branch'inizi push edin (`git push origin feature/yeni-ozellik`).
5.  Pull request gönderin.

## Lisans

Bu proje [MIT Lisansı](LICENSE) altında lisanslanmıştır.

##Yazar

https://github.com/haticekilinc
