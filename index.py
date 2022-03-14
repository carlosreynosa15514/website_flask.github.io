# La ruta del proyecto es: C:\Users\carlo\OneDrive\Cursos Practicos\Python\Flask Fast Web Mar 2022
# Tiene Virutal Environment llamado website
# Se utiliza Git y Github: https://github.com/carlosreynosa15514/website_flask.github.io

# Importando libreria flask
from flask import Flask
# Para poder utilizar files html en los paths creados
from flask import render_template 


# Inicializando Flask en una variable
app = Flask(__name__)

# Creando un path, en este caso home
@app.route('/')
def home():
    return render_template('home.html')

# Creando otra ruta
@app.route('/about')
def about():
    return render_template('about.html')

# Hacer que nuestra aplicacion siempre este escuchando
if __name__ == '__main__':
    app.run(debug=True) # Este metodo activa un servidor siempre escuchando
    