class Bank:
    bank_name: str = "Habib Bank"
    

    @classmethod
    def change_bank_name(cls, name: str)->None:
        cls.bank_name = name
        print(f"The current bank name is: {cls.bank_name}")


bank1 = Bank()

print("\tBefore change:")
print(bank1.bank_name)  # Habib Bank

print("\tAfter change:")
Bank.change_bank_name("Meezan Bank")
print(bank1.bank_name)  # Meezan Bank


