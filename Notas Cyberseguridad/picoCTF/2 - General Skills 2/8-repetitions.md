# repetitions
# Descripción del reto:
Can you make sense of this file? Download the file [here](https://artifacts.picoctf.net/c/475/enc_flag).
# Solución:
cat enc_flag | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d
cGljb0NURntiYXNlNjRfbjNzdDNkX2RpYzBkIW44X2Qwd25sMDRkM2RfNDkyNzY3ZDJ9Cg==
echo "cGljb0NURntiYXNlNjRfbjNzdDNkX2RpYzBkIW44X2Qwd25sMDRkM2RfNDkyNzY3ZDJ9Cg==" | base64 -d
picoCTF{base64_n3st3d_dic0d!n8_d0wnl04d3d_492767d2}

'picoCTF{base64_n3st3d_dic0d!n8_d0wnl04d3d_492767d2}'
# Notas adicionales
# Referencias