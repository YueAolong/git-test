# import matplotlib
# import pandas as pd
#
# matplotlib.use('TkAgg')  # 设置交互式后端，若报错可改为 'Qt5Agg'
#
# import seaborn as sns
# import matplotlib.pyplot as plt
#
# # 解决中文字体问题
# matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
# matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
#
# # 加载 Seaborn 自带数据集
# tips = sns.load_dataset('tips')
# #
# # # 1️⃣ 绘制每日消费金额分布（箱线图）
# # plt.figure(figsize=(8, 6))  # 设置图形大小
# # sns.boxplot(x='day', y='total_bill', data=tips)
# # plt.title('每日消费金额分布')
# # plt.show()
# #
# # # 2️⃣ 绘制特征相关性热力图
# # plt.figure(figsize=(8, 6))
# # correlation = tips.corr(numeric_only=True)  # 需要加 `numeric_only=True` 以避免 Pandas 警告
# # sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
# # plt.title("特征相关性热力图")
# # plt.show()
# #
# # # 3️⃣ 绘制小费与总消费的关系（联合分布图）
# # sns.jointplot(x="total_bill", y="tip", data=tips, kind="scatter", height=6)
# # plt.show()
# import plotly.express as px
# import numpy as np
#
# fig = px.scatter(tips, x='total_bill', y='tip',
#                  color='time', size='size',
#                  title='消费金额与消费关系')
# fig.show()
#
# dates = pd.date_range(start='2024-01-01', periods=50)
# sales = pd.DataFrame({
#     'date': dates,
#     'sales': np.random.randint(100, 500, 50)
# })
#
# fig = px.line(sales, x='date', y='sales',
#               title='每日销售额趋势',
#               markers=True)
# fig.update_xaxes(rangeslider_visible=True)
# fig.show()
#
# from sklearn.datasets import load_iris
# iris = load_iris()
# df_iris = pd.DataFrame(iris.data, columns=iris.feature_names)
# df_iris['species'] = iris.target_names[iris.target]
#
# fig = px.scatter_3d(df_iris,
#                     x='sepal length (cm)',
#                     y='sepal width (cm)',
#                     z='petal length (cm)',
#                     color='species')
# fig.show()
#
# import pandas as pd
# import plotly.graph_objects as go
# from plotly.subplots import make_subplots
#
# sales_data = pd.DataFrame({
#     'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
#     'Revenue': [12000, 15000, 9000, 18000, 20000],
#     'Profit': [3000, 4500, 2000, 6000, 7500],
#     'Product': ['A', 'B', 'A', 'C', 'B']
# })
#
# fig = make_subplots(
#     rows=2, cols=2,
#     specs=[[{'type': 'bar'}, {'type': 'pie'}],
#            [{'type': 'scatter', 'colspan': 2},None]],
#     subplot_titles=('月度营收', '产品占比', '利润趋势')
# )
# fig.add_trace(go.Bar(x=sales_data['Month'], y=sales_data['Revenue']),
#               row=1, col=1)
#
# fig.add_trace(go.Pie(labels=sales_data['Product'], values=sales_data['Revenue']),
#               row=1, col=2)
#
# fig.add_trace(go.Scatter(x=sales_data['Month'], y=sales_data['Profit'],mode='lines+markers'),
#               row=2, col=1)
#
# fig.update_layout(height=800, width=1000, title_text='销售仪表盘')
# fig.show()
import pandas as pd
import plotly.express as px
import pycountry

# 1. 读取数据
url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/" \
      "csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
covid_data = pd.read_csv(url)

# 2. 删除无关的列
covid_data_grouped = covid_data.drop(columns=['Province/State', 'Lat', 'Long'], errors='ignore')

# 3. 按国家汇总
covid_data_grouped = covid_data_grouped.groupby('Country/Region').sum()

# 4. 转置数据，使日期成为行索引
covid_data_transposed = covid_data_grouped.transpose()
covid_data_transposed.index.name = "Date"
covid_data_transposed.reset_index(inplace=True)

# 5. ✅ 解决警告：指定日期格式
covid_data_transposed['Date'] = pd.to_datetime(
    covid_data_transposed['Date'],
    format="%m/%d/%y",  # 适配JHU数据
    errors='coerce'
)

# 6. 选择关注的国家
countries = ['US', 'India', 'Brazil', 'Russia', 'France', 'China']
covid_data_filtered = covid_data_transposed[['Date'] + [c for c in countries if c in covid_data_transposed.columns]]

# 7. 绘制各国累计确诊趋势折线图
fig = px.line(covid_data_filtered, x='Date', y=countries, labels={'value': '累计确诊病例', 'variable': '国家'},
              title='各国累计确诊趋势')
fig.show()
