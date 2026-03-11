# shark on wire 2

# Descripción del reto:

We found this packet capture. Recover the flag.

# Solución:

wget [https://challenge-files.picoctf.net/c_fickle_tempest/07bf5ee832c595a6de406476b6c07f164d2951fbcfcf9cf3739c25dea26e5f0b/capture.pcap](https://challenge-files.picoctf.net/c_fickle_tempest/07bf5ee832c595a6de406476b6c07f164d2951fbcfcf9cf3739c25dea26e5f0b/capture.pcap)

tshark -r capture.pcap -Y "udp.dstport == 22" -T fields -e udp.srcport | awk '{printf "%c", $1-5000}' && echo ""

'picoCTF{p1LLf3r3d_data_v1a_st3g0}'

# Notas adicionales:

- A diferencia de su predecesor ("shark on wire 1"), donde la información viajaba en el payload, este reto utiliza esteganografía de red ocultando datos directamente en las cabeceras de los paquetes UDP.
    
- El atacante exfiltró la bandera enviando paquetes hacia el puerto destino 22.
    
- El truco consistió en tomar el valor decimal en código ASCII de cada carácter de la bandera, sumarle 5000, y asignar ese número resultante como el Puerto de Origen (`udp.srcport`) de cada paquete.
    
- Se utilizó `tshark` (la versión de terminal de Wireshark) para filtrar únicamente el tráfico dirigido al puerto 22 y extraer los puertos de origen. Posteriormente, mediante `awk`, se restó el offset de 5000 a cada valor y se formateó la salida a caracteres ASCII (`%c`), revelando la bandera completa de forma automatizada.
    

# Referencias:

[https://www.wireshark.org/docs/man-pages/tshark.html](https://www.wireshark.org/docs/man-pages/tshark.html) [https://linux.die.net/man/1/awk](https://linux.die.net/man/1/awk)