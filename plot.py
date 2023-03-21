#!/usr/bin/env python
# coding: utf-8


def plot_figs(file_path, plot_path, year, month):
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    from openpyxl import Workbook

    # import argparse

    # parser = argparse.ArgumentParser()
    # parser.add_argument("--file")
    # parser.add_argument("--plot")
    # args = parser.parse_args()
    # print(args.file)

    # file_path = args.file
    # plot_path = args.plot
    # print(file_path)

    # 繪製中文字
    plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']

    # 指定檔案路徑
    #file_path = 'C:/Users/data/'
    #plot_path = 'C:/Users/data/plot/'
    #year = '111'
    #month = '09'   


    # --- 廠區自來水用量 (bar & line chart) ------------------------------

    file_name = 'water.xlsx'
    sheet_name = 'water'
    plot_name = '廠區自來水用量.jpeg'

    old_water = pd.read_excel(file_path + file_name,
                              sheet_name,
                              skiprows=1,
                              usecols=[0, 2, 4, 5])
    old_water.columns = ['月份', '廠區自來水用量', '日平均(自來水公司)(CMD)', '日平均(代操作公司)(CMD)']

    # data select
    if month[0] == '0':
        timeSelect = year + '/' + month[1]
    else:
        timeSelect = year + '/' + month
    
    water = old_water[old_water['月份'].astype('object').between('110/1', timeSelect)]
    #water = water.fillna(0)
    water.drop(water.tail(1).index, inplace=True)  # drop last n rows
    # print(water)

    fig, ax = plt.subplots()  # Create the figure and axes object
    ax1 = ax.twinx()
    # Plot the first x and y axes:
    # ax.plot(kind='bar', water['廠區自來水用量'], figsize=(10,5), ax=ax)
    water.plot.bar(x='月份', y='廠區自來水用量', ax=ax, figsize=(10, 6))

    ax.set_ylabel('每月用水量(度)', fontsize=14)
    ax.tick_params(axis='y', labelcolor='black')
    ax.legend(loc='upper left', fontsize=12)
    ax.set_xlabel('月份', fontsize=14)
    ax.set_title('廠區自來水用量', fontsize=20)
    ax1.set_ylabel('CMD')
    ax.grid(axis='y', linestyle='solid', color='gray')


    y = ['日平均(自來水公司)(CMD)', '日平均(代操作公司)(CMD)']

    rows = range(2)
    color = ['limegreen', 'orange']
    linestyle = ["-", "--"]
    for x in rows:
        water.plot(x='月份', y=y[x], ax=ax1,
                   style=linestyle[x], color=color[x], linewidth=2.5, secondary_y=True, ylabel='CMD')

    ax1.tick_params(axis='y', labelcolor='black')
    ax.legend(loc='upper left', fontsize=12)
    plt.tight_layout()

    plt.savefig(plot_path + plot_name, bbox_inches='tight', dpi=300)


    # --- 重要設備妥善率比較圖 (bar chart)

    file_name = '主要設備妥善率.xlsx'
    sheet_name = '妥善率'
    plot_name = '重要設備妥善率比較圖.jpeg'

    old_machine = pd.read_excel(file_path + file_name,
                                   sheet_name,
                                   usecols=[1,2,3])
    #data select
    machine = old_machine[0:19]
    machine[machine.columns[1:3]] = machine[machine.columns[1:3]]*100

    machine.plot.bar(x='設備', rot=1,
                     figsize=(10, 5),  # Figsize to make the plot larger
                     fontsize=14)  # Making my ticks a bit bigger

    plt.grid(axis='y', linestyle='solid', color='gray')
    plt.xlabel('', fontsize=14)  # Adding a label on y axis
    plt.ylabel('百分比(%)', fontsize=14)
    plt.legend(loc='lower right', fontsize=12)
    plt.title('重要設備妥善率比較圖', fontsize=20)  # Adding a title to the top
    plt.xticks(rotation=45)

    plt.savefig(plot_path + plot_name, bbox_inches='tight', dpi=300)
