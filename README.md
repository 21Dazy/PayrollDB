# 工资管理系统

本项目是一个基于SQL Server和Python+pyodbc+tkinter实现的工资管理系统。

## 项目结构

```
PayDatabase/
│
├── database/               # 数据库相关文件
│   ├── design/             # 数据库设计文档
│   │   └── ER_Diagram.md   # ER图设计
│   ├── scripts/            # SQL脚本
│   │   ├── ddl/            # 数据定义语言脚本
│   │   ├── dml/            # 数据操作语言脚本
│   │   ├── dcl/            # 数据控制语言脚本
│   │   ├── views/          # 视图创建脚本
│   │   ├── procedures/     # 存储过程脚本
│   │   └── triggers/       # 触发器脚本
│   └── test/               # 数据库测试脚本
│ 
├── app/                    # 应用程序源码
│   ├── models/             # 数据模型
│   ├── views/              # 视图
│   ├── controllers/        # 控制器
│   └── utils/              # 工具函数
│
├── docs/                   # 项目文档
│   ├── requirements.md     # 需求分析
│   ├── design.md           # 系统设计
│   ├── implementation.md   # 系统实现
│   ├── test_report.md      # 测试报告
│   └── collaboration.md    # 协作流程文档
│
├── tests/                  # 测试代码
│
├── requirements.txt        # Python依赖
├── .gitignore              # Git忽略文件
└── README.md               # 项目说明
```

## 功能特点

- 员工信息管理
- 工资核算
- 统计报表
- 完整的CRUD操作
- 事务处理

## 安装与使用

### 环境要求

- Python 3.8+
- SQL Server 2019+
- ODBC驱动程序

### 安装步骤

1. 克隆仓库：

```
git clone <repository_url>
cd PayDatabase
```

2. 安装依赖：

```
pip install -r requirements.txt
```

3. 配置ODBC连接（见文档）

4. 运行数据库脚本：

```
sqlcmd -S <server_name> -i database/scripts/ddl/create_tables.sql
```

5. 启动应用：

```
python app/main.py
```

## 协作开发

请参考 `docs/collaboration.md` 获取有关如何参与此项目开发的详细指南。

## 许可

此项目采用 MIT 许可证。详见 LICENSE 文件。 