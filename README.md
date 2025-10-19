## 项目简介

`autoGUI` 使用 [Agno](https://docs.agno.io/) 构建了一个浏览器自动化智能体。该智能体调用谷歌 Gemini 接口，并通过 MCP 协议接入 Playwright 工具，从而执行浏览器搜索等任务。

## 环境准备

1. 安装 [uv](https://docs.astral.sh/uv/)。macOS / Linux 可以使用：
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
   Windows 用户可参考官方文档或使用 `pip install uv`。
2. 在项目根目录同步依赖：
   ```bash
   uv sync
   ```
3. 在 `.env` 中设置 Gemini API 访问密钥：
   ```bash
   GEMINI_API_KEY=你的密钥
   ```

> 运行 Playwright MCP 时需要系统已安装 Node.js（用于执行 `npx`）。

## 运行示例

```bash
uv run python base_model.py
```

脚本会创建一个自动化代理并示范如何查询当前 BTC 价格。你可以在代码中修改提示词，指示代理完成其他的浏览器自动化任务。
