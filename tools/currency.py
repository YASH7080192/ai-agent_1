import requests


def execute(arguments: dict):

    amount = arguments.get("amount")
    from_currency = arguments.get("from")
    to_currency = arguments.get("to")

    if amount is None or not from_currency or not to_currency:
        return "Currency Error: Missing arguments."

    try:

        url = f"https://open.er-api.com/v6/latest/{from_currency.upper()}"

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        if data.get("result") != "success":
            return "Currency API Error"

        rates = data.get("rates", {})

        if to_currency.upper() not in rates:
            return f"Currency '{to_currency}' not found."

        rate = rates[to_currency.upper()]

        converted = float(amount) * rate

        return (
            f"Amount: {amount} {from_currency.upper()}\n"
            f"Converted: {converted:.2f} {to_currency.upper()}"
        )

    except Exception as e:
        return f"Currency Error: {e}"


if __name__ == "__main__":

    print("===== Currency Tool =====\n")

    result = execute(
        {
            "amount": 100,
            "from": "USD",
            "to": "INR"
        }
    )

    print(result)