# Protogen: Gelişmiş Yapay Zeka Sohbet Robotu

## 🤖 Proje Genel Bakış

Protogen, modern yapay zeka teknolojilerini kullanan makine öğrenimi bir sohbet robotu projesidir. Bu proje, doğal dil işleme, makine öğrenmesi ve çoklu dil desteği gibi gelişmiş özelliklere sahip bir Telegram chatbot'u olarak tasarlanmıştır.

## ✨ Özellikler

### 1. Çoklu Dil Desteği
- Farklı dillerdeki mesajları otomatik olarak İngilizceye çevirme
- Dil tanıma ve çeviri mekanizması

### 2. Gelişmiş Sinir Ağı Mimarisi
- Dinamik öğrenme mekanizması
- Kelime gömme (word embedding) teknolojisi
- Esnek nöral ağ yapısı
  - Giriş katmanı: 1000 nöron
  - Gizli katman: 500 nöron
  - Çıkış katmanı: 1000 nöron

### 3. Bellek Yönetimi
- Kullanıcı bağlamını saklama
- Öğrenilen cümlelerin ve kelime desenlerinin kaydedilmesi
- Kalıcı hafıza mekanizması

### 4. Kural Motoru
- Önceden tanımlanmış kurallara göre yanıt üretme
- Yüksek güvenilirlikli yanıtlar sağlama

## 🛠 Teknolojiler

- Python 3.8+
- NumPy
- python-telegram-bot
- Telegram API
- SQLite (Hafıza Yönetimi)

## 📦 Kurulum

### Gereksinimler
- Python 3.8 veya üzeri
- pip paket yöneticisi

### Adım Adım Kurulum
1. Depoyu klonlayın:
   ```bash
   git clone https://github.com/kullanici_adi/protogen.git
   cd protogen
   ```

2. Sanal ortam oluşturun:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows için: venv\Scripts\activate
   ```

3. Gerekli bağımlılıkları yükleyin:
   ```bash
   pip install -r requirements.txt
   ```

4. Telegram bot tokenınızı `.env` dosyasına ekleyin:
   ```
   TELEGRAM_BOT_TOKEN=sizin_telegram_bot_tokeniniz
   ```

## 🚀 Kullanım

Botu çalıştırmak için:
```bash
python bot.py
```

## 📂 Proje Dizin Yapısı

- `bot.py`: Ana bot sınıfı ve Telegram entegrasyonu
- `neural_network.py`: Özel sinir ağı implementasyonu
- `memory_manager.py`: Kullanıcı bağlamı ve hafıza yönetimi
- `language_processor.py`: Dil tanıma ve işleme
- `translator.py`: Çeviri mekanizması
- `rules_engine.py`: Kural tabanlı yanıt sistemi
- `training_data.txt`: Ön eğitim verileri

## 🤝 Katkıda Bulunma

1. Fork yapın
2. Yeni bir dal (branch) oluşturun: `git checkout -b ozellik/harika-eklenti`
3. Değişikliklerinizi kaydedin: `git commit -m 'Harika bir özellik ekledim'`
4. Dalınızı gönderin: `git push origin ozellik/harika-eklenti`

## 🔒 Güvenlik

- Bot tokeni çevre değişkenlerinden yüklenir
- Hassas bilgiler `.env` dosyasında saklanır
- Kullanıcı verileri güvenli bir şekilde işlenir

## 📝 Lisans

Bu proje GPL-3.0 Lisansı altında yayınlanmıştır. Detaylar için LICENSE dosyasına bakın.

## 🐛 Sorun Bildirim

Herhangi bir hata veya öneri için [GitHub Issues](https://github.com/Stixyie/Machine-Learning-Chatbot/issues) sayfasını kullanabilirsiniz.

## 🌟 Teşekkür

- Telegram Bot API
- NumPy Geliştirme Ekibi
- Açık kaynak topluluğuna
