# _*_ coding: utf-8 _*_
import sqlite3
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import traceback

def insert_tables():
    now92 = "0"
    conn = sqlite3.connect('OliPriceDB.db')
    cursor = conn.cursor()

    
    url = 'http://youjia.10260.com//'
    res = requests.get(url, headers={}).content.decode('GB2312')
    soup = BeautifulSoup(res, "lxml")
    allInfo = soup.select("#box > .chem_3 > .cpbox > .cpbaojia > table > tr")[1:32]
    for i in allInfo:
        area = i.contents[1].contents[0].string        
        v92 = i.contents[3].string
        v95 = i.contents[5].string
        v98 = i.contents[7].string
        v0 = i.contents[9].string
        time = datetime.now().strftime("%Y%m%d")
        print(area,  v92, v95, v98, v0,  )
        # sql = f"INSERT INTO OIL (`AREA`, `V0`, `V89`, `V92`, `V95`, `V98`,`UPDATE_TIME`) VALUES ('{area}', '{v0}', '{v89}', '{v92}', '{v95}', '{v98}','{time}')" #第一次要使用插入语句，后边获取根据区域名称更新数据，名称固定的
        #sql = f"UPDATE OIL SET V0 = '{v0}', V92 = '{v92}', V95 = '{v95}', V98 = '{v98}', UPDATE_TIME = '{time}' WHERE AREA ='{area}'"
        sql = f"INSERT INTO OIL VALUES (null, '{area}', '{v0}',  '{v92}', '{v95}', '{v98}', '{time}')"
        
        searchSql = "select * from OIL where UPDATE_TIME = '{}'".format(time)
        resault = cursor.execute(searchSql)

        if area == "辽宁" and len(resault.fetchall()) < 0:
            try:
                now92 = v92
                cursor.execute(sql)
                conn.commit()
                print('更新数据成功--------------->', area,  v92, v95, v98, v0, time)
            except:
                print('更新数据库失败！！请检查，可能网址接口更新')
                traceback.print_exc()
    cursor.close()
    conn.close()
    return now92
