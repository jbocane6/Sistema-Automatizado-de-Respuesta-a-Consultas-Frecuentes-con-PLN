# Sistema-Automatizado-de-Respuesta-a-Consultas-Frecuentes-con-PLN

## El sistema que se diseñó está pensado para entender preguntas hechas en lenguaje natural, procesarlas y ofrecer respuestas automáticas en tiempo real que sean coherentes y útiles. El prototipo fue pensado como un conjunto de partes conectadas, cubriendo etapas como juntar datos, limpiarlos posteriormente y prepararlos, entender el significado de ellos, generar respuestas y evaluar cómo funciona.
## Para su desarrollo, se utilizaron técnicas importantes de PLN como la separación de palabras conocida como tokenización, la gestión para darle formas básicas a las palabras o lematización, detectar la intención del usuario, buscar información relevante y clasificar el significado, usando librerías populares en Python como NLTK, spaCy y Hugging Face Transformers.


Instala las librerías necesarias:

```bash
$ pip install flask scikit-learn nltk spacy pandas
$ python -m spacy download en_core_web_sm
```

Ejecuta el servidor:

```bash
$ python prototipo_pln.py
```

Envía una consulta con Postman:
![image](https://github.com/user-attachments/assets/f1a4d7dc-e4a8-44ea-84ac-5bbcca7ca7d5)
![image](https://github.com/user-attachments/assets/80621056-b2bb-4894-bbb2-cf9eeae6c595)
![image](https://github.com/user-attachments/assets/d6608796-fb82-43f3-ab6f-afbf0db23b94)

Implementación con Javascrip
```js
let headersList = {
 "Accept": "*/*",
 "User-Agent": "Thunder Client (https://www.thunderclient.com)",
 "Content-Type": "application/json"
}

let bodyContent = JSON.stringify({"question": "como actualizo producto"});

let response = await fetch("http://127.0.0.1:5000/ask", { 
  method: "POST",
  body: bodyContent,
  headers: headersList
});

let data = await response.text();
console.log(data);

```

Implementación con Python
```python
import http.client
import json

conn = http.client.HTTPSConnection("127.0.0.1", 5000)

headersList = {
 "Accept": "*/*",
 "User-Agent": "Thunder Client (https://www.thunderclient.com)",
 "Content-Type": "application/json" 
}

payload = json.dumps({"question": "como actualizo producto"})

conn.request("POST", "/ask", payload, headersList)
response = conn.getresponse()
result = response.read()

print(result.decode("utf-8"))

```
