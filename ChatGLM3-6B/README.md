# ChatGLM3-6B 实验

本目录用于记录 ChatGLM3-6B 模型的部署、问答测试代码、运行输出和截图。

## 模型信息

- 模型名称：ChatGLM3-6B
- ModelScope 地址：`https://www.modelscope.cn/ZhipuAI/chatglm3-6b.git`
- 建议本地路径：`/mnt/data/chatglm3-6b`

## 运行步骤

```bash
cd /mnt/workspace/HW3_LLM_Deployment
bash scripts/clone_models.sh chatglm
python ChatGLM3-6B/run_chatglm.py
```

运行完成后，关键回答自动整理到 `outputs/chatglm_results.md`。

## 文件说明

- `run_chatglm.py`：ChatGLM 问答测试脚本。
- `run_chatglm.ipynb`：ModelScope Notebook 执行模板。
- `outputs/`：保存运行结果。
