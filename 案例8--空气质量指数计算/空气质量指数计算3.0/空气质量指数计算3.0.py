"""
作者：si7eklz
功能：空气质量指数AQI计算
日期：20190219
版本：3.0

案例描述：
    读取已经获取的json数据文件
    将其转化成CSV文件

json库
    json库是处理json格式的Python标准库
    两个过程：
        编码（encoding），将Python数据类型装换成json格式的过程
        解码（decoding），从json格式中解析书记对应到Python数据类型的过程
            函数           含义
            dumps()        将Python数据类型转换为json格式
            loads()        将json格式字符串转换成Python数据类型
            dump()         与dumps()功能一致，输出到文件
            load()         与loads()功能一致，从文件读入

列表排序
    list.sort(func)
        func指定了排序的方法
        func可以通过lambda函数实现

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

