#Módulo emoji
import emoji
from time import sleep
print("FOGOS DE ARTIFÍCIO")

#Estrutura de repetição (loop) for.
for c in range(10, 0, -1):
    print(c), sleep(1)
print(emoji.emojize(":fireworks:"*10))
