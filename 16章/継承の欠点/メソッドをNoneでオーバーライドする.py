class Vehicle:
    def __init__(self):
        print("乗り物を生成しました。")
    
    def start_ignition(self):
        pass  # エンジンスタートの処理はここに書く

    def change_tire(self):
        pass  # タイヤ交換の処理はここに書く

    def change_spark_plug(self):
        pass  # 点火プラグの変更に関する処理はここに書く


class Car(Vehicle):
    def __init__(self):
        print("自動車を生成しました。")


class Motorcycle(Vehicle):
    def __init__(self):
        print("オートバイを生成しました。")


class LunarRover(Vehicle):
    change_spark_plug = None

    def __init__(self):
        print("月面探査機を生成しました。")


my_vehicle = LunarRover()
my_vehicle.change_spark_plug()  # None を呼び出すのでエラーになる
