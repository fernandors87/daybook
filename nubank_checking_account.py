import csv
from datetime import datetime
import yaml


if __name__ == '__main__':
    transactions = []
    with open('resources/nubank_checking_account/NU_89683218_01OUT2021_31OUT2021.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            parsed_datetime = datetime.strptime(row['Data'], '%d/%m/%Y')
            formatted_datetime = parsed_datetime.strftime('%Y-%m-%d')
            value = float(row['Valor'])

            accounts = ['nubank', 'unknown']
            if value < 0:
                accounts = ['unknown', 'nubank']

            transactions.append({
                'date': formatted_datetime,
                'description': row['Descrição'],
                'value': abs(value),
                'accounts': accounts
            })

    transactions.sort(key=lambda x: [x['date'], x['description'], x['value']])

    print(yaml.dump(transactions, explicit_start=True, sort_keys=False, width=240, allow_unicode=True))
