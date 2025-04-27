# SQL Server ODBC连接配置指南

## 1. 概述

本文档提供配置SQL Server ODBC连接的详细步骤，以便工资管理系统能够连接到数据库。工资管理系统使用pyodbc库通过ODBC驱动程序与SQL Server数据库通信。

## 2. 前提条件

在配置ODBC连接前，请确保您已满足以下条件：

- SQL Server 2019或更高版本已安装并正常运行
- 已创建PayrollDB数据库（通过运行`database/scripts/ddl/create_tables.sql`脚本）
- 系统上已安装适当的SQL Server ODBC驱动程序
- 拥有创建ODBC数据源的管理员权限

## 3. 安装SQL Server ODBC驱动程序

### 3.1 检查已安装的ODBC驱动程序

1. 打开命令提示符或PowerShell
2. 运行以下命令检查已安装的ODBC驱动：
   ```
   python -c "import pyodbc; print(pyodbc.drivers())"
   ```
3. 查看输出列表中是否包含SQL Server驱动程序

### 3.2 安装SQL Server ODBC驱动程序

如果您的系统中没有安装SQL Server ODBC驱动程序，请按照以下步骤安装：

#### Windows系统

1. 访问Microsoft下载中心，下载"Microsoft ODBC Driver for SQL Server"
   - 推荐下载链接：https://go.microsoft.com/fwlink/?linkid=2224818 (ODBC Driver 18)
   - 备选下载链接：https://go.microsoft.com/fwlink/?linkid=2202930 (ODBC Driver 17)

2. 运行下载的安装程序，按照向导完成安装

#### Linux系统（Ubuntu）

```bash
curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
curl https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/prod.list | sudo tee /etc/apt/sources.list.d/mssql-release.list
sudo apt-get update
sudo ACCEPT_EULA=Y apt-get install -y msodbcsql18
```

#### macOS系统

```bash
brew tap microsoft/mssql-release https://github.com/Microsoft/homebrew-mssql-release
brew update
brew install msodbcsql18
```

## 4. 配置ODBC数据源

### 4.1 创建系统DSN（数据源名称）

#### Windows系统

1. 打开"ODBC数据源管理器"：
   - 在Windows搜索框中输入"ODBC"
   - 选择"ODBC数据源管理器(64位)"或"设置ODBC数据源(64位)"

2. 在"ODBC数据源管理器"中，选择"系统DSN"选项卡

3. 点击"添加"按钮，会弹出"创建新数据源"对话框

4. 从驱动程序列表中选择"ODBC Driver 17 for SQL Server"（或您安装的版本）

5. 点击"完成"按钮，将弹出配置窗口

6. 进行以下设置：
   - 名称：输入`PayrollDSN`（此名称将在配置文件中使用）
   - 描述：输入`Payroll Database Connection`（可选）
   - 服务器：输入SQL Server实例名称，例如`localhost\SQLEXPRESS`
   - 点击"下一步"

7. 选择身份验证方法：
   - SQL Server身份验证：选择此选项并输入用户名和密码
     - 用户名：`payroll_user`（或您创建的用户名）
     - 密码：输入相应的密码
   - Windows身份验证：如果SQL Server配置为使用Windows认证，可选择此选项
   - 点击"下一步"

8. 设置默认数据库：
   - 选中"更改默认数据库为"选项
   - 从下拉列表中选择`PayrollDB`
   - 点击"下一步"

9. 在最后的配置页面上保持默认设置，点击"完成"

10. 在弹出的摘要页面上，可以点击"测试数据源"以验证连接是否成功

### 4.2 创建用户DSN（可选）

上述步骤创建了系统DSN，对所有用户都可用。如果需要，您也可以创建只对当前用户可见的用户DSN：

1. 在"ODBC数据源管理器"中，选择"用户DSN"选项卡
2. 按照与系统DSN相同的步骤操作

## 5. 配置应用程序使用ODBC连接

### 5.1 使用配置文件

工资管理系统通过`config.ini`文件配置数据库连接。编辑项目根目录下的`config.ini`文件：

