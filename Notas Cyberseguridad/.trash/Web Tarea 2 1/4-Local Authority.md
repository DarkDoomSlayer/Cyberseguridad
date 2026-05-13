# Local Authority
# Descripción del reto:
Can you get the flag? Go to this website and see what you can discover. http://saturn.picoctf.net:57929/
# Solución:
 curl -s http://saturn.picoctf.net:57929/
# (Al intentar un login fallido, se inspecciona el código fuente de la página y se descubre que la validación depende de un script local llamado secure.js)

dark@kali:~$ curl -s http://saturn.picoctf.net:57929/secure.js
function checkPassword(username, password)
{
  if( username === 'admin' && password === 'strongPassword098765' )
  {
    return true;
  }
...
}
# (Se extraen las credenciales en texto plano del código fuente y se utilizan en el formulario principal para iniciar sesión).

picoCTF{j5_15_7r4n5p4r3n7_05df90c8}

# Notas adicionales:
Vulnerabilidad de autenticación del lado del cliente (Client-Side Authentication). La lógica de validación y las credenciales nunca deben residir en archivos JavaScript expuestos al navegador, ya que el usuario tiene acceso total y directo a ellos. Todo control de acceso debe realizarse de forma segura en el backend.
# Referencias: