import torch
from torch import nn

torch.manual_seed(20260907)

# 造数据：y = 3*x - 1
x = torch.linspace(-1, 1, 101).reshape(-1, 1)
y = 3 * x - 1

model = nn.Linear(1, 1)
loss_fn = nn.MSELoss()
opt = torch.optim.SGD(model.parameters(), lr=0.1)

# ===== 训练循环 =====
for _ in range(200):
    pred = model(x)              # 前向：用当前 w/b 算预测
    loss = loss_fn(pred, y)     # 算损失

    opt.zero_grad()             # TODO1 清空上一轮梯度
    loss.backward()             # TODO2 反向传播，算梯度
    opt.step()                  # TODO3 按梯度更新 w/b

# ===== 评估 =====
model.eval()                    # 进入评估模式
with torch.no_grad():           # 关闭梯度记录
    final_loss = loss_fn(model(x), y)
    print(f"final loss = {final_loss.item():.6f}")
    print(f"weight     = {model.weight.item():.4f}")
    print(f"bias       = {model.bias.item():.4f}")
