# Descripción
A suspicious cell tower has been detected in the network. Analyze the captured network traffic to identify the rogue tower, find the compromised device, and recover the exfiltrated flag. Download the network capture file: [here](https://challenge-files.picoctf.net/c_plain_mesa/986fd133a4070d35bbf6f1aef9e24aebf411cc0a40af3ccb7416d776a39d2374/rogue_tower.pcap)
# Solución
Descargar el .pcac que se nos da y analizarlo en base a las pistas que nos dan para conseguir la flag

- Primero descargamos el .pcap, y con base a la pista buscamos con filtro "udp.port == 55000", para ver la dirección de los paquetes, después como no son muchos paquetes, usamos de filtro un "http" y como podemos observar hay un get el cual conecta a un destino distinto, por lo que checamos los detalles de ello y con esto podemos sacar el User-Agent y su IMSI ("310410308555787") que nos servirá para después, luego de esto inspeccionamos los paquetes con POST y vamos sacando los datos de allí y los vamos juntando hasta conseguir la flag cifrada, por último nos apoyamos de cyberchef, le mandamos el msj cifrado que esta en Base64, junto con un XOR para introducir la clave (El IMEI) y solamente vamos quitando números al IMEI hasta que conseguimos la flag

picoCTF{r0gu3_c3ll_t0w3r_dbc40831}


# Notas adicionales
- 
# Referencias
- https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)XOR(%7B'option':'UTF8','string':'08555787'%7D,'Standard',false)&input=UUZGV1duWmpma3hDQ0ZKQUJtaGJCRnhVYWtFRlFBdEZiMXhYVmdFSEFBUUJSUT09&oeol=VT