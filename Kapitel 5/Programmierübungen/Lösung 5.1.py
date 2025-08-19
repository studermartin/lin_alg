"""
Simulation des Verhaltens des Geysiers
"""

# Aufgabe 1: Von Hand

"""
	Simuliere von Hand eine Markov-Kette der Länge 20 (hier eine der Länge 10: LKLLLKLKLL), die mit einer langen Wartezeit (L) beginnt.
	Um zu simulieren, ob nach einer langen Wartezeit eine kurze Wartezeit erfolgt, nutze folgendes kleines Python-Programm mehrmals:

    from random import random
    print("after a long waiting time: ")
    if random() < 0.536:
        print("a short waiting time")
    else:
        print("a long waiting time")

    Berechne die Wahrscheinlichkeit für eine kurze und eine lange Wartezeit basierend auf der Simulation.
"""

"""
    Beispiel für die Wartezeiten:
    LKLKLLLKLLKLLLKLLLKL

    Anzahl kurzer Wartezeiten: 6
    Anzahl langer Wartezeiten: 14  
    Wahrscheinlichkeit kurzer Wartezeiten: 6/20 = 0.3
    Wahrscheinlichkeit langer Wartezeiten: 14/20 = 0.7     
"""


# Aufgabe 2: Simulation

"""
   Simuliere den Markov-Prozess mit einem Python-Programm.
   Nutze eine Schleife, um die Kette zu simulieren. Zähle die Anzahl der kurzen und langen Wartezeiten.
   Gib die Wahrscheinlichkeiten für kurze und lange Wartezeiten aus.
"""

from random import random

LONG = 0
SHORT = 1

count = 0
count_long = 0
count_short = 0
current = LONG
while count <10000:
    if current == LONG:
        if random() < 0.536:
            current = SHORT
            count_short += 1
        else:
            current = LONG
            count_long += 1
    else: # last == SHORT
        current = LONG
        count_long += 1
    count += 1

print(f"Probability long waiting time: {count_long/count}")
print(f"Probability short waiting time: {count_short/count}")
