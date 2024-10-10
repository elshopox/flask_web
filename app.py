from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta para la página de inicio
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para la página "Quiénes Somos"
@app.route('/about')
def about():
    return render_template('about.html')

# Ruta para la página de servicios
@app.route('/services')
def services():
    return render_template('services.html')

# Ruta para la página de noticias
@app.route('/news')
def news():
    return render_template('news.html')

# Ruta para la página de contacto
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Aquí puedes procesar los datos del formulario como enviarlos por email o guardarlos
        return f"Gracias {name}, hemos recibido tu mensaje."
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)