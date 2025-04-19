from collections.abc import Sequence
import operator


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

    def __repr__(self):
        """このオブジェクトを再生成する式を文字列で返す."""
        return f"{self.__class__.__qualname__}({self._galleons}, {self._sickles}, {self._knuts})"

    def __str__(self):
        """このオブジェクトの内容を人間の読みやすい文字列として返す."""
        return f"{self._galleons}g, {self._sickles}s, {self._knuts}k"

    def __add__(self, other):
        """2つの WizCoin オブジェクトの硬貨を合計する."""
        if not isinstance(other, WizCoin):
            return NotImplemented

        return WizCoin(
            other.galleons + self._galleons,
            other.sickles + self._sickles,
            other.knuts + self._knuts,
        )

    def __iadd__(self, other):
        """別の WizCoin オブジェクトの金額をこのオブジェクトに加える."""
        if not isinstance(other, WizCoin):
            return NotImplemented

        # self オブジェクトを変更するように修正する
        self._galleons += other.galleons
        self._sickles += other.sickles
        self._knuts += other.knuts
        return self  # 代入型ダンダ―メソッドは、ほとんどの場合 self を返す

    def __sub__(self, other):
        """2つの WizCoin オブジェクトの差分を計算する(self - other)."""
        if not isinstance(other, WizCoin):
            return NotImplemented

        return WizCoin(
            self._galleons - other.galleons,
            self._sickles - other.sickles,
            self._knuts - other.knuts,
        )

    def __mul__(self, other):
        """各硬貨の数に非負数を掛ける."""
        if not isinstance(other, int):
            return NotImplemented

        if other < 0:
            # 負の整数を掛けると硬貨の数が負になってしまうので無効とする
            raise WizCoinException("負の数を掛けてはいけない")

        return WizCoin(
            self._galleons * other, self._sickles * other, self._knuts * other
        )

    def __rmul__(self, other):
        """硬貨の数に非負数を掛ける."""
        return self.__mul__(other)

    def __imul__(self, other):
        """このオブジェクトの galleons, sickels, knuts に非負数を掛ける."""
        if not isinstance(other, int):
            return NotImplemented

        if other < 0:
            raise WizCoinException("負の数を掛けてはいけない")

        # WizCoin クラスは可変型のオブジェクトを生成する。
        # したがって、↓のコードのように新たなオブジェクトを生成してはいけない。
        # return WizCoin(self._galleons * other, self._sickles * other, self._knuts * other)

        # self オブジェクトを変更するように修正する。
        self._galleons *= other
        self._sickles *= other
        self._knuts *= other
        return self  # 代入型ダンダ―メソッドは、ほとんどの場合 self を返す

    def __pow__(self, other):
        """各硬貨の数をべき乗する."""
        coins_is_integer = [
            (c**other).is_integer()
            for c in [self._galleons, self._sickles, self._knuts]
        ]
        if not all(coins_is_integer):
            # 計算結果が正の整数でなければ無効とする
            raise WizCoinException("べき乗が整数でなければいけない")

        return WizCoin(self._galleons**other, self._sickles**other, self._knuts**other)

    def __int__(self):
        """この WizCoin オブジェクトに含まれる全コインの硬貨の数を返す."""
        return self._galleons + self._sickles + self._knuts

    def __float__(self):
        """コインの重さをグラムの単位で返す."""
        return self.weight_in_grams()

    def __bool__(self):
        """コインが1枚以上なら True を返す."""
        return int(self) > 0

    def __eq__(self, other):  # eq は"EQUAL(==)"
        return self._comparison_operator_helper(operator.eq, other)

    def __ne__(self, other):  # ne は"Not Equal(!=)"
        return self._comparison_operator_helper(operator.ne, other)

    def __lt__(self, other):  # lt は"Less Than(<)"
        return self._comparison_operator_helper(operator.lt, other)

    def __le__(self, other):  # le は"Less than or Equal(<=)"
        return self._comparison_operator_helper(operator.le, other)

    def __gt__(self, other):  # gt は"Greater Than(>)"
        return self._comparison_operator_helper(operator.gt, other)

    def __ge__(self, other):  # ge は"Greater than or Equal(>=)"
        return self._comparison_operator_helper(operator.ge.other)

    @property
    def galleons(self):
        """このオブジェクトのガリオン（galleon）硬貨の数を返す."""
        return self._galleons

    @galleons.setter
    def galleons(self, value):
        if not isinstance(value, int):
            raise WizCoinException(
                f"galleons attr must be set to an int, not a {value.__class__.__qualname__}"
            )

        if value < 0:
            raise WizCoinException(
                f"galleons attr must be a positive int, not {value.__class__.__qualname__}"
            )

        self._galleons = value

    @property
    def sickles(self):
        """このオブジェクトのシックル（sickle）硬貨の数を返す."""
        return self._sickles

    @sickles.setter
    def sickles(self, value):
        if not isinstance(value, int):
            raise WizCoinException(
                f"sickles attr must be set to an int, not a {value.__class__.__qualname__}"
            )

        if value < 0:
            raise WizCoinException(
                f"sickles attr must be a positive int, not {value.__class__.__qualname__}"
            )

        self._sickles = value

    @property
    def knuts(self):
        """このオブジェクトのクヌート（knut）硬貨の数を返す."""
        return self._knuts

    @knuts.setter
    def knuts(self, value):
        if not isinstance(value, int):
            raise WizCoinException(
                f"knuts attr must be set to an int, not a {value.__class__.__qualname__}"
            )

        if value < 0:
            raise WizCoinException(
                f"knuts attr must be a positive int, not {value.__class__.__qualname__}"
            )

        self._knuts = value

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

    def _comparison_operator_helper(self, operator_func, other):
        """比較ダンダ―メソッド用のヘルパーメソッド."""
        if isinstance(other, WizCoin):
            return operator_func(self.total, other.total)
        elif isinstance(other, (int, float)):
            return operator_func(self.total, other)
        elif isinstance(other, Sequence):
            other_value = (other[0] * 17 * 29) + (other[1] * 29) + other[2]
            return operator_func(self.total, other_value)
        elif operator_func == operator.eq:
            return False
        elif operator_func == operator.ne:
            return True
        else:
            return NotImplemented

    # total には setter メソッドと deleter メソッドがない点に注意


one_galleon = WizCoin(1, 0, 0)  # 493クヌートの価値
one_sickle = WizCoin(0, 1, 0)  # 29クヌートの価値
one_knut = WizCoin(0, 0, 1)  # 1クヌートの価値
coins = [one_sickle, one_knut, one_galleon]
coins.sort()  # 価値の小さい順にソートする
print(coins)
