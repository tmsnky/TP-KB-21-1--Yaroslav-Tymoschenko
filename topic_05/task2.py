import requests

def convert_currency(amount, currency):
    api_url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        exchange_rates = response.json()
        for rate in exchange_rates:
            if rate["cc"] == currency:
                converted_amount = amount * rate["rate"]
                return converted_amount, "UAH"
        return None, None
    else:
        print("Error fetching exchange rates.")
        return None, None


amount = float(input("Enter the amount: "))
currency = input("Enter the currency (EUR/USD/PLN): ").upper()

converted_amount, target_currency = convert_currency(amount, currency)

if converted_amount is not None:
    print(f"{amount} {currency} is equal to {converted_amount:.2f} {target_currency}")
else:
    print("Conversion failed.")