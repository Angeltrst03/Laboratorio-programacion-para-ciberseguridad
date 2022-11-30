#!/bin/bash
#Jorge Angel Valdez Tristan 

echo -e "Opcion 1: Escaneo de de host de una subred"
echo -e "Opcion 2: Escaneo individual de ip "
echo -e "Opcion 3: Escaneo UDP"
echo -e "Opcion 4: Escaneo con script"
echo -e "Opcion 5: Salir"
read -p "Seleccione una opcion: " seleccion

case $seleccion in
                1)
                        echo -e "Ingrese la subred a escanear :"
                        read subred
                        nmap -sn $subred -oN Results_Subred.txt;;
                2)

                        echo -e "Ingrese la ip a ser escaneada"
                        read subred
                        nmap -v -A $subred -oN ipscan.txt;;
                3)

                        echo -e "Ingrese la ip para excaneo de tipo UDP"
                        read subred
                        nmap -sU $subred -oN udpscan.txt;;
                4)

                        echo -e "Ingrese el scriptr"
                        read script
                        echo -e "Ingrese la ip"
                        read ip
                        nmap --script $script $ip -oN scriptscan.txt;;
                5)
                        exit;;
                 
esac
