import yagmail
from database import cursor
from datetime import datetime

def check_pruefungen():

    cursor.execute("SELECT bezeichnung,tuev FROM fahrzeuge")

    daten = cursor.fetchall()

    heute = datetime.now().date()

    warnungen = []

    for d in daten:

        if d[1]:

            datum = datetime.fromisoformat(d[1]).date()

            diff = (datum - heute).days

            if diff < 30:

                warnungen.append(f"{d[0]} TÜV am {datum}")

    if warnungen:

        yag = yagmail.SMTP("infobav@gmail.com","admin123")

        text = "\n".join(warnungen)

        yag.send(
            to="infobav.koch@gmail.com",
            subject="Inventar Prüfungen fällig",
            contents=text
        )
