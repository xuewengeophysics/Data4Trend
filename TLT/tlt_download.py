import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# 设置起始日期和结束日期
start_date = datetime(2022, 1, 1)
end_date = datetime.today()

# 每次拉取天数
delta_days = 3

# 用于存储所有数据
all_data = pd.DataFrame()

current_start = start_date

while current_start <= end_date:
    current_end = current_start + timedelta(days=delta_days - 1)
    if current_end > end_date:
        current_end = end_date
    
    # 拉取数据，注意yfinance的end是**不包含**当天，所以要 +1
    data = yf.download('TLT', start=current_start.strftime('%Y-%m-%d'),
                       end=(current_end + timedelta(days=1)).strftime('%Y-%m-%d'))
    
    if not data.empty:
        all_data = pd.concat([all_data, data])
    
    current_start = current_end + timedelta(days=1)

# 去重
all_data = all_data[~all_data.index.duplicated(keep='first')]

# 构造完整日期索引（每天）
full_index = pd.date_range(start=start_date, end=end_date, freq='D')

# 只保留收盘价，并重建索引，缺失用 NaN 填充
close_data = all_data['Close'].reindex(full_index)

# 保存到 CSV
close_data.to_csv('tlt_close_continuous.csv', header=True)

print("TLT 收盘数据（连续日期）已保存到 tlt_close_continuous.csv")
