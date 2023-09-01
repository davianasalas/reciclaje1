from funcion_conexion import * 
def insertar_variables_registro(fn, ap, em, pas):
    print("ESTAMOS EN LA FUNCION REGISTRO USUARIOS")
    try:
        connection = conexion()  
        
        if connection:
            print("Conexion realizada")
        
        cursor = connection.cursor()
     
        query = """INSERT INTO `usuarios` (`Firstname`, `Lastname`, `Email`, `Password`) VALUES (%s, %s, %s, %s)"""
        variables = (fn, ap, em, pas)
        
        cursor.execute(query, variables)
        connection.commit()
        print("Se ha realizado la inserción")
        return "La inserción se ha realizado señor usuario"
    
    except mysql.connector.Error:
        print("ALGO HA FALLADO:")


