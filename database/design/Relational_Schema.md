# 工资管理系统关系模式设计

## 初始关系模式（根据E-R图）

1. **部门(Department)**
   - 部门ID (DeptID) - PK
   - 部门名称 (DeptName)
   - 部门主管 (Manager)
   - 创建日期 (CreateDate)
   - 部门状态 (Status)

2. **职位(Position)**
   - 职位ID (PosID) - PK
   - 职位名称 (PosName)
   - 基本工资 (BaseSalary)
   - 岗位津贴 (Allowance)

3. **员工(Employee)**
   - 员工ID (EmpID) - PK
   - 部门ID (DeptID) - FK
   - 职位ID (PosID) - FK
   - 姓名 (Name)
   - 性别 (Gender)
   - 出生日期 (BirthDate)
   - 入职日期 (HireDate)
   - 联系电话 (Phone)
   - 邮箱地址 (Email)
   - 家庭住址 (Address)
   - 身份证号 (IDNumber)

4. **工资(Salary)**
   - 工资ID (SalaryID) - PK
   - 员工ID (EmpID) - FK
   - 发放日期 (PayDate)
   - 基本工资 (BaseSalary)
   - 绩效工资 (PerformancePay)
   - 加班工资 (OvertimePay)
   - 社保扣款 (SocialSecurity)
   - 个税扣款 (Tax)
   - 实发工资 (NetSalary)
   - 工资状态 (Status)

5. **考勤记录(Attendance)**
   - 考勤ID (AttendID) - PK
   - 员工ID (EmpID) - FK
   - 日期 (Date)
   - 签到时间 (CheckInTime)
   - 签退时间 (CheckOutTime)
   - 考勤状态 (Status)
   - 请假类型 (LeaveType)
   - 备注 (Remarks)

## 规范化过程

### 第一范式（1NF）

确保每个表中的所有属性都是原子的（不可再分）。

分析：
- 所有表的属性都是原子的，不可再分。
- 每个表都有主键。
- 基本符合1NF要求。

### 第二范式（2NF）

确保表中的非主键属性完全依赖于主键，消除部分依赖。

分析：
1. **部门表(Department)**：
   - 主键是DeptID，所有其他属性都完全依赖于DeptID。
   - 符合2NF要求。

2. **职位表(Position)**：
   - 主键是PosID，所有其他属性都完全依赖于PosID。
   - 符合2NF要求。

3. **员工表(Employee)**：
   - 主键是EmpID，所有其他属性都完全依赖于EmpID。
   - 符合2NF要求。

4. **工资表(Salary)**：
   - 主键是SalaryID，所有其他属性都完全依赖于SalaryID。
   - 符合2NF要求。

5. **考勤记录表(Attendance)**：
   - 主键是AttendID，所有其他属性都完全依赖于AttendID。
   - 符合2NF要求。

所有表都满足2NF的要求，不存在部分依赖。

### 第三范式（3NF）

确保表中的非主键属性不依赖于其他非主键属性，消除传递依赖。

分析：
1. **部门表(Department)**：
   - 不存在非主键属性依赖于其他非主键属性的情况。
   - 符合3NF要求。

2. **职位表(Position)**：
   - 不存在非主键属性依赖于其他非主键属性的情况。
   - 符合3NF要求。

3. **员工表(Employee)**：
   - 存在潜在的传递依赖：员工的基本工资和岗位津贴可能通过职位ID间接依赖。
   - 解决方案：移除员工表中的基本工资和岗位津贴字段，这些信息应从职位表中获取。

4. **工资表(Salary)**：
   - 不存在非主键属性依赖于其他非主键属性的情况。
   - 符合3NF要求。

5. **考勤记录表(Attendance)**：
   - 不存在非主键属性依赖于其他非主键属性的情况。
   - 符合3NF要求。

## 优化后的关系模式（3NF）

1. **部门(Department)**
   - 部门ID (DeptID) - PK
   - 部门名称 (DeptName)
   - 部门主管 (Manager)
   - 创建日期 (CreateDate)
   - 部门状态 (Status)

2. **职位(Position)**
   - 职位ID (PosID) - PK
   - 职位名称 (PosName)
   - 基本工资 (BaseSalary)
   - 岗位津贴 (Allowance)

3. **员工(Employee)**
   - 员工ID (EmpID) - PK
   - 部门ID (DeptID) - FK, 引用 部门(DeptID)
   - 职位ID (PosID) - FK, 引用 职位(PosID)
   - 姓名 (Name)
   - 性别 (Gender)
   - 出生日期 (BirthDate)
   - 入职日期 (HireDate)
   - 联系电话 (Phone)
   - 邮箱地址 (Email)
   - 家庭住址 (Address)
   - 身份证号 (IDNumber)

4. **工资(Salary)**
   - 工资ID (SalaryID) - PK
   - 员工ID (EmpID) - FK, 引用 员工(EmpID)
   - 发放日期 (PayDate)
   - 基本工资 (BaseSalary)
   - 绩效工资 (PerformancePay)
   - 加班工资 (OvertimePay)
   - 社保扣款 (SocialSecurity)
   - 个税扣款 (Tax)
   - 实发工资 (NetSalary)
   - 工资状态 (Status)

5. **考勤记录(Attendance)**
   - 考勤ID (AttendID) - PK
   - 员工ID (EmpID) - FK, 引用 员工(EmpID)
   - 日期 (Date)
   - 签到时间 (CheckInTime)
   - 签退时间 (CheckOutTime)
   - 考勤状态 (Status)
   - 请假类型 (LeaveType)
   - 备注 (Remarks)

## 关系模式特点

1. **主键约束**：
   - 每个表都有主键：DeptID, PosID, EmpID, SalaryID, AttendID

2. **外键约束**：
   - 员工表中的DeptID引用部门表的DeptID
   - 员工表中的PosID引用职位表的PosID
   - 工资表中的EmpID引用员工表的EmpID
   - 考勤记录表中的EmpID引用员工表的EmpID

3. **字段类型**：
   - 整数类型：所有ID字段，如DeptID, PosID, EmpID等
   - 字符串类型：DeptName, PosName, Name, Gender, Phone, Email, Address, IDNumber等
   - 日期类型：CreateDate, BirthDate, HireDate, PayDate, Date等
   - 时间类型：CheckInTime, CheckOutTime
   - 货币类型：BaseSalary, Allowance, PerformancePay, OvertimePay, SocialSecurity, Tax, NetSalary等
   - 枚举类型：Status, LeaveType等

4. **级联操作**：
   - 当删除部门表中的记录时，级联更新或删除员工表中的相关记录
   - 当删除职位表中的记录时，级联更新或删除员工表中的相关记录
   - 当删除员工表中的记录时，级联删除工资表和考勤记录表中的相关记录 