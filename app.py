from flask import Flask, flash, jsonify, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required
from config import config

#models
from models.modelUser import modelUser

#entities
from models.entities.user import User


app = Flask(__name__)

# Token de proteccion
csrf = CSRFProtect() 

# MYSQL CONEXION
db = MySQL(app)

#traer datos del usuario logueado
login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return modelUser.get_by_id(db, id)

@app.route('/')
def redireccion():
    return redirect(url_for('login'))
# LOGIN
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User(0, request.form['usuario'], request.form['contraseña'])
        logged_user = modelUser.login(db, user)
        if logged_user != None:
            if logged_user.Contraseña:
                login_user(logged_user)
                return redirect(url_for('index'))
            else: 
                flash("Contraseña incorrecta, verifique")
                return render_template("auth/login.html")
        else:
            flash("Usuario NO encontrado")
            return render_template("auth/login.html")
        
    else:
        return render_template("auth/login.html")
 

 
# Logout usuarios
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

#Index admin
@app.route('/index')
def index():
    return render_template("index_admin.html")


# Rutas protegidas
@app.route('/protegida')
@login_required
def protegida():
    return "<h1>Esta es una vista protegida, solo para usuarios autenticados >:(</h1>"

# Rutas de errores
def estado_401(error):
    return redirect(url_for('login'))

def estado_404(error):
    return "<h1>Pagina no encontrada</h1>", 404
#Gestionar pedidos admin
@app.route('/gestionarPedidos')
def gestionarPedidos():
    return render_template("Gestionar_pedidos.html")


#Pedidos en Mesa admin
@app.route('/pedidosMesa')
def pedidosMesa():
    return render_template("Pedidos_mesa.html")


#Pedidos en Linea admin
@app.route('/pedidosLinea')
def pedidosLinea():
    return render_template("Pedidos_linea.html")

#Historial Pedidos admin
@app.route('/historialPedidos')
def historial():
    return render_template("Historial_pedidos.html")

#Gestionar Productos admin (vista)
@app.route('/gestionarProductos')
def productos():
    cur = db.connection.cursor()
    cur.execute('SELECT * FROM productos')
    datos = cur.fetchall()
    return render_template('Gestionar_productos.html', productos = datos)

#Gestionar Productos admin (añadir)
@app.route('/añadirProducto', methods=['POST'])
def añadirProducto():
    if request.method == 'POST':
        IDpro = request.form['IDProducto']
        producto = request.form['nombreProducto']
        descripcion = request.form['descripcion']
        categoria = request.form['categoria']
        precio = request.form['precio']
        cur = db.connection.cursor()
        cur.execute('INSERT INTO productos (ID_Producto, Nombre_Producto, descripción, Categoría, Precio) VALUES (%s, %s, %s, %s, %s)',(IDpro, producto, descripcion, categoria, precio))
        db.connection.commit()
        flash('¡Producto agregado!')
        return redirect(url_for('productos'))

#Gestionar Productos admin (eliminar)
@app.route('/eliminarProducto/<string:id>')
def eliminarProducto(id):
    cur = db.connection.cursor()
    cur.execute('DELETE FROM productos WHERE ID_Producto = {0}'.format(id))
    db.connection.commit()
    flash('Producto eliminado con exito.')
    return redirect(url_for('productos'))

#Gestionar Productos admin (traer el id  para editar)
@app.route('/obtenerProducto/<id>')
def obtenerProducto(id):
    cur = db.connection.cursor()
    cur.execute('SELECT * FROM productos WHERE ID_Producto = %s', (id,))
    data = cur.fetchall()
    return render_template('Edit_producto.html', productos = data[0])

#Gestionar Productos admin (editar)
@app.route('/editarProducto/<id>', methods=['POST'])
def EditarProducto(id):
    if request.method == 'POST':

        IDpro = request.form['IDProducto']
        producto = request.form['nombreProducto']
        descripcion = request.form['descripcion']
        categoria = request.form['categoria']
        precio = request.form['precio']          
        Estado = request.form['Estado']          
        cur = db.connection.cursor()
        cur.execute('UPDATE productos SET ID_Producto = %s ,Nombre_Producto = %s,Descripción = %s ,Categoría = %s,Precio = %s, Estado = %s  WHERE ID_Producto = %s', (IDpro, producto, descripcion, categoria, precio, Estado, id))
        db.connection.commit()
        flash("Producto actualizado")
        return redirect(url_for('productos')    )


#Gestionar Usuarios admin
@app.route('/gestionarUsuarios')
def usuarios():
    return render_template('Gestionar_Usuarios.html')

#Gestionar Clientes admin (vista)
@app.route('/gestionarClientes')
def clientes():
    cur = db.connection.cursor()
    cur.execute('SELECT * FROM clientes')
    datos = cur.fetchall()
    return render_template('Gestionar_clientes.html', clientes = datos)

