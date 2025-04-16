import wizcoin


class WizardCustomer(wizcoin.WizCoin):
    def __init__(self, name):
        self.name = name
        self.purse = wizcoin.WizCoin(0, 0, 0)


wizard = WizardCustomer("Alice")
print(f"{wizard.name} は {wizard.purse.value()} クヌートのお金を持っています。")
print(f"{wizard.name} が持っている硬貨は {wizard.purse.weight_in_grams()} グラムです。")
