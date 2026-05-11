from __future__ import annotations

import json
import time
from pathlib import Path

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


MODEL_NAME = "Qwen-7B-Chat"
MODEL_PATH = Path("/mnt/data/Qwen-7B-Chat")
PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROMPTS_PATH = PROJECT_ROOT / "data" / "prompts.json"
OUTPUT_DIR = Path(__file__).resolve().parent / "outputs"
MAX_NEW_TOKENS = 300


def load_prompts() -> list[dict[str, str]]:
    data = json.loads(PROMPTS_PATH.read_text(encoding="utf-8"))
    return data["prompts"]


def ask(model, tokenizer, prompt: str) -> str:
    if hasattr(model, "chat"):
        try:
            response, _history = model.chat(tokenizer, prompt, history=None)
            return str(response).strip()
        except TypeError:
            response, _history = model.chat(tokenizer, prompt, history=[])
            return str(response).strip()

    inputs = tokenizer(prompt, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=MAX_NEW_TOKENS)
    answer_ids = outputs[0][inputs["input_ids"].shape[-1] :]
    return tokenizer.decode(answer_ids, skip_special_tokens=True).strip()


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    tokenizer = AutoTokenizer.from_pretrained(str(MODEL_PATH), trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        str(MODEL_PATH),
        trust_remote_code=True,
        torch_dtype="auto",
    ).eval()

    jsonl_path = OUTPUT_DIR / "qwen_results.jsonl"
    markdown_path = OUTPUT_DIR / "qwen_results.md"

    with jsonl_path.open("w", encoding="utf-8") as jsonl_file, markdown_path.open("w", encoding="utf-8") as md_file:
        md_file.write(f"# {MODEL_NAME} 问答测试结果\n\n")
        for item in load_prompts():
            prompt_id = item["id"]
            prompt = item["prompt"]
            print(f"\n===== {prompt_id} =====")
            print(prompt)

            started_at = time.perf_counter()
            answer = ask(model, tokenizer, prompt)
            latency = round(time.perf_counter() - started_at, 3)

            print("\n回答：")
            print(answer)
            print(f"耗时：{latency}s")

            record = {
                "model": MODEL_NAME,
                "prompt_id": prompt_id,
                "category": item.get("category", ""),
                "prompt": prompt,
                "answer": answer,
                "latency_seconds": latency,
            }
            jsonl_file.write(json.dumps(record, ensure_ascii=False) + "\n")

            md_file.write(f"## {prompt_id}\n\n")
            md_file.write(f"**问题：** {prompt}\n\n")
            md_file.write(f"**回答：**\n\n{answer}\n\n")
            md_file.write(f"**耗时：** {latency}s\n\n")

    print(f"\n结果已保存到：{jsonl_path}")
    print(f"报告摘录版已保存到：{markdown_path}")


if __name__ == "__main__":
    main()
