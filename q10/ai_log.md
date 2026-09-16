核心提示：--name 仅含空白时以 SystemExit(2) 结束，正常姓名输出不变
AI 改动：在 parse_args 后加 strip() 检查，空白时写 stderr 并 sys.exit(2)。
人工审查：diff 仅新增空白校验，未动其他逻辑，无多余改动。
验证：pytest 1 passed；空白输入退出码为 2，正常输入输出不变。
