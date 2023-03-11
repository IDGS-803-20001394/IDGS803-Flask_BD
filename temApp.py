from db import get_connection

#try:
#    connection = get_connection()
#    with connection.cursor() as cursor:
#        cursor.execute('call obtener_alumnos()')
#        resultset=cursor.fetchall()
#        for row in resultset:
#            print(row)
#        connection.close()
#
#except Exception as ex:
#    pass

#try:
#    connection = get_connection()
#    with connection.cursor() as cursor:
#        cursor.execute('call consultar_alumno(%s)',(1,))
#        resultset=cursor.fetchall()
#        print(resultset)
#        connection.close()
#
#except Exception as ex:
#    pass

try:
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute('call insertar_alumno(%s,%s,%s)',("Nombre","Apellidos","Correo"))
    connection.commit()
    connection.close()

except Exception as ex:
    print(ex)