from os import getenv
from agno.agent import Agent
from agno.tools.mcp import MCPTools
from agno.models.openai.like import OpenAILike

from dotenv import load_dotenv

load_dotenv(override=True)


async def run_agent(message: str) -> None:
    playwright_tools = MCPTools(command="npx -y @playwright/mcp@latest")
    await playwright_tools.connect()

    try:
        agent = Agent(
            model=OpenAILike(
                id="gemini-2.5-pro",
                api_key=getenv("GEMINI_API_KEY"),
                base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
            ),
            tools=[playwright_tools],
            instructions="你是一个浏览器自动化专家，擅长使用浏览器工具完成各种任务。所有给你的任务都需要使用浏览器工具来完成。",
        )
        await agent.aprint_response(message, stream=True)

    finally:
        await playwright_tools.close()


if __name__ == "__main__":
    import asyncio

    # Pull request example
    asyncio.run(run_agent("使用google搜索一下今天BTC的价格是多少"))
