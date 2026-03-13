from datetime import datetime

def pruef_status(datum):

    heute = datetime.now().date()
    diff = (datum - heute).days

    if diff < 0:
        return "🔴 abgelaufen"
    elif diff < 60:
        return "🟡 bald fällig"
    else:
        return "🟢 ok"
