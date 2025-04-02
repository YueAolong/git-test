# # import requests
# #
# # url = 'https://www.example.com'
# # response = requests.get(url)
# # print('状态码：',response.status_code)
# # print('网页内容：', response.text[:500])
# #
# #
# # from bs4 import BeautifulSoup
# #
# # soup = BeautifulSoup(response.text, 'html.parser')
# # print('网页标题：', soup.title.text)
# #
# # paragraphs = soup.find_all('p')
# # for p in paragraphs[:3]:
# #     print(p.text.strip())
#
# import requests
# from bs4 import BeautifulSoup
#
# url = 'https://movie.douban.com/top250'
# headers = {'User-Agent': 'Mozilla/5.0'}
#
# response = requests.get(url, headers=headers)
# soup = BeautifulSoup(response.text, 'html.parser')
#
# movies = []
# for item in soup.select('.item'):
#     title = item.select_one('.title').text
#     rating = item.select_one('.rating_num').text
#
# print('前五部电影：')
# for movie in movies[0:5]:
#     print(f'{movie["title"]} | 评分：{movie["rating"]}')
#
#
import requests
from bs4 import BeautifulSoup
import random
import time
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')  # 切换到 TkAgg 后端


# 1️⃣ 随机 User-Agent，降低被封风险
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
]

# 2️⃣ 伪装请求头
headers = {
    'User-Agent': random.choice(USER_AGENTS),
    'Referer': 'https://www.douban.com/',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

# 3️⃣ 爬取所有页面的电影
movies = []
base_url = "https://movie.douban.com/top250"

for page in range(0, 250, 25):  # 每页25条，共10页（0, 25, 50, ..., 225）
    url = f"{base_url}?start={page}"

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        time.sleep(random.uniform(3, 5))  # 休息后重试
        continue  # 跳过当前页，尝试下一页

    # 解析HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # 提取电影数据
    for item in soup.select('.item'):
        title_tag = item.select_one('.title')
        rating_tag = item.select_one('.rating_num')

        if title_tag and rating_tag:
            title = title_tag.text.strip()
            rating = rating_tag.text.strip()
            movies.append({'title': title, 'rating': rating})

    print(f"✅ 成功爬取 {page + 1} - {page + 25} 部电影")

    # 随机暂停，防止被封
    time.sleep(random.uniform(1, 3))

# 4️⃣ 存储数据
df = pd.DataFrame(movies)
df['rating'] = df['rating'].astype(float)

df.to_csv('douban_top250.csv', index=False, encoding='utf-8-sig')
print("\n🎉 数据已保存为 douban_top250.csv")

# 5️⃣ 计算评分统计信息
print("\n📊 评分统计：")
print(f"平均分：{df['rating'].mean():.2f}")
print(f"最高分：{df['rating'].max()}")

# 6️⃣ 绘制评分分布图

matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
plt.figure(figsize=(8, 5))
plt.hist(df['rating'], bins=10, edgecolor='black', color='skyblue')
plt.title('电影评分')
plt.xlabel('评分')
plt.ylabel('数量')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
