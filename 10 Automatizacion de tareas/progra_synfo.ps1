
#$dir es la direccion donde se encuentra powershell 
$dir = (get-command powershell.exe).Path

#$Script, con -Execute se especifica la aplicacion con la que se ejecutara el programa, -Argument es elscript de powershell a usar , -workingDirectory es la direccion o path donde se encuentra el script
$script = New-ScheduledTaskAction -Execute $dir -Argument "Send_synfo.ps1" -workingDirectory "C:\Users\USER\Desktop\Practica_15"

#$time se especifica la hora la cual se desea l se ejecute el script 
$time  = New-ScheduledTaskTrigger -Daily -At "12:00am"
Register-ScheduledTask  -Action $script -Trigger $time  -TaskPath “MisTareas” -Taskname "Enviarsyinfo" -Description "Envio de informacion del sistema "