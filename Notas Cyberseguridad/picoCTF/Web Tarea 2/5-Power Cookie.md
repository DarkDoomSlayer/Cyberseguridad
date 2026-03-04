# Power Cookie
# Descripción del reto:
Can you get the flag? Go to this website and see what you can discover. http://saturn.picoctf.net:56180/
# Solución:
1. Se ingresa a la página y se hace clic en el botón "Continue as guest". El servidor redirige a /check.php indicando que no hay servicios para invitados.
2. Usando las herramientas de desarrollador del navegador [F12] > Almacenamiento > Cookies, se identifica una cookie llamada 'isAdmin' con el valor '0'.
3. Se edita el valor de la cookie 'isAdmin' cambiándolo a '1' y se recarga la página para simular una sesión de administrador.

'picoCTF{gr4d3_A_c00k13_5d2505be}'

# Notas adicionales:
Vulnerabilidad de manipulación de cookies (Cookie Tampering). El servidor gestiona el control de acceso confiando ciegamente en datos almacenados y controlados por el cliente. Al cambiar la variable 'isAdmin' a 1, el atacante logra una escalación de privilegios vertical de manera trivial. Todo control de privilegios debe ser validado del lado del servidor.
# Referencias: