# Ph4nt0m 1ntrud3r

# Descripción del reto:

A digital ghost has breached my defenses... The attacker has cleverly concealed his moves in well timely manner.

# Solución:

mkdir reto_phantom && cd reto_phantom

wget [https://challenge-files.picoctf.net/c_verbal_sleep/bdda31c79c31975a5fe5402777bc87794655172e5d5bb2b569f1970df8efda34/myNetworkTraffic.pcap](https://challenge-files.picoctf.net/c_verbal_sleep/bdda31c79c31975a5fe5402777bc87794655172e5d5bb2b569f1970df8efda34/myNetworkTraffic.pcap)

tshark -r myNetworkTraffic.pcap -Y "tcp.segment_data" -T fields -e frame.time_epoch -e tcp.segment_data | sort -n | awk '{print $2}' | xxd -p -r | base64 -d

'picoCTF{1t_w4snt_th4t_34sy_tbh_4r_af160980}'

# Notas adicionales:

- El reto presenta un escenario de exfiltración de datos donde los paquetes han sido inyectados en el flujo de red con marcas de tiempo (timestamps) que no corresponden a su orden de llegada visual en herramientas como Wireshark.
    
- Para resolverlo, se utilizó `tshark` para extraer los campos `frame.time_epoch` (tiempo Unix) y `tcp.segment_data` (la carga útil del paquete).
    
- Al aplicar un ordenamiento numérico basado en el tiempo de captura (`sort -n`), se logró reconstruir la secuencia lógica de los fragmentos de datos.
    
- Los datos resultantes estaban codificados en Base64; tras la decodificación y limpieza, se reveló la bandera completa que el "fantasma" intentó ocultar mediante el desorden temporal.
    

# Referencias:

[https://www.wireshark.org/docs/man-pages/tshark.html](https://www.wireshark.org/docs/man-pages/tshark.html)