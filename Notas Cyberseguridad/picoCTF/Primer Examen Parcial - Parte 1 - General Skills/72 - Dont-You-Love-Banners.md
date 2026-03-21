# Descripción
Can you abuse the banner? The server has been leaking some crucial information on `tethys.picoctf.net 63002`. Use the leaked information to get to the server. To connect to the running application use `nc tethys.picoctf.net 54663`. From the above information abuse the machine and find the flag in the /root directory.
# Solución
Entrar a la página y hacer un link simbólico para conseguir la flag

- Primero es entrar a la pagina de apoyo que tiene la contraseña y llevárnosla, luego a la página del reto y allí contestamos las 3 preguntas que nos hace, después borramos el banner "rm banner" y luego hacemos un link simbólico "ls -s /root/flag.txt /home/player/banner" entre la flag y el banner para que la próxima vez que nos conectemos directamente nos abra la flag y con ello al volver a conectarnos, tenemos la flag

picoCTF{b4nn3r_gr4bb1n9_su((3sfu11y_f7608541}


# Notas adicionales
- 
# Referencias
- 