"""
作者：si7eklz
功能：空气质量指数AQI计算
日期：20190219
版本：5.0

案例描述：
    利用爬虫实时获取城市空气质量

概念
    网络爬虫
        自动抓取互联网信息；利用互联网数据进行分析，开发产品。
        步骤：
            1. 通过网络连接获取网页内容
            2. 对获得的网页内容进行处理

知识点
    requests模块
        requests模块是一个简洁且简单的处理HTTP请求的工具
        支持非常丰富的连接访问功能，包含URL获取，HTTP会话，Cookie记录等
        requests网页请求
            函数         
            get()----对应http的get方式
            post()----对应http的post方式,用于传递用户数据

        requests对象属性
            status_code----http请求的放回状态,200表示连接成功, 400表示失败
            text----http相应内容的字符串形式, 即URL对应的页面内容
        参考:http://cn.python-requests.org/zh_CN/latest/



"""
import requests


def get_html_text(url):
    """
        获取url文本
    """
    r = requests.get(url, timeout=30)
    # print(r.status_code)
    return r.text
 
    


def main():
    """
        主函数
    """
    city_pinyin = input('请输入城市全拼：')
    url = 'http://pm25.in/' + city_pinyin
    url_text = get_html_text(url)

    aqi_div = '''<div class="span12 data">
        <div class="span1">
          <div class="value">
            '''
    index = url_text.find(aqi_div)
    begin_index = index + len(aqi_div)
    end_index = begin_index + 3
    aqi_div = url_text[begin_index: end_index]
    print('空气质量为：{}'.format(aqi_div))

if __name__ == '__main__':
    main()

