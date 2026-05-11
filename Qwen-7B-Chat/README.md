# Qwen-7B-Chat 实验

本目录用于记录 Qwen-7B-Chat 模型的部署、问答测试代码、运行输出和截图。

## 模型信息

- 模型名称：Qwen-7B-Chat
- ModelScope 地址：`https://www.modelscope.cn/qwen/Qwen-7B-Chat.git`
- 建议本地路径：`/mnt/data/Qwen-7B-Chat`

## 运行步骤

```bash
cd /mnt/workspace/HW3_LLM_Deployment
bash scripts/clone_models.sh qwen
python Qwen-7B-Chat/run_qwen.py
```

运行完成后，关键回答自动整理到 `outputs/qwen_results.md`。

## 文件说明

- `run_qwen.py`：Qwen 问答测试脚本。
- `run_qwen.ipynb`：ModelScope Notebook 执行模板。
- `outputs/`：保存运行结果。
