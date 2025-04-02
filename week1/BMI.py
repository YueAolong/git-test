def calculate_bmi(weight, height):
    """
    计算 BMI 指数
    :param weight: 体重 (kg)
    :param height: 身高 (m)
    :return: BMI 指数
    """
    return weight / (height ** 2)


def bmi_status(bmi):
    """
    根据 BMI 指数返回健康状态
    :param bmi: 计算出的 BMI 值
    :return: 健康状况字符串
    """
    if bmi < 18.5:
        return "体重过轻"
    elif 18.5 <= bmi < 24.9:
        return "正常范围"
    elif 25 <= bmi < 29.9:
        return "超重"
    elif 30 <= bmi < 34.9:
        return "肥胖（I级）"
    elif 35 <= bmi < 39.9:
        return "肥胖（II级）"
    else:
        return "重度肥胖（III级）"


def main():
    """主函数，用户输入身高体重，计算 BMI 并给出健康状态"""
    try:
        weight = float(input("请输入您的体重(kg)："))
        height = float(input("请输入您的身高(m)："))
        bmi = calculate_bmi(weight, height)
        status = bmi_status(bmi)
        print(f"您的 BMI 指数为: {bmi:.2f}")
        print(f"健康状态: {status}")
    except ValueError:
        print("请输入有效的数值！")


if __name__ == "__main__":
    main()
