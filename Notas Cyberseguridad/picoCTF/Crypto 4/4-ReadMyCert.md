# ReadMyCert

# Descripción del reto:
How about we take you on an adventure on exploring certificate signing requests. Take a look at this CSR file `here`.

# Solución:
El reto nos proporciona un archivo `.csr` (Certificate Signing Request). Estos archivos son el estándar de la industria (PKCS#10) utilizado para solicitar la emisión de un certificado digital a una Autoridad Certificadora (CA). 

### Concepto: Inspección de Metadatos (PKI)
Un archivo CSR contiene información de identidad del solicitante (como el Common Name, Organization, Locality, etc.) y la llave pública que será certificada. Es crucial entender que la información dentro de un CSR **no está encriptada**, únicamente está estructurada bajo el estándar ASN.1 y codificada en formato PEM (Base64). Por lo tanto, cualquier persona con acceso al archivo puede leer los metadatos en texto plano utilizando las herramientas adecuadas.

En este reto, el creador inyectó la bandera directamente en uno de los atributos del "Subject" (Sujeto) del certificado.

### Proceso de explotación:
Se desarrolló un script en Python que interactúa con las herramientas nativas del sistema operativo para parsear el archivo.
1. **Descarga:** Se automatizó la obtención del archivo `readmycert.csr`.
2. **Decodificación:** Se invocó el binario `openssl` a través de un subproceso de Python con los siguientes parámetros:
   * `req`: Comando para el manejo de solicitudes PKCS#10.
   * `-in readmycert.csr`: Especifica el archivo de entrada.
   * `-noout`: Evita que el comando imprima la versión codificada por defecto.
   * `-text`: Imprime el contenido del CSR de forma legible para humanos.
3. **Extracción:** Se capturó la salida estándar del comando (STDOUT) y se aplicó una expresión regular (`picoCTF\{.*?\}`) para aislar e imprimir la bandera oculta entre los atributos de identidad de la solicitud.

**Bandera final:**
`picoCTF{read_mycert_5aeb0d4f}`

# Notas adicionales:
* Este reto es un excelente recordatorio en auditorías de seguridad: los metadatos en certificados públicos y CSRs son visibles para todos. Nunca se deben incluir contraseñas, tokens o información sensible interna dentro de los campos de identidad de un certificado SSL/TLS.
* El uso de `subprocess` permite integrar el poder de herramientas nativas robustas (como OpenSSL) directamente en flujos de trabajo automatizados con Python.

# Referencias:
* [OpenSSL req documentation](https://www.openssl.org/docs/manmaster/man1/openssl-req.html)
* [Certificate signing request (Wikipedia)](https://en.wikipedia.org/wiki/Certificate_signing_request)