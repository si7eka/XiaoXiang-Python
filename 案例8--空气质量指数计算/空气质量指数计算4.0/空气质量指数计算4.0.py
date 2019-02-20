"""
作者：si7eklz
功能：空气质量指数AQI计算
日期：20190219
版本：4.0

案例描述：
    根据输入的文件判断是json还是csv，并进行相应的操作


文件操作补充
    csv文件读取
        imort csv
        csv.reader()将每行记录作为列表返回
    使用with语句操作文件对象
        with open('file_name') as somefile:
            for line in somefile:
                print(line)
    使用with语句，不管在处理文件过程中是否发生异常，都能保证with语句执行完毕关闭文件。不需要close()语句。
    
知识点
    os模块
        os模块提供了与系统，目录操作相关的功能，不受平台的限制(win linux)
            函数                含义
            os.remove()         删除文件
            os.makedirs()       创建多层目录
            os.rmdir()          删除单机目录
            os.rename()         重命名文件
            os.path.isfile()    判断是否为文件
            os.path.isdir()     判断是否为目录
            os.path.join()      连接目录, 如path1 连接 path2为 path1/path2
            os.path.splitext()  将文件分割成文件名与扩展名，如分割tmp.txt 为 tmp和.txt

"""

import json
import csv
import os


def process_json_file(filepath):
    """
        解析json文件
    """
    # f = open(filepath, mode='r', encoding='utf-8')
    # city_list = json.load(f)
    # return city_list

    with open(filepath, mode='r', encoding='utf-8') as f:
        city_list = json.load(f)
    print(city_list)

def main():
    """
        主函数
    """
    filepath = input('请输入文件名称: ')
    filename, file_ext = os.path.splitext(filepath)

    if file_ext == '.json':
        process_json_file
    elif file_ext == '.csv':
        pass
    else:
        print('不支持文件格式！')


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

