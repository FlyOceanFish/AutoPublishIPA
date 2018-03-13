#!/usr/bin/env python
#coding=gbk
import sys
import os
import time
import shutil
import sqlite3

# /Users/wangrifei/Desktop/dis
# /Users/wangrifei/Desktop/ios_dis
# print os.path.split(sys.argv[0])
# input = raw_input("请输入文件地址：")

database_name = 'apidb.db3'
date_dir = time.strftime("%Y%m%d", time.localtime())
root_path = 'C:\\Data\\ApiServiceInterface1'
#root_path = 'C:\\Users\\Administrator\\Desktop\\dis'
ios_dis_path = os.path.split(sys.argv[0])[0]
#ios_dis_path = "C:\\Users\\Administrator\\Desktop\\ios"
# 备份数据库
print('########开始备份数据库########\n')

back_database_path = os.path.join(root_path, 'backup/数据库/'+date_dir)
if not os.path.exists(back_database_path):
    os.mkdir(back_database_path)
shutil.copy(os.path.join(root_path, database_name), back_database_path)

# 备份ytostation.html
print('########  备份数据库完成！开始备份ytostation.html  ########\n')

index_path = root_path+'/Ytostation.html'
back_index_path = os.path.join(root_path, 'backup/YtoStation/'+date_dir)
if not os.path.exists(back_index_path):
    os.mkdir(back_index_path)
shutil.copy(index_path, back_index_path)
shutil.copy(os.path.join(ios_dis_path,'Ytostation.html'), index_path)
#备份安装包
print('########  复制ytostation.html完成！开始备份安装包  ########\n')

project_path = os.path.join(root_path, 'download/images/ios/YtoStation')
backup_ipa_path = os.path.join(project_path, date_dir)
if os.path.exists(backup_ipa_path):
    shutil.rmtree(backup_ipa_path)
shutil.copytree(project_path+'/latest', backup_ipa_path)

# 复制新的安装包
print('########  备份安装包完成！开始复制新的安装包  ########\n')

shutil.copy(os.path.join(ios_dis_path, 'YtoStation.ipa'), project_path+'/latest')
shutil.copy(ios_dis_path+'/manifest.plist', project_path+'/latest')
print("########  复制新的安装包完成！开始修改数据库中App的版本########\n")

# 修改数据库

version = raw_input("请输入此次发布的版本号:")


def update_version(version):
    print("########  开始修改数据库中的版本号！########\n")
    date = time.strftime("%Y/%m/%d %H:%M:00", time.localtime())
    conn = sqlite3.connect(os.path.join(root_path, database_name))
    conn.execute('update api set version=(?),update_time=(?) where api_name = "YtoStation"', (version, date))
    conn.commit()
    conn.close()
    print("########  修改数据库中的版本号成功！########\n")


update_version(version)

print('--------- APP全部发布成功！ -----------\n')
raw_input("输入回车退出")

