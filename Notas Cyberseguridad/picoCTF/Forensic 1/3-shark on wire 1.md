# shark on wire 1
# Descripción del reto:
We found this packet capture. Recover the flag.
# Solución:
tshark -r capture.pcap -q -z follow,udp,ascii,6
===================================================================
Follow: udp,ascii
Filter: udp.stream eq 6
Node 0: 10.0.0.2:5000
Node 1: 10.0.0.12:8888
1
p
1
i
1
c
1
o
...
1
e
1
}
===================================================================

'picoCTF{StaT31355_636f6e6e}'

# Notas adicionales:
La bandera estaba oculta dentro de un flujo de comunicación específico en la red, enviada carácter por carácter en múltiples paquetes. Utilizando 'tshark' (la versión de terminal de Wireshark), es posible aislar conversaciones usando el argumento "follow,udp,ascii". Al analizar los flujos disponibles, se identifica que el Stream número 6 contiene los caracteres de la bandera íntegra intercalados en el payload.
# Referencias: