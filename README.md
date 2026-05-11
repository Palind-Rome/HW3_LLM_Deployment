# HW3_LLM_Deployment

《人工智能导论》第三次作业：大语言模型部署体验。

本仓库用于在 ModelScope 魔搭 Notebook CPU 环境中部署并测试 3 个开源大语言模型，记录每个模型的代码、Notebook、输出和截图，并在报告中完成横向对比分析。

项目公开可访问链接：

https://github.com/Palind-Rome/HW3_LLM_Deployment

## 作业目标

- 在 ModelScope 平台完成环境配置、模型下载和推理测试。
- 分别测试 Qwen-7B-Chat、ChatGLM3-6B、Baichuan2-7B-Chat。
- 每个模型单独建目录，保留对应代码、Notebook、输出和截图。
- 在报告中手动整理不同模型的横向对比分析。

## 目录结构

```text
.
├── README.md
├── 实验报告.md
├── requirements.txt
├── data/
│   └── prompts.json
├── scripts/
│   ├── clone_models.sh
│   └── setup_cpu_env.sh
├── screenshots/
│   ├── image-*.png
│   └── .gitkeep
├── Qwen-7B-Chat/
│   ├── README.md
│   ├── run_qwen.py
│   ├── run_qwen.ipynb
│   ├── outputs/
│   │   ├── qwen_results.jsonl
│   │   └── qwen_results.md
│   └── screenshots/
├── ChatGLM3-6B/
│   ├── README.md
│   ├── run_chatglm.py
│   ├── run_chatglm.ipynb
│   ├── outputs/
│   │   ├── chatglm_results.jsonl
│   │   └── chatglm_results.md
│   └── screenshots/
└── Baichuan2-7B-Chat/
    ├── README.md
    ├── run_baichuan.py
    ├── run_baichuan.ipynb
    ├── outputs/
    │   ├── baichuan_results.jsonl
    │   └── baichuan_results.md
    └── screenshots/
```

说明：根目录下的三个模型文件夹是作业展示主体，分别保存对应模型的运行脚本、Notebook 模板和输出结果。实验截图目前统一放在根目录 `screenshots/` 下，并在 `实验报告.md` 中引用。真正的模型权重很大，不放入 GitHub 仓库，统一下载到 ModelScope Notebook 的 `/mnt/data`。

## ModelScope 快速流程

### 1. 平台准备

1. 注册并登录 [ModelScope](https://www.modelscope.cn/home)。
2. 绑定阿里云账号，领取免费 CPU 云计算资源。
3. 启动 CPU Notebook，进入 Jupyter 环境。
4. 点击 Terminal 图标打开终端。

### 2. 克隆本项目

```bash
cd /mnt/workspace
git clone https://github.com/Palind-Rome/HW3_LLM_Deployment.git
cd HW3_LLM_Deployment
```

### 3. 安装依赖

```bash
bash scripts/setup_cpu_env.sh
```

如果平台没有 conda，可先安装 Miniconda，再创建并激活环境：

```bash
cd /opt/conda/envs
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b -p /opt/conda
echo 'export PATH="/opt/conda/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
conda create -n qwen_env python=3.10 -y
source /opt/conda/etc/profile.d/conda.sh
conda activate qwen_env
```

### 4. 分模型运行实验

Qwen-7B-Chat：

```bash
bash scripts/clone_models.sh qwen
python Qwen-7B-Chat/run_qwen.py
```

ChatGLM3-6B：

```bash
bash scripts/clone_models.sh chatglm
python ChatGLM3-6B/run_chatglm.py
```

Baichuan2-7B-Chat：

```bash
bash scripts/clone_models.sh baichuan
python Baichuan2-7B-Chat/run_baichuan.py
```

也可以打开每个模型目录里的 `.ipynb` 文件，在 Jupyter 中按单元格执行。

## 输出与截图

- 根目录 `screenshots/`：保存 ModelScope 平台、环境配置、模型下载、git clone、运行过程和问答结果截图。
- `Qwen-7B-Chat/outputs/qwen_results.jsonl`：Qwen 原始问答结果。
- `Qwen-7B-Chat/outputs/qwen_results.md`：Qwen 报告摘录版结果。
- `ChatGLM3-6B/outputs/chatglm_results.jsonl`：ChatGLM 原始问答结果。
- `ChatGLM3-6B/outputs/chatglm_results.md`：ChatGLM 报告摘录版结果。
- `Baichuan2-7B-Chat/outputs/baichuan_results.jsonl`：Baichuan 原始问答结果。
- `Baichuan2-7B-Chat/outputs/baichuan_results.md`：Baichuan 报告摘录版结果。
