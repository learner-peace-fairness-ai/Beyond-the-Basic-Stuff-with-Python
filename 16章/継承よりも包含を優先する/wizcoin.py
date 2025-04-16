class WizCoin:
    def __init__(self, galleons, sickles, knuts):
        """galleons, sickles, knuts をセットして WisCoin オブジェクトを作る."""
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
        # 注意: __init__() メソッドは値を返さない

    def value(self):
        """この WizCoin オブジェクトに含まれる全コインの価値（単位は knuts）."""
        return (self.galleons * 17 * 29) + (self.sickles * 29) + (self.knuts)
    
    def weight_in_grams(self):
        """コインの重さをグラムの単位で返す."""
        return (self.galleons * 31.103) + (self.sickles * 11.34) + (self.knuts * 5.0)
