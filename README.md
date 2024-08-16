# TC1028.415 Pensamiento Computacional para Ingeniería Proyecto 

# Examen de Personalidad: ¿Extrovertido, Introvertido o un poco de ambos?

CONTEXTO

Los términos de extrovertido, introvertido o ambivertido se utilizan para clasificar la personalidad de las personas en un ambito social. El comportamiento que tomas en una situación donde interfieren más personas, a veces conocidas, otras desconocidas, se puede definir en estos tres conceptos y puede que tú mismo ya tengas presente que tipo de persona eres, pero ¿no te gustaría averiguarlo? 

Estos términos fueron creados por el psiquiatra Carl Gustav Jung (1920), quien indicaba que una persona extrovertida busca "un contacto intenso con el mundo exterior" mientras que alguien introvertido "mira hacia el interior". En términos del autor nadie es completamente introvertido o extrovertido, pero si tendemos a inclinarnos a uno de estos casos. Fuente https://bvgpsicologia.com/que-es-ser-introvertido-o-extrovertido/

En este examen diseñado por la psicóloga Vanesa Fernandez Lopez (2022) recabado de la página Webconsultas: https://www.webconsultas.com/mente-y-emociones/test-de-psicologia/test-eres-extrovertido-o-introvertido-12699 ; se te presentarán una serie de preguntas que te ayudarán a poder descifrar si te inclinas más a tener una personalidad introvertida o extrovertida, o si se te puede considerar en un punto medio. Al final del test se te presentarán tus resultados en base a tus respuestas. 


ALGORITMO

Inicio del examen 

Resuestas = ("Pregunta 1", "Pregunta 2", "Pregunta 3", "Pregunta 4", "Pregunta 5", "Pregunta 6", "Pregunta 7", "Pregunta 8", "Presunta 9", "Pregunta 10")

0 = ambivertido
1 = introvertido
2 = extrovertido

Pregunta 1 = "1. Cuando estoy en una reunion de trabajo"
Desplega =
  a) Prefiero pasar desapercibido 
  b) Me gusta participar
  c) Intervengo solo cuando es necesario

Si elige "a" guarda valor 1 en "Respuestas"
Si elige "b" guarda valor 2 en "Respuestas"
Si elige "c" guarda valor 0 en "Respuestas"


Pregunta 2 = "2. A la hora de entablar nuevas amistades"
Desplega =
  a) Me gusta y lo hago fácilmente 
  b) No me gusta, y me cuesta muchísimo
  c) Dependiendo de cómo sean las personas, se me da mejor o peor

Si elige "a" guarda valor 2 en "Respuestas"
Si elige "b" guarda valor 1 en "Respuestas"
Si elige "c" guarda valor 0 en "Respuestas"


Pregunta 3 = "3. Mi interés y disfrute por las relaciones sociales"
Desplega =
  a) Es nulo
  b) Es moderado, dependiendo de las circunstancias
  c) Es alto; me encanta estar con gente, hablar, etcétera

Si elige "a" guarda valor 1 en "Respuestas"
Si elige "b" guarda valor 0 en "Respuestas"
Si elige "c" guarda valor 2 en "Respuestas"


Pregunta 4 = "4. En general, mi grado de sociabilidad es"
Desplega =
  a) Bajísimo
  b) Muy alto
  c) Moderado

Si elige "a" guarda valor 1 en "Respuestas"
Si elige "b" guarda valor 2 en "Respuestas"
Si elige "c" guarda valor 0 en "Respuestas"


Pregunta 5 = "5. Cuando debo de realizar un trabajo en equipo"
Desplega =
  a) Lo evito como sea
  b) Me gusta organizarme y trabajar con la gente
  c) Lo hago, aunque no sea mi elección preferida

Si elige "a" guarda valor 1 en "Respuestas"
Si elige "b" guarda valor 2 en "Respuestas"
Si elige "c" guarda valor 0 en "Respuestas"


Pregunta 6 = "6. ¿Qué tipos de hobbies prefieres?"
Desplega =
  a) Tranquilos (leer, ver una película…)
  b) Son variados; desde correr hasta ver una buena película o leer
  c) De acción (senderismo, deportes activos)

Si elige "a" guarda valor 1 en "Respuestas"
Si elige "b" guarda valor 0 en "Respuestas"
Si elige "c" guarda valor 2 en "Respuestas"


Pregunta 7 = "7. ¿En qué grado necesitas estar rodeado de otras personas?"
Desplega =
  a) Mucho; si estoy solo se me cae la casa encima
  b) Cuando las necesito o me aburro
  c) Poco; soy bastante solitario

Si elige "a" guarda valor 2 en "Respuestas"
Si elige "b" guarda valor 0 en "Respuestas"
Si elige "c" guarda valor 1 en "Respuestas"


Pregunta 8 = "8. A nivel emocional, las cosas me afectan"
Desplega =
  a) Poco
  b) Considerablemente, dependiendo de los acontecimientos
  c) Muchísimo; soy muy emocional

Si elige "a" guarda valor 2 en "Respuestas"
Si elige "b" guarda valor 0 en "Respuestas"
Si elige "c" guarda valor 1 en "Respuestas"


Pregunta 9 = "9. En general, la gente piensa de mí que soy"
Desplega =
  a) Una persona que se adapta a las circunstancias y, dependiendo de quien opine, más o menos simpático
  b) Callado y aburrido
  c) Sociable y divertido

Si elige "a" guarda valor 0 en "Respuestas"
Si elige "b" guarda valor 1 en "Respuestas"
Si elige "c" guarda valor 2 en "Respuestas"


Pregunta 10 = "10. Me considero una persona"
Desplega =
  a) Optimista
  b) Realista
  c) Pesimista

Si elige "a" guarda valor 2 en "Respuestas"
Si elige "b" guarda valor 0 en "Respuestas"
Si elige "c" guarda valor 1 en "Respuestas"


Respuestas = ("Pregunta 1", "Pregunta 2", "Pregunta 3", "Pregunta 4", "Pregunta 5", "Pregunta 6", "Pregunta 7", "Pregunta 8", "Presunta 9", "Pregunta 10")

Contar numero de valores de 2, 1, 0 en "Respuestas"

Si Respuestas = 2 > 1 > 0
  Despliega = "ERES EXTROVERTIDO"

Si Respuestas = 1 > 2 > 0
  Despliega = "ERES INTROVERTIDO"

Si Respuestas = 0 > 1 > 2
  Despliega = "ERES AMBIVERTIDO"







