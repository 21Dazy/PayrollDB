#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyodbc
import sys
import traceback

"""
ODBC连接测试脚本
此脚本用于测试与SQL Server数据库的ODBC连接。
"""

def test_connection(dsn_name=None, server=None, database=None, username=None, password=None):
    """
    测试ODBC连接
    参数:
        dsn_name: ODBC数据源名称（如果使用DSN连接）
        server: 服务器地址（如果使用直接连接）
        database: 数据库名称（如果使用直接连接）
        username: 用户名（如果使用SQL Server身份验证）
        password: 密码（如果使用SQL Server身份验证）
    返回:
        连接成功返回True，否则返回False
    """
    try:
        # 构建连接字符串
        if dsn_name:
            conn_str = f"DSN={dsn_name}"
            if username and password:
                conn_str += f";UID={username};PWD={password}"
        else:
            conn_str = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database}"
            if username and password:
                conn_str += f";UID={username};PWD={password}"
            else:
                conn_str += ";Trusted_Connection=yes"
        
        print(f"正在连接数据库，连接字符串: {conn_str}")
        
        # 尝试连接
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        
        # 执行简单查询
        cursor.execute("SELECT @@VERSION")
        row = cursor.fetchone()
        if row:
            print("连接成功!")
            print(f"SQL Server版本: {row[0]}")
            
            # 测试查询数据库表
            try:
                cursor.execute("SELECT COUNT(*) FROM sys.tables")
                row = cursor.fetchone()
                print(f"数据库中的表数量: {row[0]}")
            except:
                print("无法查询表信息，可能是权限问题。")
        
        # 关闭连接
        cursor.close()
        conn.close()
        return True
    
    except Exception as e:
        print("连接失败!")
        print(f"错误信息: {str(e)}")
        print("详细错误信息:")
        traceback.print_exc()
        return False


def list_available_drivers():
    """
    列出系统上所有可用的ODBC驱动程序
    """
    print("系统上可用的ODBC驱动程序:")
    drivers = pyodbc.drivers()
    for index, driver in enumerate(drivers, 1):
        print(f"{index}. {driver}")
    return drivers


def main():
    """
    主函数，用于交互式测试ODBC连接
    """
    print("=" * 50)
    print("SQL Server ODBC连接测试工具")
    print("=" * 50)
    
    # 列出可用驱动
    drivers = list_available_drivers()
    if not drivers:
        print("未检测到任何ODBC驱动程序！请安装SQL Server ODBC驱动。")
        return
    
    print("\n请选择连接方式:")
    print("1. 使用DSN（数据源名称）")
    print("2. 使用直接连接")
    choice = input("请输入选择 (1/2): ")
    
    if choice == "1":
        dsn_name = input("请输入DSN名称: ")
        use_sql_auth = input("是否使用SQL Server身份验证 (y/n): ").lower() == 'y'
        
        if use_sql_auth:
            username = input("请输入用户名: ")
            password = input("请输入密码: ")
            test_connection(dsn_name=dsn_name, username=username, password=password)
        else:
            test_connection(dsn_name=dsn_name)
    
    elif choice == "2":
        server = input("请输入服务器地址 (例如 localhost\\SQLEXPRESS): ")
        database = input("请输入数据库名称 (例如 PayrollDB): ")
        use_sql_auth = input("是否使用SQL Server身份验证 (y/n): ").lower() == 'y'
        
        if use_sql_auth:
            username = input("请输入用户名: ")
            password = input("请输入密码: ")
            test_connection(server=server, database=database, username=username, password=password)
        else:
            test_connection(server=server, database=database)
    
    else:
        print("无效的选择!")


if __name__ == "__main__":
    main() 