# import requests
#
# API_KEY = "d61c2872b67dc515b9a30341a5b2c76c"  # 你的 API Key
# CITY = "Beijing"
#
# url = "https://api.openweathermap.org/data/2.5/weather"
# params = {
#     "q": CITY,
#     "appid": API_KEY,
#     "units": "metric"  # 使用摄氏度
# }
#
# try:
#     response = requests.get(url, params=params)
#     response.raise_for_status()  # 如果 HTTP 请求失败，抛出异常
#     data = response.json()
#
#     # 提取需要的信息
#     temp = data["main"]["temp"]
#     feels_like = data["main"]["feels_like"]
#     humidity = data["main"]["humidity"]
#     pressure = data["main"]["pressure"]
#     wind_speed = data["wind"]["speed"]
#     weather_desc = data["weather"][0]["description"].capitalize()  # 首字母大写
#     city_name = data["name"]
#     country = data["sys"]["country"]
#
#     # 打印格式化信息
#     print(f"📍 {city_name}, {country} 天气状况：")
#     print(f"🌡 温度：{temp}°C（体感 {feels_like}°C）")
#     print(f"💧 湿度：{humidity}%")
#     print(f"🌬 风速：{wind_speed} m/s")
#     print(f"🌤 天气：{weather_desc}")
#     print(f"🗜 气压：{pressure} hPa")
#
# except requests.exceptions.HTTPError as errh:
#     print("HTTP 错误：", errh)
# except requests.exceptions.RequestException as err:
#     print("请求失败：", err)
#
# {
#   "coord": {"lon": 116.39, "lat": 39.91},
#   "weather": [{"id": 800, "main": "Clear", "description": "晴天"}],
#   "main": {"temp": 25.6, "feels_like": 26.2},
#   "name": "Beijing"
# }
# # 获取经纬度
# longitude = data["coord"]["lon"]
# latitude = data["coord"]["lat"]
#
# # 获取体感温度
# feels_like = data["main"]["feels_like"]

# import requests
#
# login_url = "https://reqres.in/api/login"
# payload = {
#     "username": "eve.holt@reqres.in",
#     "password": "cityslicka"
# }
#
# # 发送POST请求
# response = requests.post(login_url, data=payload)
#
# # 检查登录是否成功
# if response.status_code == 200:
#     print("登录成功！")
# else:
#     print("登录失败：", response.text)
import requests
def get_api_key():
    # 从文件读取API密钥
    with open("config.txt", "r") as file:
        return file.readline().strip().split('=')[1]

API_KEY = get_api_key()


def get_news(keyword):
    # 构造请求URL
    url = f"https://newsapi.org/v2/everything?q={keyword}&apiKey={API_KEY}"

    try:
        # 发送GET请求
        response = requests.get(url)

        # 检查请求是否成功
        response.raise_for_status()  # 如果状态码不是2xx，会抛出异常

        # 解析JSON数据
        data = response.json()

        if data["status"] == "ok":
            if data["articles"]:
                print(f"找到 {len(data['articles'])} 条关于 '{keyword}' 的新闻：\n")
                # 显示前5条新闻
                for article in data["articles"][:5]:
                    print(f"标题：{article['title']}")
                    print(f"来源：{article['source']['name']}")
                    print(f"发布时间：{article['publishedAt']}")
                    print(f"链接：{article['url']}\n")
            else:
                print(f"没有找到关于 '{keyword}' 的新闻。")
        else:
            print(f"获取新闻失败：{data.get('message', '未知错误')}")

    except requests.exceptions.RequestException as e:
        print(f"请求失败：{e}")
    except ValueError as e:
        print(f"JSON 解析失败：{e}")
    except Exception as e:
        print(f"发生未知错误：{e}")


def main():
    # 获取用户输入
    keyword = input("请输入搜索关键词：")

    if keyword.strip():  # 检查输入不为空
        get_news(keyword)
    else:
        print("关键词不能为空！")


if __name__ == "__main__":
    main()
