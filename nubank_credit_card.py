import csv
from datetime import datetime
import yaml


if __name__ == '__main__':
    transactions = []
    with open('resources/nubank_credit_card/nubank-2021-10.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            print(row)
            parsed_datetime = datetime.strptime(row['date'], '%Y-%m-%d')
            formatted_datetime = parsed_datetime.strftime('%Y-%m-%d')
            value = float(row['amount'])

            accounts = ['some_expense', 'nubank_credit_card']
            if value < 0:
                accounts = ['nubank_credit_card', 'maybe_credit_card_paid']

            transactions.append({
                'date': formatted_datetime,
                'description': row['title'],
                'value': abs(value),
                'accounts': accounts
            })

    transactions.sort(key=lambda x: [x['date'], x['description'], x['value']])

    print(yaml.dump(transactions, explicit_start=True, sort_keys=False, width=240, allow_unicode=True))
