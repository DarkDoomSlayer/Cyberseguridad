# IntroToBurp
# Descripción del reto:
Try here to find the flag http://titan.picoctf.net:49856/
# Solución:
1. Se accedió a la página y se llenó el formulario de registro inicial con datos ficticios.
2. Al ser redirigido a la página de autenticación 2FA (/dashboard), se abrió el Inspector de elementos del navegador (F12).
3. Se localizó la etiqueta del formulario correspondiente al código: <input type="text" name="otp" placeholder="Enter OTP">.
4. Se modificó el atributo 'name' (eliminando la palabra 'otp') para evitar que el navegador enviara esa variable al servidor.
5. Se envió el formulario con un número cualquiera. Al no recibir el parámetro esperado, el servidor falló de forma insegura y concedió el acceso.\
6. Finalmente, la pagina nos muestra le mensaje siguiente:
   "Welcome, carlos you sucessfully bypassed the OTP request. Your Flag: picoCTF{#0TP_Bypvss_SuCc3$S_e1eb16ed}"

'picoCTF{#0TP_Bypvss_SuCc3$S_e1eb16ed}'

# Notas adicionales:
El reto demuestra una vulnerabilidad en la lógica de validación conocida como "Fail Open". Si el servidor no recibe el parámetro 'otp' en la petición, en lugar de bloquear el intento, asume que la validación pasó y entrega la bandera. Aunque el reto sugiere usar un proxy como Burp Suite, es posible realizar un bypass manipulando el DOM del HTML directamente desde las herramientas de desarrollador.
# Referencias: