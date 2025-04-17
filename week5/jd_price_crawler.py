import requests
from bs4 import BeautifulSoup
import csv
import time
import random
import logging
from fake_useragent import UserAgent
from datetime import datetime
import os

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("jd_crawler.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class JDPriceCrawler:
    def __init__(self, max_retries=3, timeout=10, delay_range=(1, 3)):
        """
        初始化爬虫
        
        参数:
            max_retries (int): 最大重试次数
            timeout (int): 请求超时时间(秒)
            delay_range (tuple): 请求间隔范围(秒)
        """
        self.max_retries = max_retries
        self.timeout = timeout
        self.delay_range = delay_range
        self.ua = UserAgent()
        self.session = requests.Session()
        
    def get_random_headers(self):
        """生成随机请求头"""
        return {
            'User-Agent': self.ua.random,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0',
        }
    
    def random_delay(self):
        """随机延迟一段时间"""
        delay = random.uniform(self.delay_range[0], self.delay_range[1])
        logger.debug(f"等待 {delay:.2f} 秒...")
        time.sleep(delay)
    
    def get_product_price(self, product_id):
        """
        获取商品价格
        
        参数:
            product_id (str): 商品ID
            
        返回:
            dict: 包含商品信息的字典，如果失败则返回None
        """
        url = f"https://item.jd.com/{product_id}.html"
        
        for attempt in range(self.max_retries):
            try:
                logger.info(f"正在获取商品 {product_id} 的价格 (尝试 {attempt+1}/{self.max_retries})")
                
                # 随机延迟
                self.random_delay()
                
                # 发送请求
                response = self.session.get(
                    url, 
                    headers=self.get_random_headers(), 
                    timeout=self.timeout
                )
                
                # 检查响应状态
                if response.status_code != 200:
                    logger.warning(f"请求失败，状态码: {response.status_code}")
                    continue
                
                # 解析HTML
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # 获取商品标题
                title = soup.select_one('.sku-name')
                title = title.text.strip() if title else "未知商品"
                
                # 获取商品价格 (京东价格是通过API获取的，这里模拟一下)
                # 实际项目中，你可能需要调用京东的价格API
                price_api_url = f"https://p.3.cn/prices/mgets?skuIds=J_{product_id}"
                price_response = self.session.get(
                    price_api_url, 
                    headers=self.get_random_headers(), 
                    timeout=self.timeout
                )
                
                if price_response.status_code == 200:
                    try:
                        price_data = price_response.json()
                        if price_data and len(price_data) > 0:
                            price = price_data[0].get('p', '未知价格')
                        else:
                            price = '未知价格'
                    except ValueError:
                        price = '解析失败'
                else:
                    price = '获取失败'
                
                # 获取当前时间
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                # 返回结果
                return {
                    'product_id': product_id,
                    'title': title,
                    'price': price,
                    'crawl_time': current_time
                }
                
            except requests.exceptions.Timeout:
                logger.warning(f"请求超时 (尝试 {attempt+1}/{self.max_retries})")
            except requests.exceptions.RequestException as e:
                logger.error(f"请求异常: {e}")
            except Exception as e:
                logger.error(f"未知错误: {e}")
        
        logger.error(f"获取商品 {product_id} 价格失败，已达到最大重试次数")
        return None
    
    def crawl_products(self, product_ids, output_file='jd_prices.csv'):
        """
        爬取多个商品的价格并保存到CSV
        
        参数:
            product_ids (list): 商品ID列表
            output_file (str): 输出CSV文件名
        """
        # 检查文件是否存在，决定是否写入表头
        file_exists = os.path.isfile(output_file)
        
        with open(output_file, 'a', newline='', encoding='utf-8-sig') as f:
            writer = csv.DictWriter(f, fieldnames=['product_id', 'title', 'price', 'crawl_time'])
            
            # 如果文件不存在，写入表头
            if not file_exists:
                writer.writeheader()
            
            # 爬取每个商品
            for product_id in product_ids:
                result = self.get_product_price(product_id)
                if result:
                    writer.writerow(result)
                    logger.info(f"成功获取商品 {product_id} 的价格: {result['price']}")
                else:
                    logger.error(f"无法获取商品 {product_id} 的价格")
        
        logger.info(f"爬取完成，结果已保存到 {output_file}")

def main():
    # 示例商品ID列表
    product_ids = ['100012043978']
    
    # 创建爬虫实例
    crawler = JDPriceCrawler(max_retries=3, timeout=10, delay_range=(1, 3))
    
    # 开始爬取
    crawler.crawl_products(product_ids)

if __name__ == "__main__":
    main() 