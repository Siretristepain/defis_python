from datetime import date, timedelta

# Dictionnaire qui lie les indices des jours de la semaine aux nombre de lettres des jours de la semaine
week = {
    0 : 5,
    1 : 5,
    2 : 8,
    3 : 5,
    4 : 8,
    5 : 6,
    6 : 8,
}

start_date = date(2000, 1, 1)
end_date = date.today()

delta = end_date - start_date
nb_magical_days = 0

for i in range(delta.days + 1):
    day = start_date + timedelta(days=i)

    if (day.day + week[day.weekday()]) % 10 == 0:
        nb_magical_days += 1

print(f"Depuis le 1er janvier 2000 a aujourd'hui, il y a eu {nb_magical_days} jours magiques.")
# Depuis le 1er janvier 2000 a aujourd'hui, il y a eu 926 jours magiques.
