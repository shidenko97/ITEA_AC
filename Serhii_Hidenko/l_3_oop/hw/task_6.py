from Serhii_Hidenko.l_3_oop.hw.account import Account


if __name__ == "__main__":

    with Account("Serhii", 1000) as acc:

        del acc._copy_transactions

        acc.add_transaction(30)
        acc.add_transaction(40)
        acc.add_transaction(50)

        acc.print_transactions()
