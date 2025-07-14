import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from utils import calculate_growth_rate, get_data_lists
from ipdb import set_trace


txt_path = "money_supply.txt"
data_lists = get_data_lists(txt_path, 2)
# set_trace()

years = data_lists[0]
data = [round(float(i), 6) for i in data_lists[1]]

growth_rates = calculate_growth_rate(data)
# set_trace()

# 创建图形和坐标轴
fig, ax1 = plt.subplots()

# 绘制原始数据 (左坐标轴)
# ax1.plot(data, marker='o', linestyle='-', color='g', label='money_supply')
bars = ax1.bar(years, data, color='g', label='原始数据', alpha=0.6)
ax1.set_xlabel('Annual')
ax1.set_ylabel('Trillion RMB', color='g')

# 设置左坐标轴的刻度更细
ax1.yaxis.set_major_locator(MaxNLocator(integer=True, prune='lower', nbins=20))

ax1.tick_params(axis='y', labelcolor='g')

# 在柱状图上标注原始数据的数值
for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, height + 5, f'{height}', ha='center', va='bottom', color='r')

# 创建右坐标轴
ax2 = ax1.twinx()
ax2.plot(years, growth_rates, marker='o', linestyle='-', color='b', label='growth_rate')
ax2.set_ylabel('(%)', color='b')
ax2.tick_params(axis='y', labelcolor='b')

# 在每个增长率点上标注数字
for i, value in enumerate(growth_rates):
    if 0 == i:
        continue
    ax2.text(years[i], value, f'{value:.2f}%', ha='center', va='top', color='b')

# 设置图表标题
plt.title("money supply and growth rate")

# 显示图表
fig.tight_layout()
plt.show()