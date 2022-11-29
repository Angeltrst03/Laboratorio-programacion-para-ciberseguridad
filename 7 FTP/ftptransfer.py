#script para transferencias de archivos dtp
#25 de octubre del 2022 jorge Angel Valdez Tristan

from ftplib import FTP

#establecer coneccion y introducir usuario y contraseña

ftp= FTP("192.168.120.132","tris","1957496")
#listar el directorio
ftp.retrlines("LIST")


  #nos movemos al directorio upload
ftp.cwd("upload")
 
with open("ADVERTENCIA.txt","rb")as text_file:
 #cargamos el archivo aditado
 ftp.storlines("STOR ADVERTENCIA.txt",text_file)
 # Salimos de la conexion
 ftp.quit()
 



