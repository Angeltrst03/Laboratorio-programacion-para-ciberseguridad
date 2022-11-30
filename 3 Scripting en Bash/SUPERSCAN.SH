#!/bin/bash
# Script superscan.sh
# 27/Septiembre/2022 Jorge Angel Valdez Tristan 
#
# Ejemplo de Menu en BASH
#
date
	echo "------------------------"
	echo "     Menu Principal"
	echo "------------------------"
	echo "1. Net Discover"
	echo "2. Portscanv1"
	echo "3. Welcome"
	echo "4. Exit"
read -p "Opcion [ 1 - 4 ] " c
case $c in
	1) $HOME/netdiscover.sh;;
	2) $HOME./portscanv1.sh;;
	3) $HOME./welcome.sh;;
	4) exit 0;;
esac