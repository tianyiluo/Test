#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
China MWR data scraper
Author: Tianyi Luo
Date: 2019-01-18
'''


from selenium import webdriver
import time, os, datetime
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup


def data_scraper():
    driver = webdriver.Firefox()
    driver.get("http://xxfb.mwr.cn/sq_djdh.html")
    time.sleep(5)
    nowtime = f"{datetime.datetime.now():%Y-%m-%d-%H-%M}"
    fn = 'china_riv_%s.xlsx' % nowtime
    dfs = []
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    soup_header = soup.find_all("tr", {"class": "th-title"})[0]
    header = soup_header.find_all("td")
    header_txt = [h.text for h in header]
    soup_data = soup.find("div", {"id": "hdtable"})
    data = soup_data.find_all("td")
    data_txt = [d.text for d in data]
    # print(data_txt)
    data_txt = np.transpose(np.reshape(data_txt, (-1, 8)))
    columns = header_txt
    data = []
    for t in data_txt:
        temp = t.tolist()
        data.append(temp)
    data = np.transpose(data)
    df_temp = pd.DataFrame(data=data, columns=columns)
    dfs.append(df_temp)
    df = pd.concat(dfs)
    head_cols = df.columns.values[:4].tolist()
    df.drop_duplicates(subset=head_cols, keep='first', inplace=True)
    df.to_excel(os.path.join(data_folder, fn), index=None)
    driver.quit()

    driver = webdriver.Firefox()
    driver.get("http://xxfb.mwr.cn/sq_dxsk.html")
    time.sleep(5)
    nowtime = f"{datetime.datetime.now():%Y-%m-%d-%H-%M}"
    fn = 'china_res_%s.xlsx' % nowtime
    dfs = []
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    soup_header = soup.find_all("tr", {"class": "th-title"})[0]
    header = soup_header.find_all("td")
    header_txt = [h.text for h in header]
    print(header_txt)
    soup_data = soup.find("div", {"id": "hdtable"})
    data = soup_data.find_all("td")
    data_txt = [d.text for d in data]
    # print(data_txt)
    data_txt = np.transpose(np.reshape(data_txt, (-1, 8)))
    columns = header_txt
    data = []
    for t in data_txt:
        temp = t.tolist()
        data.append(temp)
    data = np.transpose(data)
    df_temp = pd.DataFrame(data=data, columns=columns)
    dfs.append(df_temp)
    df = pd.concat(dfs)
    head_cols = df.columns.values[:4].tolist()
    df.drop_duplicates(subset=head_cols, keep='first', inplace=True)
    df.to_excel(os.path.join(data_folder, fn), index=None)
    driver.quit()

    driver = webdriver.Firefox()
    driver.get("http://xxfb.mwr.cn/sq_zdysq.html")
    time.sleep(5)
    nowtime = f"{datetime.datetime.now():%Y-%m-%d-%H-%M}"
    fn = 'china_rain_%s.xlsx' % nowtime
    dfs = []
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    soup_header = soup.find_all("tr", {"class": "th-title"})[0]
    header = soup_header.find_all("td")
    header_txt = [h.text for h in header]
    print(header_txt)
    soup_data = soup.find("div", {"id": "hdtable"})
    data = soup_data.find_all("td")
    data_txt = [d.text for d in data]
    # print(data_txt)
    data_txt = np.transpose(np.reshape(data_txt, (-1, 7)))
    columns = header_txt
    data = []
    for t in data_txt:
        temp = t.tolist()
        data.append(temp)
    data = np.transpose(data)
    df_temp = pd.DataFrame(data=data, columns=columns)
    dfs.append(df_temp)
    df = pd.concat(dfs)
    head_cols = df.columns.values[:4].tolist()
    df.drop_duplicates(subset=head_cols, keep='first', inplace=True)
    df.to_excel(os.path.join(data_folder, fn), index=None)
    driver.quit()



if __name__ == '__main__':
    project_folder = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    data_folder = os.path.join(project_folder, 'data')
    data_scraper()
    print ("Done!")