from datetime import date

birthday = date(1999, 10, 31)  # 年、月、日を渡す
print(birthday.year)
print(birthday.month)
print(birthday.day)
print(birthday.weekday())  # weekday() はメソッドなので忘れずに () を付ける
