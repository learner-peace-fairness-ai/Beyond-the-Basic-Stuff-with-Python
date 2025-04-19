class WizCoinException(Exception):
    """WizCoin モジュールが誤用された場合にこの例外を発生させる"""
    pass

class WizCoin:
    def __init__(self, galleons, sickles, knuts):
        """galleons, sickles, knuts をセットして WisCoin オブジェクトを作る."""
        self._galleons = galleons
        self._sickles = sickles
        self._knuts = knuts
        # 注意: __init__() メソッドは値を返さない
    
    @property
    def _galleons(self):
        """このオブジェクトのガリオン（galleon）硬貨の数を返す."""
        return self._galleons

    @_galleons.setter
    def _galleons(self, value):
        if not isinstance(value, int):
            raise WizCoinException(f"galleons attr must be set to an int, not a {value.__class__.__qualname__}")
        
        if value < 0:
            raise WizCoinException(f"galleons attr must be a positive int, not {value.__class__.__qualname__}")

        self._galleons = value
    
    @property
    def _sickles(self):
        """このオブジェクトのシックル（sickle）硬貨の数を返す."""
        return self._sickles

    @_sickles.setter
    def _sickles(self, value):
        if not isinstance(value, int):
            raise WizCoinException(f"sickles attr must be set to an int, not a {value.__class__.__qualname__}")
        
        if value < 0:
            raise WizCoinException(f"sickles attr must be a positive int, not {value.__class__.__qualname__}")

        self._sickles = value

    @property
    def _knuts(self):
        """このオブジェクトのクヌート（knut）硬貨の数を返す."""
        return self._knuts

    @_knuts.setter
    def _knuts(self, value):
        if not isinstance(value, int):
            raise WizCoinException(f"knuts attr must be set to an int, not a {value.__class__.__qualname__}")
        
        if value < 0:
            raise WizCoinException(f"knuts attr must be a positive int, not {value.__class__.__qualname__}")

        self._knuts = value

    def __repr__(self):
        """このオブジェクトを再生成する式を文字列で返す."""
        return f"{self.__class__.__qualname__}({self._galleons}, {self._sickles}, {self._knuts})"
    
    def __str__(self):
        """このオブジェクトの内容を人間の読みやすい文字列として返す."""
        return f"{self._galleons}g, {self._sickles}s, {self._knuts}k"

    def value(self):
        """この WizCoin オブジェクトに含まれる全コインの価値（単位は knuts）."""
        return (self._galleons * 17 * 29) + (self._sickles * 29) + (self._knuts)

    def weight_in_grams(self):
        """コインの重さをグラムの単位で返す."""
        return (self._galleons * 31.103) + (self._sickles * 11.34) + (self._knuts * 5.0)

    @property
    def total(self):
        """この WizCoin オブジェクトに含まれる全コインの価値（単位は knuts ）."""
        return (self._galleons * 17 * 29) + (self._sickles * 29) + (self._knuts)
    
    # total には setter メソッドと deleter メソッドがない点に注意
