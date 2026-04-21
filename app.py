from flask import Flask, render_template, request
import os

app = Flask(__name__)

# --- AYARLAR ---
# Müşteri listesini göreceğin gizli linkin sonu. 
# Örn: sitenizin-adresi.onrender.com/ozel_musteri_paneli
PANEL_LINKI = "ozel_musteri_paneli" 

@app.route('/')
def ana_sayfa():
    return render_template('index.html')

@app.route('/kaydet', methods=['POST'])
def kaydet():
    ad = request.form.get('ad_soyad')
    tel = request.form.get('telefon')
    
    # Verileri dosyaya kaydeder
    with open("musteriler.txt", "a", encoding="utf-8") as f:
        f.write(f"Ad: {ad} | Tel: {tel}\n")
    
    return "<h1>Bilgileriniz başarıyla kaydedildi! En kısa sürede size ulaşacağız.</h1><a href='/'>Siteye Geri Dön</a>"

# GİZLİ PANEL SAYFASI
@app.route(f'/{PANEL_LINKI}')
def listele():
    if not os.path.exists("musteriler.txt"):
        return "<h1>Henüz kayıtlı müşteri yok.</h1>"
    
    with open("musteriler.txt", "r", encoding="utf-8") as f:
        satirlar = f.readlines()
    
    # Şık bir tablo görünümü
    cikti = f"""
    <html>
    <head><title>Oreon Müşteri Paneli</title></head>
    <body style="font-family: sans-serif; padding: 50px; background: #0a162b; color: white;">
        <h1 style="color: #bc965d;">Müşteri Kayıt Listesi</h1>
        <table border="1" cellpadding="15" style="border-collapse: collapse; width: 100%; border-color: #bc965d;">
            <tr style="background: #050c1a; color: #bc965d;"><th>Müşteri Bilgileri (Ad ve Telefon)</th></tr>
    """
    for satir in satirlar:
        cikti += f"<tr><td>{satir}</td></tr>"
    
    cikti += "</table><br><br><a href='/' style='color: #bc965d;'>Siteye Dön</a></body></html>"
    return cikti

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
