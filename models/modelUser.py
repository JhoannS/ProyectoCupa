from .entities.user import User


class modelUser():
    
    @classmethod
    def login(self, db, user):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT ID_Empleado, Usuario, Contraseña, Nombre FROM empleados WHERE Usuario ='{}'".format(user.Usuario, user.Contraseña)
            cursor.execute(sql)
            row=cursor.fetchone()
            if row != None:
                user = User(row[0],row[1],User.check_password(row[2],user.Contraseña),row[3])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT ID_Empleado, Usuario, Nombre FROM empleados WHERE ID_Empleado = {}".format(id)
            cursor.execute(sql)
            row=cursor.fetchone()
            if row != None:
                return User(row[0],row[1],None,row[2])
                
            else:
                return None
        except Exception as ex:
            raise Exception(ex)