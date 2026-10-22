from collections import Counter
from pathlib import Path
import sys

def parse_logs(file_path):
    """读取日志文件，并解析有效记录。"""
    logs = []
    invalid_count = 0

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            parts = line.split("|")

            if len(parts) != 4:
                invalid_count += 1
                continue

            ip, port, protocol, status = parts #序列解包

            try:
                port = int(port)
                status = int(status)
            except ValueError:
                invalid_count += 1
                continue

            logs.append({
                "ip": ip,
                "port": port,
                "protocol": protocol,
                "status": status
            })

    return logs, invalid_count
def analyze_logs(logs):
    """统计日志总数、状态和 IP 访问次数。"""
    ip_counts = Counter(log["ip"] for log in logs)
    status_counts = Counter(log["status"] for log in logs)

    normal_count = status_counts[200]
    alert_count = len(logs) - normal_count

    return ip_counts, status_counts, normal_count, alert_count

def generate_report(file_path):
    """生成并输出日志分析报告。"""
    path = Path(file_path)

    if not path.is_file():
        print(f"错误：日志文件不存在：{path}")
        return 1

    try:
        logs, invalid_count = parse_logs(path)
    except (OSError, UnicodeError) as error:
        print(f"错误：读取日志文件失败：{error}")
        return 1

    ip_counts, status_counts, normal_count, alert_count = (
        analyze_logs(logs)
    )

    print("=" * 40)
    print("          日志分析报告")
    print("=" * 40)
    print(f"日志文件：{path}")
    print(f"有效记录数：{len(logs)}")
    print(f"异常格式记录数：{invalid_count}")
    print(f"正常记录数：{normal_count}")
    print(f"需关注记录数：{alert_count}")

    print("\n状态码统计：")
    for status, count in sorted(status_counts.items()):
        print(f"{status}: {count}")

    print("\nIP 访问统计：")
    for ip, count in ip_counts.most_common():
        print(f"{ip}: {count}")

    print("=" * 40)
    return 0

def main():
    if len(sys.argv) > 2:
        print("用法：python src/log_analyzer.py [日志文件路径]")
        return 1

    if len(sys.argv) == 2:
        file_path = sys.argv[1]
    else:
        file_path = "logs/sample.log"

    return generate_report(file_path)


if __name__ == "__main__":
    sys.exit(main())
