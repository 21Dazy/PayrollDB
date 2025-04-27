# Git 多人协作指南 - 使用 Fork 模式进行分支协作开发

## 基础概念解释

在开始之前，让我们先了解一些基本概念：

- **Git**: 版本控制系统，用于跟踪文件变化
- **仓库 (Repository)**: 存储项目文件和历史记录的地方
- **主仓库**: 团队共享的官方代码库
- **Fork**: 在你自己账号下创建主仓库的个人副本
- **克隆 (Clone)**: 将仓库下载到本地电脑
- **分支 (Branch)**: 独立的开发线，可以同时进行多个功能开发
- **提交 (Commit)**: 保存你的更改
- **推送 (Push)**: 将本地更改上传到远程仓库
- **拉取请求 (Pull Request)**: 请求将你的更改合并到主仓库

## 一、安装和配置 Git

### 1. 安装 Git

**Windows 用户**:
1. 访问 [Git 官网](https://git-scm.com/download/win)
2. 下载安装程序并运行
3. 使用默认选项完成安装

**Mac 用户**:
1. 打开终端
2. 输入 `brew install git` (如果已安装 Homebrew)
   或者从 [Git 官网](https://git-scm.com/download/mac) 下载安装程序

### 2. 配置 Git 身份

安装完成后，打开命令提示符或终端，设置你的身份：

```
git config --global user.name "你的名字"
git config --global user.email "你的邮箱@example.com"
```

## 二、Fork 工作流基本步骤

### 1. 创建 Fork (一次性操作)

1. 访问项目的主仓库页面 (例如: GitHub 上的 `https://github.com/组织名/工资管理系统`)
2. 点击右上角的 "Fork" 按钮
3. 等待几秒钟，仓库将被复制到你的账户中

![Fork 按钮示意图](https://i.imgur.com/6tKlcTk.png)

### 2. 克隆你的 Fork 到本地 (一次性操作)

1. 在你的 Fork 仓库页面，点击绿色的 "Code" 按钮
2. 复制显示的 URL (例如: `https://github.com/你的用户名/工资管理系统.git`)
3. 打开命令提示符或终端
4. 导航到你想保存项目的文件夹：`cd 目标文件夹路径`
5. 执行克隆命令：

```
git clone https://github.com/你的用户名/工资管理系统.git
```

6. 进入项目文件夹：

```
cd 工资管理系统
```

### 3. 连接到原始主仓库 (一次性操作)

为了能够获取主仓库的最新更新，需要添加一个指向原始仓库的远程链接：

```
git remote add upstream https://github.com/组织名/工资管理系统.git
```

验证远程链接设置是否正确：

```
git remote -v
```

你应该看到两个远程链接：
- `origin`: 指向你的 Fork
- `upstream`: 指向原始主仓库

## 三、日常开发工作流

### 1. 更新你的本地仓库 (每次开始新工作前)

在开始新工作之前，确保你的本地仓库是最新的：

```
# 切换到主分支
git checkout main

# 从原始仓库获取最新更改
git fetch upstream

# 合并原始仓库的更改到你的本地主分支
git merge upstream/main

# 将更新后的本地主分支推送到你的 Fork
git push origin main
```

### 2. 创建功能分支 (每个新功能/任务)

为每个新功能或任务创建一个独立的分支：

```
# 创建并切换到新分支
git checkout -b feature/员工管理功能
```

命名建议：
- `feature/xxx`: 新功能
- `bugfix/xxx`: 修复 bug
- `docs/xxx`: 文档更新

### 3. 在分支上工作并提交更改

1. 编辑、添加或删除文件
2. 查看文件状态：

```
git status
```

3. 添加更改到暂存区：

```
# 添加特定文件
git add 文件名.py

# 添加所有更改
git add .
```

4. 提交更改：

```
git commit -m "添加员工信息编辑功能"
```

提交信息建议：
- 简明扼要地描述你做了什么
- 使用现在时态 ("添加功能" 而不是 "添加了功能")
- 可以使用中文，保持团队一致性

### 4. 推送分支到你的 Fork

```
git push origin feature/员工管理功能
```

如果是第一次推送此分支，Git 可能会提示你设置上游分支，按照提示执行即可。

### 5. 创建拉取请求 (Pull Request)

1. 访问你的 Fork 仓库页面
2. 你应该看到一个提示，表示你最近推送了一个分支，点击 "Compare & pull request"
3. 如果没有提示，点击 "Pull requests" 标签，然后点击 "New pull request"
4. 选择：
   - base repository: 原始主仓库
   - base: main (或目标分支)
   - head repository: 你的 Fork
   - compare: 你的功能分支
5. 填写 PR 标题和描述：
   - 标题：简要描述此 PR 的目的
   - 描述：详细说明你做了什么更改、解决了什么问题
6. 点击 "Create pull request"

![Pull Request 示意图](https://i.imgur.com/DrdSrCs.png)

### 6. 代码审查和讨论

1. 团队成员会审查你的代码并提出建议
2. 可能需要根据反馈进行修改：
   ```
   # 在同一分支上继续修改
   git add .
   git commit -m "根据代码审查修改表单验证"
   git push origin feature/员工管理功能
   ```
3. 修改会自动更新到已有的 PR 中

### 7. PR 被合并后

当你的 PR 被接受并合并到主仓库后：

1. 切换回你的主分支：
   ```
   git checkout main
   ```

2. 更新你的本地仓库和 Fork：
   ```
   git fetch upstream
   git merge upstream/main
   git push origin main
   ```

3. 删除已完成的功能分支（可选）：
   ```
   # 删除本地分支
   git branch -d feature/员工管理功能
   
   # 删除远程分支
   git push origin --delete feature/员工管理功能
   ```

## 四、常见问题与解决方案

### 1. 合并冲突

当你的更改与主仓库中的更改冲突时：

1. 先更新你的主分支：
   ```
   git checkout main
   git fetch upstream
   git merge upstream/main
   git push origin main
   ```

2. 将主分支的更改合并到你的功能分支：
   ```
   git checkout feature/员工管理功能
   git merge main
   ```

3. 解决冲突：
   - 打开有冲突的文件
   - 找到标记了 `<<<<<<< HEAD`, `=======`, `>>>>>>> main` 的部分
   - 编辑文件解决冲突，保留正确的代码
   - 删除冲突标记

4. 提交解决冲突后的版本：
   ```
   git add .
   git commit -m "解决合并冲突"
   git push origin feature/员工管理功能
   ```

### 2. 撤销本地更改

如果你想放弃本地未提交的更改：
```
git checkout -- 文件名.py  # 撤销单个文件
git checkout -- .          # 撤销所有文件
```

### 3. 撤销最近的提交

如果你想撤销最近的提交但保留更改：
```
git reset --soft HEAD~1
```

### 4. 查看提交历史
```
git log                  # 详细历史
git log --oneline        # 简洁历史
git log --graph --oneline # 图形化历史
```

## 五、Git 图形界面工具

如果你不喜欢命令行操作，可以考虑使用图形界面工具：

1. **GitHub Desktop**: [下载链接](https://desktop.github.com/)
   - 简单易用，与 GitHub 集成良好
   
2. **GitKraken**: [下载链接](https://www.gitkraken.com/)
   - 功能强大，有免费版和专业版

3. **SourceTree**: [下载链接](https://www.sourcetreeapp.com/)
   - 功能全面，免费使用

## 六、Git 常用命令速查表

| 命令 | 描述 |
|------|------|
| `git clone URL` | 克隆仓库到本地 |
| `git status` | 查看文件状态 |
| `git add 文件名` | 添加文件到暂存区 |
| `git commit -m "消息"` | 提交更改 |
| `git push origin 分支名` | 推送到远程仓库 |
| `git pull origin 分支名` | 从远程仓库拉取更新 |
| `git checkout 分支名` | 切换分支 |
| `git checkout -b 分支名` | 创建并切换到新分支 |
| `git branch` | 列出本地分支 |
| `git branch -a` | 列出所有分支（包括远程） |
| `git fetch upstream` | 从原始仓库获取更新 |
| `git merge upstream/main` | 合并原始仓库的更改 |
| `git remote -v` | 查看远程仓库链接 |

## 七、小组协作最佳实践

1. **频繁更新和提交**：
   - 每天开始工作前更新你的仓库
   - 小步提交，每个提交专注于一个变更

2. **遵循分支命名约定**：
   - `feature/xxx`: 新功能
   - `bugfix/xxx`: 修复问题
   - `docs/xxx`: 文档更新

3. **写好提交信息**：
   - 清晰描述你做了什么
   - 必要时解释为什么这样做

4. **拉取请求说明**：
   - 提供足够的上下文
   - 描述你的解决方案
   - 提及相关问题编号

5. **审查代码**：
   - 积极参与代码审查
   - 提供有建设性的反馈
   - 及时响应审查意见

6. **避免直接提交到主分支**：
   - 始终使用功能分支
   - 通过 PR 合并到主分支

7. **解决合并冲突**：
   - 尽早解决合并冲突
   - 如有必要，与相关团队成员讨论解决方案

## 学习资源

- [Git 官方文档](https://git-scm.com/doc)
- [GitHub 指南](https://guides.github.com/)
- [廖雪峰的 Git 教程](https://www.liaoxuefeng.com/wiki/896043488029600)（中文）
- [GitHub Learning Lab](https://lab.github.com/)（互动学习）

## 团队 Git 工作流程图

```
主仓库 (upstream)          个人 Fork (origin)             本地仓库
     |                          |                          |
     |                          |                          |
     |      fork操作            |                          |
     | -----------------------> |                          |
     |                          |                          |
     |                          |       克隆操作           |
     |                          | -----------------------> |
     |                          |                          |
     |                          |                          |  创建功能分支
     |                          |                          | -------------> feature/xxx
     |                          |                          |                   |
     |                          |                          |                   |
     |                          |                          |                   |  提交更改
     |                          |                          |                   | --------> 
     |                          |                          |                   |
     |                          |     推送功能分支         |                   |
     |                          | <----------------------- |                   |
     |                          |                          |                   |
     |      提交PR              |                          |                   |
     | <----------------------- |                          |                   |
     |         |                |                          |                   |
     |  代码审查                |                          |                   |
     |         |                |                          |                   |
     |  合并到主分支            |                          |                   |
     |         |                |                          |                   |
     |         v                |                          |                   |
     |    main更新              |                          |                   |
     |                          |                          |                   |
     |     获取更新             |      更新main分支        |                   |
     | -----------------------> | -----------------------> |                   |
     |                          |                          | <----------------- 
     |                          |                          |  合并完成后切回main
     |                          |                          |
```

按照这个文档指南，即使是 Git 新手也能快速掌握使用 Fork 模式进行多人协作开发的基本流程。如有任何问题，欢迎随时向团队中有经验的成员请教。 