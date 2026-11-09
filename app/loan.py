def monthly_payment(principal, annual_rate, months):
    r = annual_rate / 12
    n = months

    if n <= 0:
        raise ValueError("le nb de mois doit etre superieur a 0")
    elif r == 0:
        mensualite = principal / n
    else:
        mensualite = principal * r / (1 - (1 + r) ** (-n))

    return mensualite