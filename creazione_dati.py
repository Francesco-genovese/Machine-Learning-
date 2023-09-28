import random
import csv

semi = ['Cuori', 'Quadri', 'Fiori', 'Picche']
valori = ['Asso', 'Due', 'Tre', 'Quattro', 'Cinque', 'Sei', 'Sette', 'Otto', 'Nove', 'Dieci', 'Fante', 'Regina', 'Re']

numero_di_righe = 1000  # Modifica questo valore per il numero di righe desiderato

with open('dati_carte.csv', mode='w', newline='') as file_csv:
    writer = csv.writer(file_csv)
    writer.writerow(['Nome', 'Carta_Scelta', 'Punteggio'])

    for _ in range(numero_di_righe):
        nome = random.choice(['Alice', 'Bob', 'Carol', 'David', 'Eva', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack'])
        carta_scelta = random.choice(valori) + " di " + random.choice(semi)
        punteggio = random.randint(1, 10)
        writer.writerow([nome, carta_scelta, punteggio])

print(f"{numero_di_righe} righe di dati sono state generate e salvate nel file 'dati_carte.csv'.")
 
