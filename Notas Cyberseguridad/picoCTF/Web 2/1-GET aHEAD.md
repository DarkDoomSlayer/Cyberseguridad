# GET aHEAD
# Descripción del reto:
Find the flag being held on this server to get ahead of the competition http://wily-courier.picoctf.net:54478/
# Solución:
curl -I http://wily-courier.picoctf.net:54478/
HTTP/1.1 200 OK
Date: Thu, 26 Feb 2026 04:01:17 GMT
Server: Apache/2.4.38 (Debian)
X-Powered-By: PHP/7.2.34
flag: picoCTF{r3j3ct_th3_du4l1ty_8b13f07}
Content-Type: text/html; charset=UTF-8

'picoCTF{r3j3ct_th3_du4l1ty_8b13f07}'
# Notas adicionales
# Referencias
https://youtu.be/oiZk0tIkR48?si=fTufKRcOqpyT8ajP