import datetime
from urllib import request

class CheckHoliday:
  """CheckHoliday

  内閣府発表の祝日リストまたは指定したファイルを元に祝日かどうかを判定する機能を提供する。
  国民の祝日を判定する場合はインターネット接続が必要。

  Attributes:
    GOVERMENT_CSV_URL (str): 内閣府が配布している国民の祝日リストのurl

  TODO:
    * インスタンス化して特定のファイルやurlをソースとできるようにする
  """
  GOVERMENT_CSV_URL = 'https://www8.cao.go.jp/chosei/shukujitsu/syukujitsu.csv'

  @classmethod
  def today_is_holiday(cls) -> bool:
    """today_is_holiday
    今日が国民の祝日かを確認する
    
    Return:
      bool: 祝日ならTrue、そうでないならFalseを返す
    """
    today = datetime.date.today()
    return cls.the_day_is_holiday(today)
    
  @classmethod
  def the_day_is_holiday(cls, date: datetime.date) -> bool:
    """the_day_is_holiday
    指定された日が国民の祝日かを確認する
    
    Args:
      date (datetime.date): 判定する日付

    Return:
      bool: 祝日ならTrue、そうでないならFalseを返す
    """
    holidays = None
    with request.urlopen(cls.GOVERMENT_CSV_URL) as res:
      holidays = res.read().decode('shift_jis')
    return f"{date.year}/{date.month}/{date.day}" in holidays

  def __init__(self):
    pass


if __name__ == "__main__":
    today = datetime.date.today().strftime('%Y/%m/%d')
    print(f"today is {today}")
    is_holiday = CheckHoliday.today_is_holiday()
    print(is_holiday)
    holiday = datetime.datetime.strptime("2023/09/23", "%Y/%m/%d")
    is_holiday = CheckHoliday.the_day_is_holiday(holiday)
    print(is_holiday)
