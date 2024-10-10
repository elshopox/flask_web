from flask import Flask, render_template, request
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

# Página principal
@app.route('/')
def index():
    return render_template('index.html')

# Página Quiénes Somos
@app.route('/about')
def about():
    return render_template('about.html')

# Página de Servicios
@app.route('/services')
def services():
    return render_template('services.html')

# Página de Noticias
@app.route('/news')
def news():
    return render_template('news.html')

# Página de Contacto con manejo de método POST
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        mensaje = request.form.get('mensaje')
        # Aquí puedes procesar los datos, como enviarlos a un email o guardarlos
        return f"Mensaje enviado por {nombre}."
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)  # Puedes usar esto para desarrollo
    # freezer.freeze()  # Usa esto para congelar la aplicación para producción