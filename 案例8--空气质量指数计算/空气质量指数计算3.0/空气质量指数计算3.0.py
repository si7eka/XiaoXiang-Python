"""
作者：si7eklz
功能：空气质量指数AQI计算
日期：20190219
版本：3.0

案例描述：
    读取已经获取的json数据文件
    将其转化成CSV文件
"""

import json
import csv



def process_json_file(filepath):
    """
        解析json文件
    """
    f = open(filepath, mode='r', encoding='utf-8')
    city_list = json.load(f)
    return city_list


def main():
    """
        主函数
    """
    filepath = input('请输入json文件名称: ')
    city_list = process_json_file(filepath)
    city_list.sort(key=lambda city: city['aqi'])

    lines = []
    # 列名
    lines.append(list(city_list[0].keys()))
    for city in city_list:
        lines.append(list(city.values()))

    f = open('aqi.csv', 'w', encoding='utf-8', newline='')
    writer = csv.writer(f)
    for line in lines:
        writer.writerow(line)

    f.close()
    

if __name__ == '__main__':
    main()

