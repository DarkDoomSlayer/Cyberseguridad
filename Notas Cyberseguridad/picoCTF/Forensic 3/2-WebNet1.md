# WebNet1

# Descripción del reto:

We found this packet capture and key. Recover the flag.

# Solución:

rm capture.pcap* picopico.key*

wget [https://challenge-files.picoctf.net/c_fickle_tempest/d1e9add4e31989553f239ebf71ba5972f9bed7bd4932f931e14bfba80d75f815/capture.pcap](https://challenge-files.picoctf.net/c_fickle_tempest/d1e9add4e31989553f239ebf71ba5972f9bed7bd4932f931e14bfba80d75f815/capture.pcap)

wget [https://challenge-files.picoctf.net/c_fickle_tempest/d1e9add4e31989553f239ebf71ba5972f9bed7bd4932f931e14bfba80d75f815/picopico.key](https://challenge-files.picoctf.net/c_fickle_tempest/d1e9add4e31989553f239ebf71ba5972f9bed7bd4932f931e14bfba80d75f815/picopico.key)

tshark -r capture.pcap -o 'uat:rsa_keys:"picopico.key",""' -Y http -V | grep -E -o 'picoCTF{[^}]+}'

'picoCTF{honey.roasted.peanuts}'

# Notas adicionales:

- Este reto es la continuación directa de WebNet0, utilizando la misma técnica de intercepción de tráfico cifrado mediante una llave privada RSA expuesta.
    
- La diferencia principal radica en la inyección de señuelos o falsos positivos (`this.is.not.your.flag.anymore`) dentro de las cabeceras o payloads HTTP para confundir el análisis manual.
    
- Al automatizar la extracción con `tshark` e inyectar la llave RSA a través de la tabla de atributos de usuario (`uat:rsa_keys`), se desencripta el tráfico al vuelo. Luego, el uso de expresiones regulares con `grep` permite listar todas las cadenas con formato de bandera, aislando fácilmente la verdadera.
    

# Referencias:

[https://wiki.wireshark.org/TLS](https://wiki.wireshark.org/TLS) [https://www.wireshark.org/docs/man-pages/tshark.html](https://www.wireshark.org/docs/man-pages/tshark.html)