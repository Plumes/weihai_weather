#coding:utf-8
from lxml import html
import requests
import re
import time
import MySQLdb
page = requests.get('http://astro.wh.sdu.edu.cn/weather/try_c.htm')

tree = html.fromstring(page.content.decode('utf8','ignore'))
time_info = tree.xpath('//a[@name="Current"]/text()')
current_time = re.search(r'\d+-\d+-\d+ \d+:\d+', time_info[1]).group()
current_time = time.strptime(current_time, "%y-%m-%d %H:%M")
current_time = (int) (time.mktime(current_time)-8*3600)

sunshine_time = re.findall(r'\d+:\d+', time_info[2])

weather_data = tree.xpath('//td/b/text()')
if len(weather_data) == 12:
    weather = {}
    weather['temperature'] = (float)(re.search(r'\d+\.?\d*', weather_data[0]).group())
    weather['dewpoint'] = (float)(re.search(r'\d+\.?\d*', weather_data[1]).group())
    weather['humidity'] = (float)(re.search(r'\d+\.?\d*', weather_data[2]).group())
    weather['wind_chill'] = (float)(re.search(r'\d+\.?\d*', weather_data[3]).group())
    weather['wind_speed'] = (float)(re.search(r'\d+\.?\d*', weather_data[4]).group())
    weather['wind_direction'] = re.search(r'[A-Z]+', weather_data[4]).group()
    weather['thw_index'] = (float)(re.search(r'\d+\.?\d*', weather_data[5]).group())
    weather['barometer'] = (float)(re.search(r'\d+\.?\d*', weather_data[6]).group())
    weather['heat_index'] = (float)(re.search(r'\d+\.?\d*', weather_data[7]).group())
    weather['daily_rainfall'] = (float)(re.search(r'\d+\.?\d*', weather_data[8]).group())
    weather['monthly_rainfall'] = (float)(re.search(r'\d+\.?\d*', weather_data[9]).group())
    weather['current_rainfall'] = (float)(re.search(r'\d+\.?\d*', weather_data[10]).group())
    weather['sunshine'] = (float)(re.search(r'\d+\.?\d*', weather_data[11]).group())
    print weather
    
    # 打开数据库连接
    db = MySQLdb.connect("localhost","root","123456qwe","weather" )

    # SQL 插入语句
    sql = """INSERT INTO weihai(created,
             sunrise, sunset, temperature, dewpoint, humidity, wind_chill, wind_speed, wind_direction, thw_index, barometer, heat_index,
             daily_rainfall, monthly_rainfall, current_rainfall, sunshine)
             VALUES (%d, \'%s\', \'%s\', %f, %f, %f, %f, %f, \'%s\', %f, %f, %f, %f, %f, %f, %f)""" % (current_time, sunshine_time[0], sunshine_time[1],
                weather['temperature'], weather['dewpoint'], weather['humidity'], weather['wind_chill'], weather['wind_speed'],
                weather['wind_direction'], weather['thw_index'],weather['barometer'], weather['heat_index'], weather['daily_rainfall'],
                weather['monthly_rainfall'], weather['current_rainfall'], weather['sunshine'])
    cur = db.cursor()
    try:
       # 执行sql语句
       cur.execute(sql)
       # 提交到数据库执行
       db.commit()
    except:
       # Rollback in case there is any error
       db.rollback()

    # 关闭数据库连接
    db.close()