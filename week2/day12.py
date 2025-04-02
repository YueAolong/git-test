import re

pattern = r'hello'
text = 'hello world'

result = re.match(pattern, text)
if result:
    print('找到匹配：', result.group())
else:
    print('为找到匹配')

text = 'Contact: 123-456-7890'
pattern = r'\d{3}-\d{3}-\d{4}'

result = re.search(pattern, text)
if result:
    print('找到号码：', result.group())

text = '苹果价格：￥5.5，橡胶价格：￥3.0'
pattern = r'￥(\d+\.\d+)'

prices = re.findall(pattern, text)
print('所有价格：', prices)


text = '2024-05-20'
new_text = re.sub(r'-', '/', text)
print(new_text)


def validate_email(email):
    pattern = r'^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$'
    return re.match(pattern, email) is not None


print(validate_email('test@example.com'))
print(validate_email('invalid.email@com'))

html = '<a href="https://www.example.com">Example</a>'
pattern = r'href="(https?://.*?)"'

links = re.findall(pattern, html)
print('提取的链接：', links)


text = '联系方式：18637247945'
pattern = r'(\d{3})\d{4}(\d{4})'

hidden = re.sub(pattern, r'\1****\2', text)
print(hidden)


import re


def validate_id_card(id_card):
    pattern = r'^\d{17}[\dXx]$'

    if not re.match(pattern, id_card):
        return False, '身份证号格式错误'

    birth_year = id_card[6:10]
    birth_month = id_card[10:12]
    birth_day = id_card[12:14]

    return True, f'出生日期：{birth_year}-{birth_month}-{birth_day}'


print(validate_id_card('410527199901142415'))
print(validate_id_card('41052719990114241x'))
print(validate_id_card('41052719990114241'))
