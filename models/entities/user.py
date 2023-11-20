from werkzeug.security import check_password_hash
#generate_password_hash
from flask_login import UserMixin

class User(UserMixin):
    
    def __init__(self, id, Usuario, Contraseña, Nombre="") -> None:
        self.id = id
        self.Usuario =  Usuario  
        self.Contraseña = Contraseña
        self.Nombre = Nombre

    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)

#print(generate_password_hash("CupaJs**"))
#print(generate_password_hash("LisRb**"))
#print(generate_password_hash("JSzamudio**"))

#print(generate_password_hash("HolaMundo**"))