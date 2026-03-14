# WebNet0

# Descripción del reto:

We found this packet capture and key. Recover the flag.

# Solución:

wget [https://challenge-files.picoctf.net/c_fickle_tempest/66113619363fca174ef6bf56587007af1626f99c44fc5cf92333f9fd8876ce9a/capture.pcap](https://challenge-files.picoctf.net/c_fickle_tempest/66113619363fca174ef6bf56587007af1626f99c44fc5cf92333f9fd8876ce9a/capture.pcap) wget [https://challenge-files.picoctf.net/c_fickle_tempest/66113619363fca174ef6bf56587007af1626f99c44fc5cf92333f9fd8876ce9a/picopico.key](https://challenge-files.picoctf.net/c_fickle_tempest/66113619363fca174ef6bf56587007af1626f99c44fc5cf92333f9fd8876ce9a/picopico.key)

tshark -r capture.pcap -o 'uat:rsa_keys:"picopico.key",""' -Y http -V | grep -E -o 'picoCTF{[^}]+}'

'picoCTF{nongshim.shrimp.crackers}'

# Notas adicionales:

- El reto consiste en una captura de tráfico de red (`capture.pcap`) donde la comunicación HTTP viaja cifrada bajo el protocolo TLS/SSL (HTTPS).
    
- A diferencia de los análisis de red estándar, aquí se proporciona la llave privada RSA del servidor (`picopico.key`). Poseer esta llave permite realizar un ataque _Man-in-the-Middle_ pasivo o, en análisis forense, desencriptar todo el tráfico capturado al vuelo.
    
- Debido a las actualizaciones en las versiones modernas de Wireshark/tshark, la sintaxis heredada (`tls.keys_list`) es obsoleta. La inyección de la llave privada se realiza mediante las Tablas de Atributos de Usuario (UAT) usando el parámetro `-o 'uat:rsa_keys:"ruta_llave","contraseña"'`.
    
- Una vez inyectada la llave, el tráfico se descifra internamente, permitiendo filtrar por el protocolo `http` y extraer la bandera inyectada en las cabeceras o el payload de la comunicación en texto plano.
    

# Referencias:

[https://wiki.wireshark.org/TLS](https://wiki.wireshark.org/TLS) [https://www.wireshark.org/docs/man-pages/tshark.html](https://www.wireshark.org/docs/man-pages/tshark.html)