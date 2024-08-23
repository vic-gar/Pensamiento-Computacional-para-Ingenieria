print("1. Cuando estoy en una reunion de trabajo \n 1) Prefiero pasar desapercibido \n 2) Intervengo solo cuando es necesario \n 3) Me gusta participar")

resp_1 = int(input())
resultado = resp_1

print("2. A la hora de entablar nuevas amistades \n 1) No me gusta, y me cuesta muchísimo \n 2) Dependiendo de cómo sean las personas, se me da mejor o peor \n 3) Me gusta y lo hago fácilmente")

resp_2 = int(input())
resultado = resp_1 + resp_2

print("3. Mi interés y disfrute por las relaciones sociales \n 1) Es nulo \n 2) Es moderado, dependiendo de las circunstancias \n 3) Es alto; me encanta estar con gente, hablar, etcétera")

resp_3 = int(input())
resultado = resp_1 + resp_2 + resp_3

print ("4. En general, mi grado de sociabilidad es \n 1) Bajísimo \n 2) Moderado \n 3) Muy alto")

resp_4 = int(input())
resultado = resp_1 + resp_2 + resp_3 + resp_4

print ("5. Cuando debo de realizar un trabajo en equipo  \n 1) Lo evito como sea \n 2) Lo hago, aunque no sea mi elección preferida \n 3) Me gusta organizarme y trabajar con la gente")

resp_5 = int(input())
resultado = int(resp_1 + resp_2 + resp_3 + resp_4 + resp_5)

print ("Si tu resultado se encuentra entre 1 y 5 eres INTROVERTIDO")
print ("Si tu resultado se encuentra entre 6 y 10 eres AMBIVERTIDO")
print ("Si tu resultado se encuentra entre 11 y 15 eres EXTROVERTIDO")

print("Resultado:", resultado)

