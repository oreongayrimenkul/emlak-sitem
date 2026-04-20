from flask import Flask, render_template, request

# Dosyalar yan yana olduğu için '.' (nokta) koyduk
app = Flask(__name__, template_folder='.')

@app.route('/')
def ana_sayfa():
    return render_template('ilan.html')

@app.route('/kaydet', methods=['POST'])
def kaydet():
    ad = request.form.get('ad_soyad')
    tel = request.form.get('telefon')
    butce = request.form.get('butce')
    
    with open("musteriler.txt", "a", encoding="utf-8") as f:
        f.write(f"Ad: {ad}, Tel: {tel}, Butce: {butce}\n")
    
    return "<h1>Bilgileriniz kaydedildi!</h1><a href='/'>Geri Don</a>"

if __name__ == '__main__':
    app.run(debug=True)