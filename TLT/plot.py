import pandas as pd
import matplotlib.pyplot as plt
from ipdb import set_trace

# ---------- 1. 读取原始 CSV ----------
input_csv = 'TLT_2022-01-01_.csv'   # 你的原始文件
df = pd.read_csv(input_csv, parse_dates=['Date'])
# set_trace()

# ---------- 2. 设置日期为索引 ----------
df.set_index('Date', inplace=True)

# ---------- 3. 构造连续日期索引 ----------
full_index = pd.date_range(start=df.index.min(), end=df.index.max(), freq='D')
df_continuous = df.reindex(full_index)

# ---------- 4. 填充 ----------
df_continuous['Close'] = df_continuous['Close'].fillna(method='ffill')

# ---------- 5. 保存连续日期 CSV ----------
output_csv = 'tlt_close_continuous.csv'
df_continuous.to_csv(output_csv, header=True)
print(f"连续日期 CSV 已保存: {output_csv}")

# ---------- 6. 绘图 ----------
plt.figure(figsize=(12,6))
plt.plot(df_continuous.index, df_continuous['Close'], color='blue', linewidth=2)
plt.title('TLT', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Close (USD)', fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()
