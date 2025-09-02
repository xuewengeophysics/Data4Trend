import time
import datetime

def date_to_timestamp(date_str: str) -> int:
    """
    将日期字符串 (YYYY-MM-DD) 转换为 Unix 时间戳 (秒)
    适用于 Yahoo Finance 的 period1 / period2 参数
    """
    dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    return int(time.mktime(dt.timetuple()))

# 示例
print(date_to_timestamp("2022-01-01"))  # 1751472000
