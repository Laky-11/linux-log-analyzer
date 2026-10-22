
# Linux 日志分析与自动化工具

## 1. 项目简介

本项目使用 Python 对简化的服务器访问日志进行解析和统计，
并计划通过 Shell 脚本实现日志分析流程的自动化。

项目用于练习 Python 文件处理、日志解析、Linux 命令行操作、
Shell 脚本和 Git 版本管理。

## 2. 当前功能

- 读取指定的日志文件
- 校验日志字段并解析记录
- 统计有效记录与异常格式记录
- 统计状态码分布
- 统计各 IP 的访问次数
- 支持从命令行指定日志文件路径

## 3. 技术栈

- Python 3
- Git / GitHub
- Linux / Bash（后续完善）

## 4. 项目结构

```text
linux-log-analyzer/
├── logs/
│   └── sample.log
├── src/
│   └── log_analyzer.py
├── scripts/
├── reports/
├── .gitignore
└── README.md
```

## 5. 运行环境

- Python 3
- Windows 或 Linux
- Git（用于版本管理）

## 6. 运行方法

在项目根目录执行：

```bash
python src/log_analyzer.py
```

指定日志文件：

```bash
python src/log_analyzer.py logs/sample.log
```

在 Linux 环境中，可根据实际安装情况使用 `python3` 命令。

## 7. 日志格式

每行包含四个字段：

```text
IP|端口|协议|状态码
```

示例：

```text
10.10.20.15|443|HTTPS|403
```

## 8. 后续计划

- 使用 Shell 脚本自动执行日志分析
- 自动生成并保存分析报告
- 完善异常处理与测试
- 补充 Linux 环境下的运行说明
