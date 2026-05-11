#!/usr/bin/env bash
set -euo pipefail

MODEL_DIR="${MODEL_DIR:-/mnt/data}"
MODEL_NAME="${1:-qwen}"

mkdir -p "$MODEL_DIR"
cd "$MODEL_DIR"

clone_if_missing() {
  local url="$1"
  local dir="$2"

  if [ -d "$dir" ]; then
    echo "Skip $dir because it already exists."
    return
  fi

  git clone "$url" "$dir"
}

case "$MODEL_NAME" in
  qwen)
    clone_if_missing "https://www.modelscope.cn/qwen/Qwen-7B-Chat.git" "Qwen-7B-Chat"
    ;;
  chatglm)
    clone_if_missing "https://www.modelscope.cn/ZhipuAI/chatglm3-6b.git" "chatglm3-6b"
    ;;
  baichuan)
    clone_if_missing "https://www.modelscope.cn/baichuan-inc/Baichuan2-7B-Chat.git" "Baichuan2-7B-Chat"
    ;;
  all)
    echo "Warning: 7B models are large. Make sure /mnt/data has enough space."
    clone_if_missing "https://www.modelscope.cn/qwen/Qwen-7B-Chat.git" "Qwen-7B-Chat"
    clone_if_missing "https://www.modelscope.cn/ZhipuAI/chatglm3-6b.git" "chatglm3-6b"
    clone_if_missing "https://www.modelscope.cn/baichuan-inc/Baichuan2-7B-Chat.git" "Baichuan2-7B-Chat"
    ;;
  *)
    echo "Usage: bash scripts/clone_models.sh [qwen|chatglm|baichuan|all]"
    exit 1
    ;;
esac
