from pprint import pprint

import yaml


def open_ledger():
    with open('ledger.yml') as file:
        return yaml.load(file, Loader=yaml.FullLoader)


def balance(transactions):
    report = {}
    for transaction in transactions:
        acc1: str = transaction['accounts'][0]
        acc2: str = transaction['accounts'][1]
        report[acc1] = report.get(acc1, 0) + transaction['value']
        report[acc2] = report.get(acc2, 0) - transaction['value']
    return report


if __name__ == '__main__':
    ledger = open_ledger()
    pprint(balance(ledger['transactions']))
