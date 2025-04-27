# 工资管理系统设计文档

## 1. 系统架构

### 1.1 总体架构

工资管理系统采用三层架构设计：

```
+-------------------+
|    表示层(UI)     |  - 用户界面，使用tkinter实现
+-------------------+
|    业务逻辑层     |  - 业务处理，实现各种功能
+-------------------+
|    数据访问层     |  - 数据库操作，与SQL Server交互
+-------------------+
|     数据库层      |  - SQL Server数据库
+-------------------+
```

### 1.2 模块划分

系统主要分为以下几个模块：

1. **基础信息管理模块**：员工、部门、职位管理
2. **业务功能模块**：考勤管理、工资管理
3. **统计分析模块**：报表生成、数据分析
4. **系统配置模块**：系统参数设置、权限管理
5. **数据库访问模块**：数据连接、事务处理

## 2. 数据库设计

### 2.1 ER图

详见 `database/design/ER_Diagram.md`

### 2.2 表结构

系统包含以下主要数据表：

1. **Department (部门表)**
   - DeptID (PK)
   - DeptName
   - Manager
   - CreateDate
   - Status

2. **Position (职位表)**
   - PosID (PK)
   - PosName
   - BaseSalary
   - Allowance

3. **Employee (员工表)**
   - EmpID (PK)
   - DeptID (FK)
   - PosID (FK)
   - Name
   - Gender
   - BirthDate
   - HireDate
   - Phone
   - Email
   - Address
   - IDNumber

4. **Salary (工资表)**
   - SalaryID (PK)
   - EmpID (FK)
   - PayDate
   - BaseSalary
   - PerformancePay
   - OvertimePay
   - SocialSecurity
   - Tax
   - NetSalary (计算列)
   - Status

5. **Attendance (考勤表)**
   - AttendID (PK)
   - EmpID (FK)
   - Date
   - CheckInTime
   - CheckOutTime
   - Status
   - LeaveType
   - Remarks

详细的表结构和关系定义见 `database/scripts/ddl/create_tables.sql`

## 3. 系统模块设计

### 3.1 用户界面设计

#### 3.1.1 界面框架
- 主窗口：左侧菜单栏，右侧内容区，底部状态栏
- 弹出对话框：用于数据录入、编辑和确认操作

#### 3.1.2 主要界面
- 员工管理界面
- 部门管理界面
- 职位管理界面
- 考勤管理界面
- 工资管理界面
- 统计报表界面

### 3.2 业务模块设计

#### 3.2.1 员工管理模块
- 提供员工信息的CRUD操作
- 支持按多种条件查询员工
- 实现部门和职位变更功能

#### 3.2.2 考勤管理模块
- 记录员工每日考勤情况
- 支持请假和加班记录
- 生成月度考勤统计

#### 3.2.3 工资管理模块
- 基于职位基本工资计算
- 结合绩效和加班情况
- 自动计算社保和个税扣除
- 支持批量计算和发放

#### 3.2.4 统计分析模块
- 部门工资统计报表
- 员工考勤统计报表
- 工资发放趋势分析

### 3.3 数据访问模块设计

- 使用`DatabaseManager`类封装数据库操作
- 支持参数化查询防止SQL注入
- 实现事务处理确保数据一致性
- 提供存储过程调用接口

## 4. 接口设计

### 4.1 内部接口

#### 数据库接口
- `execute_query`：执行查询操作
- `execute_non_query`：执行非查询操作
- `execute_stored_procedure`：执行存储过程

#### 模型接口
各模型类（如Employee, Department等）提供以下通用接口：
- `get_all_xxx`：获取所有记录
- `get_xxx_by_id`：根据ID获取记录
- `add_xxx`：添加记录
- `update_xxx`：更新记录
- `delete_xxx`：删除记录

### 4.2 外部接口

系统暂不提供外部API接口。如需集成外部系统，可通过以下方式：
- 数据库级别集成
- 文件导入/导出功能

## 5. 安全设计

### 5.1 身份认证

- 用户登录验证
- 基于角色的权限控制

### 5.2 数据安全

- 敏感信息加密存储
- 数据库访问权限控制
- 操作日志记录审计

## 6. 部署设计

### 6.1 系统要求

- 操作系统：Windows 10+
- 数据库：SQL Server 2019+
- Python环境：Python 3.8+
- 网络：局域网环境

### 6.2 部署步骤

1. 安装SQL Server数据库
2. 运行数据库创建脚本
3. 安装Python及依赖包
4. 配置系统参数
5. 启动应用程序 