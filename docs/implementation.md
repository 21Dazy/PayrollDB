# 工资管理系统实现文档

## 1. 开发环境

- **操作系统**：Windows 10/11
- **编程语言**：Python 3.8+
- **IDE**：Visual Studio Code / PyCharm
- **数据库**：Microsoft SQL Server 2019
- **版本控制**：Git
- **UI框架**：Tkinter

## 2. 项目结构

```
PayDatabase/
│
├── database/               # 数据库相关文件
│   ├── design/             # 数据库设计文档
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
│
├── tests/                  # 测试代码
│
├── requirements.txt        # Python依赖
└── README.md               # 项目说明
```

## 3. 关键模块实现

### 3.1 数据库连接模块

数据库连接模块位于 `app/utils/db_utils.py`，主要实现以下功能：

1. 数据库连接管理
2. SQL查询执行
3. 事务处理
4. 存储过程调用

核心类 `DatabaseManager` 封装了数据库操作，提供高级接口供其他模块调用。

#### 关键方法

```python
# 连接数据库
def connect(self):
    # 实现...

# 断开连接
def disconnect(self):
    # 实现...

# 执行查询
def execute_query(self, query, params=None):
    # 实现...

# 执行非查询操作
def execute_non_query(self, query, params=None):
    # 实现...

# 执行存储过程
def execute_stored_procedure(self, proc_name, params=None):
    # 实现...
```

### 3.2 模型层实现

模型层位于 `app/models/` 目录，实现了各实体的业务逻辑：

1. `employee.py` - 员工模型
2. `department.py` - 部门模型
3. `position.py` - 职位模型
4. `salary.py` - 工资模型
5. `attendance.py` - 考勤模型

每个模型类都依赖于 `DatabaseManager` 进行数据操作，并提供特定的业务方法。

#### 示例：员工模型关键方法

```python
# 获取所有员工
def get_all_employees(self):
    # 实现...

# 添加员工
def add_employee(self, dept_id, pos_id, name, gender, birth_date, hire_date, 
                 phone, email, address, id_number):
    # 实现...

# 更新员工信息
def update_employee(self, emp_id, dept_id=None, pos_id=None, ...):
    # 实现...

# 删除员工
def delete_employee(self, emp_id):
    # 实现...
```

### 3.3 视图层实现

视图层位于 `app/views/` 目录，使用Tkinter实现用户界面：

1. `main_window.py` - 主窗口框架
2. `employee_view.py` - 员工管理界面
3. `department_view.py` - 部门管理界面
4. `position_view.py` - 职位管理界面
5. `salary_view.py` - 工资管理界面
6. `attendance_view.py` - 考勤管理界面
7. `report_view.py` - 报表界面

视图组件主要负责用户交互和数据展示，调用模型层方法完成业务操作。

### 3.4 应用程序入口

应用程序入口位于 `app/main.py`，负责初始化系统：

1. 配置日志系统
2. 创建数据库连接
3. 初始化模型实例
4. 创建主窗口
5. 启动应用程序循环

## 4. 关键业务流程实现

### 4.1 员工管理流程

1. 用户在界面输入或选择员工信息
2. 视图层收集数据并调用员工模型相应方法
3. 员工模型执行业务逻辑和数据验证
4. 调用数据库管理器执行SQL操作
5. 返回结果给视图层
6. 视图层更新界面显示结果

### 4.2 工资计算流程

1. 用户选择员工和计算日期
2. 视图层调用工资模型的计算方法
3. 工资模型获取职位基本工资和员工信息
4. 调用存储过程执行工资计算（包含社保和个税计算）
5. 工资结果写入数据库并返回给视图层
6. 视图层更新界面显示工资明细

### 4.3 报表生成流程

1. 用户选择报表类型和参数（日期范围、部门等）
2. 视图层调用相应模型的统计方法
3. 模型层执行复杂查询或调用存储过程
4. 返回统计数据给视图层
5. 视图层格式化数据并显示在界面上
6. 支持导出功能

## 5. 数据库实现

### 5.1 表结构实现

数据库表结构通过 `database/scripts/ddl/create_tables.sql` 脚本创建，包含：

1. 创建数据库
2. 创建表结构
3. 设置主键和外键约束
4. 添加默认值和检查约束
5. 创建计算列

### 5.2 存储过程实现

系统主要实现了以下存储过程：

1. `CalculateEmployeeSalary` - 计算员工工资
2. `GetEmployeesByDepartment` - 获取部门员工
3. `ChangeEmployeePosition` - 变更员工职位
4. `GenerateDepartmentSalaryReport` - 生成部门工资报表

### 5.3 视图实现

系统实现了多个数据库视图简化查询：

1. `EmployeeInfoView` - 员工信息视图
2. `EmployeeSalaryView` - 员工工资视图
3. `AttendanceSummaryView` - 考勤汇总视图
4. `DepartmentSalaryView` - 部门薪资统计视图

### 5.4 触发器实现

系统实现的主要触发器：

1. 工资记录更新触发器
2. 员工信息变更日志触发器
3. 防止表删除触发器

## 6. 安全实现

### 6.1 数据库权限

通过 `database/scripts/dcl/permissions.sql` 脚本配置数据库用户权限：

1. 创建数据库角色
2. 分配对象权限
3. 限制敏感操作

### 6.2 数据验证

1. 客户端输入验证
2. 服务端业务逻辑验证
3. 数据库约束验证

## 7. 部署实现

### 7.1 环境配置

1. 安装SQL Server数据库
2. 配置ODBC连接（详见`docs/odbc_configuration.md`）
3. 安装Python依赖包

### 7.2 应用配置

系统通过配置文件 `config.ini` 和 `config/database.json` 实现灵活配置：

1. 数据库连接参数
2. 系统参数设置
3. 日志配置 