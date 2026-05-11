# HW3_LLM_Deployment

《人工智能导论》第三次作业：大语言模型部署体验。

本仓库用于在 ModelScope 魔搭 Notebook CPU 环境中部署并测试 2-3 个开源大语言模型，记录每个模型的代码、Notebook、输出和截图，并在报告中完成横向对比分析。

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
├── 作业报告.md
├── requirements.txt
├── data/
│   └── prompts.json
├── scripts/
│   ├── clone_models.sh
│   └── setup_cpu_env.sh
├── screenshots/
│   └── .gitkeep
├── Qwen-7B-Chat/
│   ├── README.md
│   ├── run_qwen.py
│   ├── run_qwen.ipynb
│   ├── outputs/
│   └── screenshots/
├── ChatGLM3-6B/
│   ├── README.md
│   ├── run_chatglm.py
│   ├── run_chatglm.ipynb
│   ├── outputs/
│   └── screenshots/
└── Baichuan2-7B-Chat/
    ├── README.md
    ├── run_baichuan.py
    ├── run_baichuan.ipynb
    ├── outputs/
    └── screenshots/
```

说明：根目录下的三个模型文件夹是作业展示主体。真正的模型权重很大，不放入 GitHub 仓库，统一下载到 ModelScope Notebook 的 `/mnt/data`。

## ModelScope 快速流程

以下步骤对应老师 PDF 中的流程。ModelScope CPU 资源空闲 1 小时可能释放，模型较大，建议一次只下载和运行一个模型。

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

这里记得截图，报告中需要放 git clone 或部署完成截图。

### 3. 安装依赖

```bash
bash scripts/setup_cpu_env.sh
```

如果平台没有 conda，可按老师 PDF 先安装 Miniconda，再创建并激活环境：

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

- 根目录 `screenshots/`：放 git clone、依赖安装、模型下载等整体部署截图。
- `Qwen-7B-Chat/screenshots/`：放 Qwen 问答结果截图。
- `ChatGLM3-6B/screenshots/`：放 ChatGLM 问答结果截图。
- `Baichuan2-7B-Chat/screenshots/`：放 Baichuan 问答结果截图。
- 每个模型目录的 `outputs/`：脚本会生成 JSONL 原始结果和 Markdown 摘录，方便填报告。

## 推荐截图清单

- `screenshots/01_git_clone.png`：git clone 成功截图。
- `screenshots/02_environment.png`：依赖安装或模型下载截图。
- `Qwen-7B-Chat/screenshots/01_qwen_result.png`：Qwen 问答结果截图。
- `ChatGLM3-6B/screenshots/01_chatglm_result.png`：ChatGLM 问答结果截图。
- `Baichuan2-7B-Chat/screenshots/01_baichuan_result.png`：Baichuan 问答结果截图。

## 报告提交提醒

- 截止时间：5 月 31 日 23:59。
- 文档命名格式：`hw3_学号_姓名`。
- 评分重点：项目公开可访问链接 8 分，报告 12 分。
- 报告需包含部署截图、问答截图、横向对比分析。
