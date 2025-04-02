# import matplotlib
# matplotlib.use('TkAgg')  # 切换到 TkAgg 后端
#
# import matplotlib.pyplot as plt
#
#
# # 设置字体为微软雅黑
# matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 微软雅黑
# matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
#
# # 画图
# plt.plot([1, 2, 3], [4, 5, 6])
# plt.title('中文标题：电影评分分布')  # 中文标题
# plt.xlabel('评分')  # 中文标签
# plt.ylabel('数量')  # 中文标签
# plt.show()
# 抓取数据部分


import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')  # 切换到 TkAgg 后端

matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

url = "http://www.weather.com.cn/weather/101010100.shtml"
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(response.content, 'html.parser')

weather_data = []
for item in soup.select('.sky'):
    date = item.select_one('h1').text
    temp = item.select_one('.tem').text.strip()
    weather_data.append({'日期': date, '温度': temp})

# 数据清洗
df = pd.DataFrame(weather_data)
df['最高温'] = df['温度'].str.extract('(\d+)℃').astype(int)
df['最低温'] = df['温度'].str.extract('/(\d+)℃').astype(int)

# 保存数据
df.to_csv('weather.csv', index=False, encoding='utf-8-sig')

# 可视化
plt.plot(df['日期'], df['最高温'], label='最高温')
plt.plot(df['日期'], df['最低温'], label='最低温')
plt.legend()
plt.show()