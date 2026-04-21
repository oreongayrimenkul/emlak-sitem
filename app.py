from flask import Flask, render_template, request
import os

# Standart Flask yapısı: templates klasörünü otomatik tanır
app = Flask(__name__)

@app.route('/')
def ana_sayfa():
    # Artık 'templates/index.html' dosyasını arayacak
    return render_template('index.html')

@app.route('/kaydet', methods=['POST'])
def kaydet():
    ad = request.form.get('ad_soyad')
    tel = request.form.get('telefon')
    saat = request.form.get('saat') # Formdaki yeni saat alanını aldık
    
    # Verileri musteriler.txt dosyasına kaydeder
    with open("musteriler.txt", "a", encoding="utf-8") as f:
        f.write(f"Ad: {ad}, Tel: {tel}, Tercih Edilen Saat: {saat}\n")
    
    return "<h1>Bilgileriniz başarıyla kaydedildi! En kısa sürede size ulaşacağız.</h1><a href='/'>Siteye Geri Dön</a>"

if __name__ == '__main__':
    # Render'da çalışması için port ayarı
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
