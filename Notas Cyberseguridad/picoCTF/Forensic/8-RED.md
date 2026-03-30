# RED

# Descripción del reto:

RED, RED, RED, RED. Download the image: red.png.

# Solución:

mkdir reto_red && cd reto_red

wget [https://challenge-files.picoctf.net/c_verbal_sleep/831307718b34193b288dde31e557484876fb84978b5818e2627e453a54aa9ba6/red.png](https://challenge-files.picoctf.net/c_verbal_sleep/831307718b34193b288dde31e557484876fb84978b5818e2627e453a54aa9ba6/red.png)

zsteg -a red.png

echo "cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==" | base64 -d

'picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}'

# Notas adicionales:

- El reto utiliza esteganografía en el canal de color Rojo. La descripción repetitiva "RED" y el poema oculto en los metadatos (cuyas iniciales forman el acróstico "CHECK LSB") confirmaron la técnica a utilizar.
    
- Se utilizó `zsteg` para analizar los bits menos significativos (LSB) de la imagen.
    
- En el canal `b1,rgba,lsb,xy`, se encontró un payload codificado en Base64.
    
- Al decodificar la cadena, se obtuvo la bandera final.
    

# Referencias:

[https://github.com/zed-0xff/zsteg](https://github.com/zed-0xff/zsteg)