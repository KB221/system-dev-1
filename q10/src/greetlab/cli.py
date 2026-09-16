import argparse
import sys

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--name", required=True)
    a = p.parse_args()
    # 空白字符（空格/tab/空串）视为非法输入，以退出码 2 结束
    if not a.name or not a.name.strip():
        print("error: --name must not be blank", file=sys.stderr)
        sys.exit(2)
    print(f"Hello, {a.name}!")
