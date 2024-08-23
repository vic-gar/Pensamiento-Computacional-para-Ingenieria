## TC1028.415 Pensamiento Computacional para Ingeniería Proyecto 

## Examen de Personalidad: ¿Extrovertido, Introvertido o un poco de ambos?

# CONTEXTO

Los términos de extrovertido, introvertido o ambivertido se utilizan para clasificar la personalidad de las personas en un ambito social. El comportamiento que tomas en una situación donde interfieren más personas, a veces conocidas, otras desconocidas, se puede definir en estos tres conceptos y puede que tú mismo ya tengas presente que tipo de persona eres, pero ¿no te gustaría averiguarlo? 

Estos términos fueron creados por el psiquiatra Carl Gustav Jung (1920), quien indicaba que una persona extrovertida busca "un contacto intenso con el mundo exterior" mientras que alguien introvertido "mira hacia el interior". En términos del autor nadie es completamente introvertido o extrovertido, pero si tendemos a inclinarnos a uno de estos casos. Fuente (https://bvgpsicologia.com/que-es-ser-introvertido-o-extrovertido/)

En este examen diseñado por la psicóloga Vanesa Fernandez Lopez (2022) recabado de la página Webconsultas: (https://www.webconsultas.com/mente-y-emociones/test-de-psicologia/test-eres-extrovertido-o-introvertido-12699) ; se te presentarán una serie de preguntas que te ayudarán a poder descifrar si te inclinas más a tener una personalidad introvertida o extrovertida, o si se te puede considerar en un punto medio. Al final del test se te presentarán tus resultados en base a tus respuestas. 


# ALGORITMO

**Inicio del examen** (Estado Inicial)


>Primer pregunta

 '''
print("1. Cuando estoy en una reunion de trabajo 
  1) Prefiero pasar desapercibido
  2) Intervengo solo cuando es necesario
  3) Me gusta participar
     ")
'''
>se guarda la respuesta que indica el usuario

resp_1 = int(input())

>se guarda la respuesta en el resultado para sumar las respuestas

resultado = resp_1


>Segunda Pregunta

'''
print("2. A la hora de entablar nuevas amistades  
  1) No me gusta, y me cuesta muchísimo
  2) Dependiendo de cómo sean las personas, se me da mejor o peor
  3) Me gusta y lo hago fácilmente
     ")
'''
>se guarda la respuesta que indica el usuario

resp_2 = int(input())

>se guarda la respuesta en el resultado para sumar las respuestas

resultado = resp_1 + resp_2


>Tercera Pregunta

'''
print("3. Mi interés y disfrute por las relaciones sociales 
  1) Es nulo
  2) Es moderado, dependiendo de las circunstancias
  3) Es alto; me encanta estar con gente, hablar, etcétera
     ")
'''

>se guarda la respuesta que indica el usuario

resp_3 = int(input())

>se guarda la respuesta en el resultado para sumar las respuestas

resultado = resp_1 + resp_2 + resp_3


> Cuarta Pregunta

'''
print ("4. En general, mi grado de sociabilidad es 
  1) Bajísimo
  2) Moderado
  3) Muy alto
     ")
'''

>se guarda la respuesta que indica el usuario

resp_4 = int(input())

>se guarda la respuesta en el resultado para sumar las respuestas

resultado = resp_1 + resp_2 + resp_3 + resp_4


>Quinta Pregunta

'''
print ("5. Cuando debo de realizar un trabajo en equipo
  1) Lo evito como sea
  2) Lo hago, aunque no sea mi elección preferida
  3) Me gusta organizarme y trabajar con la gente
     ")
'''
>se guarda la respuesta que indica el usuario

resp_5 = int(input())

>se guarda la respuesta en el resultado para sumar las respuestas

resultado = int(resp_1 + resp_2 + resp_3 + resp_4 + resp_5)

>Dependiendo de la suma de tu resultado final sabras tu resultado

'''
print ("Si tu resultado se encuentra entre 1 y 5 eres INTROVERTIDO")
print ("Si tu resultado se encuentra entre 6 y 10 eres AMBIVERTIDO")
print ("Si tu resultado se encuentra entre 11 y 15 eres EXTROVERTIDO")
'''

>Se despliega el resultado obtenido

**Estado Final** (print("Resultado:", resultado))











