#!/bin/bash

# 接收第一个参数：CSV文件路径
csv_file="$1"

# 判断文件是否不存在
if [ ! -f "$csv_file" ]; then
    # 错误信息输出到stderr
    echo "错误：文件 $csv_file 不存在" >&2
    # 返回非零退出码
    exit 1
fi

# 1. 统计5xx状态码最多的前2个path
echo "=====5xx访问最多的前2个path====="
awk -F',' 'NR>1 && $4>=500 && $4<600 {print $3}' "$csv_file" \
| sort \
| uniq -c \
| sort -k1,1nr -k2,2 \
| head -n 2

# 2. 计算平均延迟，保留两位小数
echo -e "\n===== 平均 latency_ms(保留两位小数) ====="
awk -F',' 'NR>1 {sum += $5; cnt++} END{printf "%.2f\n", sum/cnt}' "$csv_file"
