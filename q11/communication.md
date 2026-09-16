# Issue
标题：空白 --name 仍输出问候语并以 0 退出（应返回非零退出码）

- 环境：Windows（版本待确认）；greetlab-25020007055==0.1.0，wheel 安装。
- 复现命令：sdt-greet --name "   "
- 期望结果：name 仅含空白时报错，并以非零退出码退出（约定为 2）。
- 实际结果：输出 "Hello,  !"，退出码为 0。

# 提交信息
标题：Validate --name is non-blank and exit 2 on whitespace-only input
正文：--name 仅由空白组成时仍打印问候语并以 0 退出；现在解析参数后
      增加 strip() 检查，空白时写 stderr 并 SystemExit(2)，与缺参数
      时 argparse 的退出码 2 保持一致。

# 评审意见
[Blocking] 确认未传 --name 与传空白两条路径退出码一致，否则破坏依赖
          退出码的调用脚本。
[Suggestion] 错误文案抽为常量，避免测试断言与代码漂移。
[Nit]       函数内注释可删。
