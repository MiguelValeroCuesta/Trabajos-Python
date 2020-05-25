import pymysql

class Classconnect():
    def __init__(self):
        #Me conecta con la base de datos
        self.CrearConnect()
        #Abre la conexion
        self.AbrirConnect()
    def CrearConnect(self):
        self.db = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            passwd="",
            db="alumnos"
        )
    def AbrirConnect(self):
        self.cursor = self.db.cursor()

    def EjecutarSQL(self,sql):
        self.cursor.execute(sql)
        
    def DevolverDatos(self):
        return self.cursor.fetchall()

    def DevolverActualizacion(self):
        return self.cursor.fetchone()
    
    def CerrarBase(self):
        self.db.close()

    def RealizarCambio(self):
        self.db.commit()

    def DeshacerCambio(self):
        self.db.rollback()