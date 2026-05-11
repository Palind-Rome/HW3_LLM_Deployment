# hw3_学号_姓名

# 大语言模型部署体验报告

## 一、基本信息

| 项目 | 内容 |
| --- | --- |
| 课程 | 人工智能导论 |
| 作业 | 第三次作业：大语言模型部署体验 |
| 学号 | 待填写 |
| 姓名 | 待填写 |
| 平台 | ModelScope 魔搭 CPU Notebook |
| 项目公开链接 | [Palind-Rome/HW3_LLM_Deployment](https://github.com/Palind-Rome/HW3_LLM_Deployment) |

## 二、实验目的

本次实验在 ModelScope 魔搭平台上部署开源大语言模型，并针对中文语义歧义、指代消解、嵌套逻辑推理、多义词理解和课程助理应用场景进行问答测试。通过统一的问题集记录不同模型的回答，比较它们在理解准确性、推理能力、表达清晰度、稳定性和资源开销方面的差异。

## 三、详细实验步骤记录

### 3.1 打开 notebook 实例

首先，注册并登录 ModelScope，绑定阿里云账号后，得到了云计算资源。

![image-20260511082326686](screenshots/image-20260511082326686.png)

点击启动 notebook，开始进行实验。

![image-20260511082421549](screenshots/image-20260511082421549.png)

如图，在实例中打开终端：

![image-20260511082914785](screenshots/image-20260511082914785.png)

### 3.2 配置环境

先配置 conda 环境，配置命令如下：

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b -p /opt/conda
echo 'export PATH="/opt/conda/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
conda --version
export CONDA_PLUGINS_AUTO_ACCEPT_TOS=yes
conda create -n qwen_env python=3.10 -y
source /opt/conda/etc/profile.d/conda.sh
conda activate qwen_env
```

配置截图如下：

![image-20260511090611398](screenshots/image-20260511090611398.png)

![image-20260511090653362](screenshots/image-20260511090653362.png)

![image-20260511090708004](screenshots/image-20260511090708004.png)

![image-20260511093314724](screenshots/image-20260511093314724.png)

然后为 conda 环境配置基础依赖，命令如下：

```bash
pip install \
torch==2.3.0+cpu \
torchvision==0.18.0+cpu \
--index-url https://download.pytorch.org/whl/cpu
pip install -U pip setuptools wheel
# 安装基础依赖（兼容 transformers 4.33.3 和 neuralchat）
pip install \
"intel-extension-for-transformers==1.4.2" \
"neural-compressor==2.5" \
"transformers==4.33.3" \
"modelscope==1.9.5" \
"pydantic==1.10.13" \
"sentencepiece" \
"tiktoken" \
"einops" \
"transformers_stream_generator" \
"uvicorn" \
"fastapi" \
"yacs" \
"setuptools_scm"
# 安装 fschat（需要启用 PEP517 构建）
pip install fschat --use-pep517
# 安装 tqdm、huggingface-hub 等增强体验
pip install tqdm huggingface-hub
```

配置截图如下：

![image-20260511101411897](screenshots/image-20260511101411897.png)

![image-20260511101400276](screenshots/image-20260511101400276.png)

![image-20260511101525108](screenshots/image-20260511101525108.png)

![image-20260511101629693](screenshots/image-20260511101629693.png)

![image-20260511101636290](screenshots/image-20260511101636290.png)

### 3.3  大模型实践

首先要下载大模型到本地。先切换到数据目录，

```bash
cd /mnt/data
```

然后下载对应大模型 ：

```bash
git clone https://www.modelscope.cn/qwen/Qwen-7B-Chat.git
git clone https://www.modelscope.cn/ZhipuAI/chatglm3-6b.git
git clone https://www.modelscope.cn/baichuan-inc/Baichuan2-7B-Chat.git
```

截图如下：

![image-20260511103829627](screenshots/image-20260511103829627.png)

现在来构建实例。首先切换工作目录：

```bash
cd /mnt/workspace
```

然后编写推理脚本 `run_qwen_cpu.py`

```python
from transformers import TextStreamer, AutoTokenizer, AutoModelForCausalLM

model_name = "/mnt/data/Qwen-7B-Chat" # 本地路径
prompt = "请说出以下两句话区别在哪里？ 1、冬天：能穿多少穿多少 2、夏天：能穿多少穿多少"

tokenizer = AutoTokenizer.from_pretrained(
	model_name,
	trust_remote_code=True
)

model = AutoModelForCausalLM.from_pretrained(
	model_name,
	trust_remote_code=True,
	torch_dtype="auto" # 自动选择 float32/float16（根据模型配置）
).eval()

inputs = tokenizer(prompt, return_tensors="pt").input_ids

streamer = TextStreamer(tokenizer)
outputs = model.generate(inputs, streamer=streamer, max_new_tokens=300)
```

为了让实验更加方便、更加自动化，我首先在本地个人电脑上完成三个模型的推理脚本代码编写，然后将脚本上传到 GitHub 的作业项目仓库上，最后在 ModelScope 的 Notebook 中克隆我刚刚写好的仓库，这样就能直接运行脚本。具体流程如下图：

首先，我将待测试的问答 prompt 写入 `prompt.json`：

![image-20260511104352196](screenshots/image-20260511104352196.png)

然后，我完成了各个模型的运行 python 脚本。脚本会自动使用  `prompt.json` 作为输入，以 Qwen 为例：

![image-20260511104718799](screenshots/image-20260511104718799.png)

![image-20260511104803602](screenshots/image-20260511104803602.png)



## 四、测试模型与项目目录

| 序号 | 模型 | 来源/版本 | 本地模型路径 | 仓库实验目录 | 测试状态 |
| --- | --- | --- | --- | --- | --- |
| 1 | Qwen-7B-Chat | ModelScope: `qwen/Qwen-7B-Chat` | `/mnt/data/Qwen-7B-Chat` | `Qwen-7B-Chat/` | 待填写 |
| 2 | ChatGLM3-6B | ModelScope: `ZhipuAI/chatglm3-6b` | `/mnt/data/chatglm3-6b` | `ChatGLM3-6B/` | 待填写 |
| 3 | Baichuan2-7B-Chat | ModelScope: `baichuan-inc/Baichuan2-7B-Chat` | `/mnt/data/Baichuan2-7B-Chat` | `Baichuan2-7B-Chat/` | 待填写 |

## 五、问答测试设计

本实验使用统一问题集，以保证不同模型之间可横向比较。问题保存在仓库的 `data/prompts.json` 中。

| 编号 | 能力维度 | 测试问题 |
| --- | --- | --- |
| Q1 | 语义歧义 | 请说出以下两句话区别在哪里？1、冬天：能穿多少穿多少 2、夏天：能穿多少穿多少 |
| Q2 | 语义歧义 | 请说出以下两句话区别在哪里？单身狗产生的原因有两个，一是谁都看不上，二是谁都看不上 |
| Q3 | 逻辑推理 | 他知道我知道你知道他不知道吗？这句话里，到底谁不知道？请逐层分析。 |
| Q4 | 指代消解 | 明明明明明白白白喜欢他，可她就是不说。这句话里，明明和白白谁喜欢谁？请解释你的判断。 |
| Q5 | 多义词理解 | “意思”对话中每个“意思”分别是什么意思？ |
| Q6 | 应用场景 | 假设你是大学课程助教，请说明该作业应怎样安排完成顺序。 |

## 六、问答测试结果截图

### 6.1 Qwen-7B-Chat

运行命令：

```bash
bash scripts/clone_models.sh qwen
python Qwen-7B-Chat/run_qwen.py
```

结果截图：

![Qwen 问答结果截图](Qwen-7B-Chat/screenshots/01_qwen_result.png)

运行输出文件：

- `Qwen-7B-Chat/outputs/qwen_results.jsonl`
- `Qwen-7B-Chat/outputs/qwen_results.md`

代表性回答摘录：

| 问题 | 回答要点 | 是否正确 | 备注 |
| --- | --- | --- | --- |
| Q1 | 待填写 | 待填写 | 待填写 |
| Q2 | 待填写 | 待填写 | 待填写 |
| Q3 | 待填写 | 待填写 | 待填写 |
| Q4 | 待填写 | 待填写 | 待填写 |
| Q5 | 待填写 | 待填写 | 待填写 |
| Q6 | 待填写 | 待填写 | 待填写 |

### 6.2 ChatGLM3-6B

运行命令：

```bash
bash scripts/clone_models.sh chatglm
python ChatGLM3-6B/run_chatglm.py
```

结果截图：

![ChatGLM 问答结果截图](ChatGLM3-6B/screenshots/01_chatglm_result.png)

运行输出文件：

- `ChatGLM3-6B/outputs/chatglm_results.jsonl`
- `ChatGLM3-6B/outputs/chatglm_results.md`

代表性回答摘录：

| 问题 | 回答要点 | 是否正确 | 备注 |
| --- | --- | --- | --- |
| Q1 | 待填写 | 待填写 | 待填写 |
| Q2 | 待填写 | 待填写 | 待填写 |
| Q3 | 待填写 | 待填写 | 待填写 |
| Q4 | 待填写 | 待填写 | 待填写 |
| Q5 | 待填写 | 待填写 | 待填写 |
| Q6 | 待填写 | 待填写 | 待填写 |

### 6.3 Baichuan2-7B-Chat

运行命令：

```bash
bash scripts/clone_models.sh baichuan
python Baichuan2-7B-Chat/run_baichuan.py
```

结果截图：

![Baichuan 问答结果截图](Baichuan2-7B-Chat/screenshots/01_baichuan_result.png)

运行输出文件：

- `Baichuan2-7B-Chat/outputs/baichuan_results.jsonl`
- `Baichuan2-7B-Chat/outputs/baichuan_results.md`

代表性回答摘录：

| 问题 | 回答要点 | 是否正确 | 备注 |
| --- | --- | --- | --- |
| Q1 | 待填写 | 待填写 | 待填写 |
| Q2 | 待填写 | 待填写 | 待填写 |
| Q3 | 待填写 | 待填写 | 待填写 |
| Q4 | 待填写 | 待填写 | 待填写 |
| Q5 | 待填写 | 待填写 | 待填写 |
| Q6 | 待填写 | 待填写 | 待填写 |

## 七、横向对比分析

本节根据三个模型目录中的输出和截图手动整理，不需要额外代码生成。

### 7.1 总体对比表

| 维度 | Qwen-7B-Chat | ChatGLM3-6B | Baichuan2-7B-Chat | 分析结论 |
| --- | --- | --- | --- | --- |
| 中文语义歧义理解 | 待填写 | 待填写 | 待填写 | 待填写 |
| 嵌套逻辑推理 | 待填写 | 待填写 | 待填写 | 待填写 |
| 指代消解 | 待填写 | 待填写 | 待填写 | 待填写 |
| 多义词解释 | 待填写 | 待填写 | 待填写 | 待填写 |
| 应用场景回答 | 待填写 | 待填写 | 待填写 | 待填写 |
| 表达清晰度 | 待填写 | 待填写 | 待填写 | 待填写 |
| 推理速度/资源占用 | 待填写 | 待填写 | 待填写 | 待填写 |

### 7.2 具体分析

#### 语义歧义类问题

待填写：比较模型是否能解释“能穿多少穿多少”在冬天和夏天中的语义差异，以及“谁都看不上”中主客体方向的不同。

#### 逻辑与指代类问题

待填写：比较模型是否能逐层拆解“他知道我知道你知道他不知道吗”，以及是否能正确判断“明明”和“白白”的指代关系。

#### 多义词理解问题

待填写：比较模型是否能把不同语境下的“意思”解释为含义、礼物/表示、情面、有趣、不好意思等不同含义。

#### 应用场景问题

待填写：比较模型作为课程助教时的回答是否条理清晰、步骤可执行、是否覆盖公开链接、截图和横向对比等评分点。

### 7.3 小结

待填写：综合来看，哪个模型更适合中文歧义理解，哪个模型在逻辑推理中更稳定，哪个模型回答更简洁或更啰嗦。注意结合实际截图和回答内容进行说明。

## 八、实验问题与解决方法

| 问题 | 原因分析 | 解决方法 |
| --- | --- | --- |
| CPU 推理速度较慢 | 7B 模型参数量较大，CPU 算力有限 | 减少输出长度，一次只运行一个模型 |
| 存储空间不足 | 多个 7B 模型同时下载占用空间大 | 按模型逐个下载、测试、清理 |
| 依赖冲突 | 不同模型依赖版本不同 | 按 README 固定版本安装，必要时重建环境 |
| Notebook 资源释放 | 平台空闲 1 小时会清空环境 | 及时保存截图、结果文件和仓库代码 |

## 九、结论

待填写：概括本次部署体验、模型测试结果、横向对比结论，以及对开源大模型部署成本和能力边界的认识。

## 十、附录

### 10.1 关键命令

```bash
cd /mnt/workspace
git clone https://github.com/Palind-Rome/HW3_LLM_Deployment.git
cd HW3_LLM_Deployment
bash scripts/setup_cpu_env.sh

bash scripts/clone_models.sh qwen
python Qwen-7B-Chat/run_qwen.py

bash scripts/clone_models.sh chatglm
python ChatGLM3-6B/run_chatglm.py

bash scripts/clone_models.sh baichuan
python Baichuan2-7B-Chat/run_baichuan.py
```

### 10.2 提交检查

- [ ] 报告文件命名为 `hw3_学号_姓名`。
- [ ] 报告中包含项目公开可访问链接。
- [ ] 报告中包含 git clone 或部署完成截图。
- [ ] 报告中包含问答测试结果截图。
- [ ] 报告中包含至少 2 个模型的横向对比分析。
- [ ] Canvas 提交前检查图片是否能正常显示。