```ini
[DATABASE]
# 使用DSN连接方式（推荐）
DSN = PayrollDSN

# 如果不使用DSN，可以使用以下直接连接方式
# SERVER = localhost\SQLEXPRESS
# DATABASE = PayrollDB

# SQL Server身份验证（如果使用DSN但不包含凭据信息）
# USERNAME = payroll_user
# PASSWORD = 您的密码
```

### 5.2 使用环境变量（可选）

也可以通过环境变量配置数据库连接，这种方式更安全，尤其是在生产环境中：

#### Windows系统
```
setx PAYROLL_DB_DSN "PayrollDSN"
setx PAYROLL_DB_USER "payroll_user"
setx PAYROLL_DB_PASSWORD "您的密码"
```

#### Linux/macOS系统
```bash
export PAYROLL_DB_DSN="PayrollDSN"
export PAYROLL_DB_USER="payroll_user"
export PAYROLL_DB_PASSWORD="您的密码"
```

## 6. 测试ODBC连接

在配置完成后，可以使用项目中提供的测试脚本来验证连接：

1. 打开命令提示符或终端
2. 导航到项目目录
3. 运行测试脚本：
   ```
   python database/test/test_odbc_connection.py
   ```

或者使用这个简单的Python代码片段测试连接：

```python
import pyodbc

try:
    # 使用DSN方式连接
    conn = pyodbc.connect('DSN=PayrollDSN')
    
    # 或者使用直接连接方式
    # conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost\SQLEXPRESS;DATABASE=PayrollDB;UID=payroll_user;PWD=您的密码')
    
    cursor = conn.cursor()
    cursor.execute("SELECT @@VERSION")
    row = cursor.fetchone()
    print(f"连接成功！SQL Server版本: {row[0]}")
    
    cursor.close()
    conn.close()
except Exception as e:
    print(f"连接失败: {str(e)}")
```

## 7. 常见问题与解决方案

### 7.1 连接失败："数据源名称未找到且未指定默认驱动程序"

- **原因**：DSN名称输入错误或DSN未正确创建
- **解决方案**：检查DSN名称拼写，确保在正确的ODBC管理器（32位/64位）中创建了DSN

### 7.2 连接失败："SQL Server不存在或拒绝访问"

- **原因**：服务器名称错误或SQL Server服务未运行
- **解决方案**：
  - 确认SQL Server服务正在运行
  - 验证服务器名称和实例名称是否正确
  - 检查防火墙设置是否允许SQL Server连接

### 7.3 连接失败："登录失败"

- **原因**：用户名或密码错误，或用户没有访问权限
- **解决方案**：
  - 验证用户名和密码是否正确
  - 确认用户对PayrollDB有适当的访问权限
  - 尝试使用SQL Server管理工具手动测试登录

### 7.4 连接失败："找不到指定模块"

- **原因**：ODBC驱动程序未正确安装或位数不匹配（32位/64位）
- **解决方案**：
  - 重新安装ODBC驱动程序
  - 确保安装的驱动程序版本与应用程序位数匹配
  - 使用`pyodbc.drivers()`检查驱动程序是否正确安装

## 8. 安全最佳实践

1. **避免在代码中硬编码凭据**：
   - 使用配置文件或环境变量存储连接信息
   - 对生产环境的配置文件进行适当的访问权限控制

2. **使用最小权限原则**：
   - 为应用程序创建专用数据库用户
   - 只授予应用程序所需的最小权限
   - 避免使用SA账户或数据库所有者账户

3. **加密连接**：
   - 在ODBC连接字符串中使用`Encrypt=YES`参数
   - 在生产环境中使用SSL证书

4. **审核和日志**：
   - 启用SQL Server审核功能以跟踪关键操作
   - 定期检查日志以识别异常活动

## 9. 参考资源

- [Microsoft ODBC Driver for SQL Server文档](https://docs.microsoft.com/en-us/sql/connect/odbc/microsoft-odbc-driver-for-sql-server)
- [pyodbc文档](https://github.com/mkleehammer/pyodbc/wiki)
- [SQL Server连接字符串参考](https://www.connectionstrings.com/sql-server/)
- [ODBC数据源管理器使用指南](https://docs.microsoft.com/en-us/sql/odbc/admin/odbc-data-source-administrator) 