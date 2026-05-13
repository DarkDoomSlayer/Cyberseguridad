# Roboto Sans
# Descripción del reto:
The flag is somewhere on this web application not necessarily on the website. Find it. http://saturn.picoctf.net:51652/
# Solución:
dark@kali:~$ curl -s http://saturn.picoctf.net:51652/robots.txt
# (Se identifica la cadena Base64: anMvbXlmaWxlLnR4dA==)

echo "anMvbXlmaWxlLnR4dA==" | base64 -d
js/myfile.txt

curl -s http://saturn.picoctf.net:51652/js/myfile.txt
picoCTF{Who_D03sN7_L1k5_90B0T5_718c9043}

'picoCTF{Who_D03sN7_L1k5_90B0T5_718c9043}'

# Notas adicionales:
Vulnerabilidad de exposición de información. El archivo robots.txt reveló una ruta oculta ofuscada en Base64. Al decodificarla, se obtuvo la ubicación del archivo de texto que contenía la bandera.
# Referencias: