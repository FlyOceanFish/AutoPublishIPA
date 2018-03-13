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
# input = raw_input("�������ļ���ַ��")

database_name = 'apidb.db3'
date_dir = time.strftime("%Y%m%d", time.localtime())
root_path = 'C:\\Data\\ApiServiceInterface1'
#root_path = 'C:\\Users\\Administrator\\Desktop\\dis'
ios_dis_path = os.path.split(sys.argv[0])[0]
#ios_dis_path = "C:\\Users\\Administrator\\Desktop\\ios"
# �������ݿ�
print('########��ʼ�������ݿ�########\n')

back_database_path = os.path.join(root_path, 'backup/���ݿ�/'+date_dir)
if not os.path.exists(back_database_path):
    os.mkdir(back_database_path)
shutil.copy(os.path.join(root_path, database_name), back_database_path)

# ����ytostation.html
print('########  �������ݿ���ɣ���ʼ����ytostation.html  ########\n')

index_path = root_path+'/Ytostation.html'
back_index_path = os.path.join(root_path, 'backup/YtoStation/'+date_dir)
if not os.path.exists(back_index_path):
    os.mkdir(back_index_path)
shutil.copy(index_path, back_index_path)
shutil.copy(os.path.join(ios_dis_path,'Ytostation.html'), index_path)
#���ݰ�װ��
print('########  ����ytostation.html��ɣ���ʼ���ݰ�װ��  ########\n')

project_path = os.path.join(root_path, 'download/images/ios/YtoStation')
backup_ipa_path = os.path.join(project_path, date_dir)
if os.path.exists(backup_ipa_path):
    shutil.rmtree(backup_ipa_path)
shutil.copytree(project_path+'/latest', backup_ipa_path)

# �����µİ�װ��
print('########  ���ݰ�װ����ɣ���ʼ�����µİ�װ��  ########\n')

shutil.copy(os.path.join(ios_dis_path, 'YtoStation.ipa'), project_path+'/latest')
shutil.copy(ios_dis_path+'/manifest.plist', project_path+'/latest')
print("########  �����µİ�װ����ɣ���ʼ�޸����ݿ���App�İ汾########\n")

# �޸����ݿ�

version = raw_input("������˴η����İ汾��:")


def update_version(version):
    print("########  ��ʼ�޸����ݿ��еİ汾�ţ�########\n")
    date = time.strftime("%Y/%m/%d %H:%M:00", time.localtime())
    conn = sqlite3.connect(os.path.join(root_path, database_name))
    conn.execute('update api set version=(?),update_time=(?) where api_name = "YtoStation"', (version, date))
    conn.commit()
    conn.close()
    print("########  �޸����ݿ��еİ汾�ųɹ���########\n")


update_version(version)

print('--------- APPȫ�������ɹ��� -----------\n')
raw_input("����س��˳�")

