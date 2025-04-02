from user_validation import validate_username, validate_password


username = input('请输入用户名：')
password = input('请输入密码：')


if validate_username(username):
    print("√ 用户名有效")
else:
    print('× 用户名无效，必须是3-20个字符，并且只能包含字母、数字和下划线！')

if validate_password(password):
    print('√ 密码有效')
else:
    print('× 密码无效，密码至少八位，且必须包含1个大写字母和一个数字！')
