class Account:

    def __init__(self, acc_no, holder_name, transactions):

        self.__acc_no = acc_no
        self.__holder_name = holder_name
        self.__transactions = transactions

    def get_name(self):
        return self.__holder_name

    def total_transaction(self):
        return sum(self.__transactions)

    def average_transaction(self):

        if len(self.__transactions) == 0:
            return 0

        return sum(self.__transactions) / len(self.__transactions)

    def suspicious_transactions(self):

        frauds = []

        for amt in self.__transactions:

            if amt > 100000:
                frauds.append(amt)

        return frauds

    def negative_balance_risk(self):

        if sum(self.__transactions) < 0:
            return True

        return False


n = int(input())

accounts = []

highest_volume = 0
top_account = ""

negative_count = 0

for i in range(n):

    acc_no = input()

    holder_name = input()

    transactions = list(map(int, input().split()))

    acc = Account(acc_no, holder_name, transactions)

    accounts.append(acc)

    total = acc.total_transaction()

    if total > highest_volume:
        highest_volume = total
        top_account = acc.get_name()

    if acc.negative_balance_risk():
        negative_count += 1


print("Fraud Alerts:")

for acc in accounts:

    frauds = acc.suspicious_transactions()

    if frauds:

        print(acc.get_name(), "->", frauds)


print("Average Transactions:")

for acc in accounts:

    print(
        acc.get_name(),
        "-",
        round(acc.average_transaction(), 2)
    )


print("Negative Balance Risk Accounts:", negative_count)

print("Highest Transaction Volume Account:")
print(top_account, "-", highest_volume)