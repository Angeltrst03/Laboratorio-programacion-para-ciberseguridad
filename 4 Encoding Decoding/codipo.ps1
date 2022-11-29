#Jorge Angel Valdez Tristan 1957496
clear-host
write-host "bienvenido a un ejemplo de codificacion/decodificacion base64 usando powershell"
write-host "codificando un archivo de texto"
$inputfile ="C:\Users\USER\Downloads\secret.txt"
$fc =get-content $inputfile 
$gb= [system.text.encoding]::UTF8.getbytes($fc)
$etext = [system.convert]::tobase64string($gb)

write-host "El contenido del archivo CODIFICADO es " $etext


write-host "Decodificando el archivo previo:" 

[system.text.encoding]::ASCII.getstring([system.convert]::frombase64string($etext)) | Out-File -Encoding "ASCII"  C:\Users\USER\Downloads\secret.txt
$outfile12 = get-content C:\Users\USER\Downloads\secret.txt
write-host "el texto decodifcado es el siguiente"
write-host "Decodificado" $outfile12