#Gestionar Clientes admin (añadir)
@app.route('/añadirClientes', methods=['POST'])
def añadirClientes():
    
    if request.method == 'POST':
        documento = request.form['documento']
        nombre = request.form['nombreCli']
        apellido = request.form['apellidoCli']
        Dirección_Entrega = request.form['direccion']
        Teléfono = request.form['telefono']
        Tipo_Cliente = request.form['tipo_cliente']

        cur = db.connection.cursor()
        cur.execute('INSERT INTO clientes (ID_Cliente, Nombre, Apellidos, Dirección_Entrega, Teléfono, Tipo_de_Cliente) VALUES (%s, %s, %s, %s, %s, %s)',(documento, nombre, apellido, Dirección_Entrega, Teléfono, Tipo_Cliente))
        db.connection.commit()
        flash('¡Usuario Agregado exitosamente!')
        return redirect(url_for('clientes'))


#Gestionar Clientes admin (eliminar)
@app.route('/eliminarClientes/<string:id>') 
def eliminarClientes(id):
    cur = db.connection.cursor()
    cur.execute('DELETE FROM clientes WHERE ID_Cliente = {0}'.format(id))
    db.connection.commit()
    flash('Cliente eliminado')
    return redirect(url_for('clientes'))


#Gestionar Clientes admin (traer el id  para editar)
@app.route('/obtenerCliente/<string:id>')
def obtenerCliente(id):
    cur = db.connection.cursor()
    cur.execute('SELECT * FROM clientes WHERE ID_Cliente = %s', (id,))
    data = cur.fetchall()
    return render_template('Edit_cliente.html', cliente = data[0])

#Gestionar Clientes admin (editar)
@app.route('/editarClientes/<id>', methods=['POST'])
def editarClientes(id):
    if request.method == 'POST':
        documento = request.form['documento']
        nombre = request.form['nombreCli']
        apellido = request.form['apellidoCli']
        Dirección_Entrega = request.form['direccion']
        Teléfono = request.form['telefono']
        Tipo_de_Cliente = request.form['tipo_cliente']

        cur = db.connection.cursor()
        cur.execute('UPDATE clientes SET ID_Cliente = %s, Nombre = %s, Apellidos = %s, Dirección_Entrega = %s, Teléfono = %s, Tipo_de_Cliente = %s WHERE ID_Cliente = %s',(documento, nombre, apellido, Dirección_Entrega, Teléfono, Tipo_de_Cliente, id))
        db.connection.commit()
        flash("¡Cliente actualizado exitosamente!")
        return redirect(url_for('clientes'))

#Gestionar empleados admin (vista)
@app.route('/gestionarEmpleados')
def empleados():
    cur = db.connection.cursor()
    cur.execute('SELECT * FROM empleados')
    datos = cur.fetchall()
    return render_template('Gestionar_empleados.html', empleados = datos)

#Gestionar Empleados admin (añadir)
@app.route('/añadirEmpleado', methods=['POST'])
def añadirEnpleados():
    
    if request.method == 'POST':

        ID = request.form['IDEmp']
        nombre = request.form['nombreEmp']
        apellido = request.form['apellidoEmp']
        rol = request.form['cargo']
        Teléfono = request.form['telefonoEmp']
        usuario = request.form['usuarioEmp']

        cur = db.connection.cursor()
        cur.execute('INSERT INTO empleados (ID_Empleado, Nombre, Apellidos, ID_Cargo, Teléfono, Usuario) VALUES (%s, %s, %s, %s, %s, %s)',(ID, nombre, apellido, rol, Teléfono, usuario))
        db.connection.commit()
        flash('Empleado Agregado!')
        return redirect(url_for('empleados'))


#Gestionar Empleado admin (eliminar)
@app.route('/eliminarEmpleado/<string:id>') 
def eliminarEmpleado(id):
    cur = db.connection.cursor()
    cur.execute('DELETE FROM empleados WHERE ID_Empleado = {0}'.format(id))
    db.connection.commit()
    flash('Empleado eliminado')
    return redirect(url_for('empleados'))


#Gestionar Clientes admin (traer el id  para editar)
@app.route('/obtenerEmpleado/<string:id>')
def obtenerEmpleado(id):
    cur = db.connection.cursor()
    cur.execute('SELECT * FROM empleados WHERE ID_Empleado = %s', (id,))
    data = cur.fetchall()
    return render_template('Edit_empleado.html', empleado = data[0])

#Gestionar Clientes admin (editar)
@app.route('/editarEmpleado/<id>', methods=['POST'])
def editarEmpleado(id):
    if request.method == 'POST':

        ID = request.form['IDEmp']
        nombre = request.form['nombreEmp']
        apellido = request.form['apellidoEmp']
        rol = request.form['cargo']
        Teléfono = request.form['telefonoEmp']
        usuario = request.form['usuarioEmp']

        cur = db.connection.cursor()
        cur.execute('UPDATE empleados SET ID_Empleado = %s,Nombre = %s, Apellidos = %s, ID_Cargo = %s, Teléfono = %s, Usuario = %s WHERE ID_Empleado = %s',(ID, nombre, apellido, rol, Teléfono, usuario, id))
        db.connection.commit()
        flash("Empleado actualizado")
        return redirect(url_for('empleados'))


@app.route('/indexMesero')
def indexMesero():
    return render_template("index_mesero.html")

if __name__ == '__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401, estado_401)
    app.register_error_handler(404, estado_404)
    app.run(port = 3000)