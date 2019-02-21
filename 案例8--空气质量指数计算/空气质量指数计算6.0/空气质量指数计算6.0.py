"""
作者：si7eklz
功能：空气质量指数AQI计算
日期：20190221
版本：6.0

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

    高效的解析和处理html， beautifulsoup4

    网页解析
        结构化解析
        DOM(Document Object Model), 树形结构

                         DOCUMENT
                            │
                          <HTML>
                       ROOT ELEMENT
               ┌────────────┴────────────┐
             <head>                    <body> 
             ELEMENT                   ELEMENT
               │                         │
             <title>                    <div> 
             ELEMENT                   ELEMENT              
               │                    ┌────┴──────┐
           "MY TITLE"              <h1>        <p>
            ELEMENT              ELEMENT     ELEMENT
                                                |
                                               <a>
                                             ELEMENT

    BeautifulSoup解析网页
        BeautifulSoup
            用于解析HTML或xml
            pip install beautifulsoup4
            improt bs4
            步骤
                1. 创建BeautifulSoup对象
                2. 查询节点
                   find， 查到第一个满足的节点
                   find_all，找到所有满足调节的节点
            
            创建对象
                创建BeautifulSoup对象
                bs = BeautifulSoup(
                    url,
                    html_parser, 指定解析器
                    enoding      指定编码格式（确保和网页编码一致）
                )
            
            查找节点
            <a href='a.html' class='a_link'>next page</a>
            可按节点类型， 属性或内容访问
            按类型查找节点
                bs.fing_all('a')
            按属性查找节点
                bs.find_all('a',href='a.html')
                bs.find_all('a',href='a.html',string='next page')
                bs.find_all('a',class_='a_link')
                    注意：是class_ 因为python有关键字class避免混淆
            或者bs.find_all('a',{'class':'a_link'})
"""
import requests
from bs4 import BeautifulSoup


def get_city_aqi(city_pinyin):
    """
        获取城市AQI
    """
    url = 'http://pm25.in/' + city_pinyin
    r = requests.get(url, timeout=30)
    soup = BeautifulSoup(r.text, 'lxml')
    div_list = soup.find_all('div', {'class': 'span1'})

    city_aqi = []
    for i in range(8):
        div_content = div_list[i]
        caption = div_content.find('div', {'class': 'caption'}).text.strip()
        value = div_content.find('div', {'class': 'value'}).text.strip()

        city_aqi.append((caption, value))
    return city_aqi
    


def main():
    """
        主函数
    """
    city_pinyin = input('请输入城市全拼：')
    city_aqi = get_city_aqi(city_pinyin)
    print(city_aqi)

if __name__ == '__main__':
    main()

