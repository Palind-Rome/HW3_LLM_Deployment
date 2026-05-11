# Baichuan2-7B-Chat 实验

本目录用于记录 Baichuan2-7B-Chat 模型的部署、问答测试代码、运行输出和截图。

## 模型信息

- 模型名称：Baichuan2-7B-Chat
- ModelScope 地址：`https://www.modelscope.cn/baichuan-inc/Baichuan2-7B-Chat.git`
- 建议本地路径：`/mnt/data/Baichuan2-7B-Chat`

## 运行步骤

```bash
cd /mnt/workspace/HW3_LLM_Deployment
bash scripts/clone_models.sh baichuan
python Baichuan2-7B-Chat/run_baichuan.py
```

运行完成后，关键回答会自动整理到 `outputs/`。

## 文件说明

- `run_baichuan.py`：Baichuan 问答测试脚本。
- `run_baichuan.ipynb`：ModelScope Notebook 执行模板。
- `outputs/`：保存运行结果。
