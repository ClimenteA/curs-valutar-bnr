from cursvalutarbnr import Currency, ron_exchange_rate


ron_to_eur = ron_exchange_rate(
    ammount=1,                    # suma pe care vrei sa o convertesti din 'from_currency' la 'to_currency'
    from_currency=Currency.RON,   # valuta (curency) corespunzatoare pentru ammount 
    to_currency=Currency.EUR      # valuta (curency) in care vrei sa fie convertita suma specificata in 'ammount' 
)

print("ron_to_eur", ron_to_eur)

eur_to_ron = ron_exchange_rate(
    ammount=1, 
    from_currency=Currency.EUR, 
    to_currency=Currency.RON, 
    date="2023-04-25"             # poti specifica si data in isoformat pentru care vrei sa fie convertita suma
)

print("eur_to_ron", eur_to_ron)