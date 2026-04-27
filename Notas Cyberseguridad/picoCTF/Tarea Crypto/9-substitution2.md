# substitution2

# Descripción del reto:
It seems that another encrypted message has been intercepted. The encryptor seems to have learned their lesson though and now there isn't any punctuation! Can you still crack the cipher? Download the message `here`.

# Solución:
El reto presenta un **Cifrado de Sustitución Monoalfabética** en formato *scriptio continua* (sin espacios ni signos de puntuación). El autor intentó ofuscar el criptograma eliminando la estructura sintáctica, creyendo que esto mitigaría el análisis estadístico.

### Concepto: N-Grams y Known-Plaintext Attack (KPA)
Eliminar los espacios no soluciona la vulnerabilidad matemática de un cifrado de sustitución. Los atacantes pueden utilizar el análisis de **N-gramas** (secuencias de $N$ letras consecutivas que se repiten con alta frecuencia en un idioma, como "the", "ing", "tion") para recuperar el texto plano.

En este caso, las herramientas heurísticas basadas en diccionarios (como Quipqiup) lograron recuperar el texto en inglés, pero "alucinaron" al intentar decodificar la bandera final debido a su naturaleza aleatoria (hashes y leetspeak). Para obtener la bandera exacta, se transicionó a un **Ataque de Texto Plano Conocido (KPA)** manual.

### Proceso de explotación:
1. **Análisis Heurístico Inicial:** Se utilizó `quipqiup` para realizar un análisis de frecuencia sobre el bloque de texto continuo, logrando recuperar la mayor parte del documento en inglés e identificando la ubicación de la bandera.
2. **Alineación KPA:** Dado que Quipqiup falló en la traducción del hash final, se utilizó el criptograma original y se buscó el patrón de la bandera. Sabiendo que el texto original debía contener la cadena `picoCTF`, se localizó el segmento cifrado correspondiente (`QCUHUIE`).
3. **Mapeo Manual del Alfabeto:** 
   * Se alineó `QCUHUIE` $\rightarrow$ `picoCTF`, extrayendo las equivalencias directas (ej. Q=p, C=i, U=c...).
   * Utilizando el contexto recuperado ("the flag is..."), se mapearon letras adicionales para construir un diccionario de sustitución parcial pero matemáticamente exacto.
4. **Traducción Quirúrgica:** Se aplicó el diccionario deducido directamente sobre el bloque final de la bandera cifrada `{K6F4G_4K41R515_15_73A10B5_702E03EU}`, traduciendo los caracteres uno a uno sin depender de diccionarios de palabras reales.

**Bandera final:**
`picoCTF{n6r4m_4n41y515_15_73d10u5_702f03fc}`

# Notas adicionales:
* Las herramientas impulsadas por IA o estadística heurística son increíblemente rápidas, pero tienden a introducir errores en cadenas de alta entropía (como contraseñas, hashes o banderas). Siempre es necesario verificar los resultados críticos mediante criptoanálisis manual o scripts deterministas.
* "N-gram analysis is tedious" (El análisis de n-gramas es tedioso), como bien dice la bandera, pero sumamente efectivo.

# Referencias:
* [N-gram (Wikipedia)](https://en.wikipedia.org/wiki/N-gram)
* [Known-plaintext attack (Wikipedia)](https://en.wikipedia.org/wiki/Known-plaintext_attack)
