from src.cursvalutarbnr import Currency, ron_exchange_rate



eur_to_ron = ron_exchange_rate(
    ammount=1,                    # suma pe care vrei sa o convertesti la 'to_currency'
    to_currency=Currency.EUR      # valuta (curency) in care vrei sa fie convertita suma specificata in 'ammount' 
)

print("eur_to_ron", eur_to_ron)

ron_to_ron = ron_exchange_rate(
    ammount=1, 
    to_currency=Currency.RON, 
    date="2023-04-25"             # poti specifica si data in isoformat pentru care vrei sa fie convertita suma
)

print("ron_to_ron", ron_to_ron)
