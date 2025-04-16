import wizcoin


class WizardCustomer(wizcoin.WizCoin):
    def __init__(self, name):
        self.name = name
        super().__init__(0, 0, 0)


wizard = WizardCustomer("Alice")
print(f"{wizard.name} は {wizard.value()} クヌートのお金を持っています。")
print(f"{wizard.name} が持っている硬貨は {wizard.weight_in_grams()} グラムです。")
