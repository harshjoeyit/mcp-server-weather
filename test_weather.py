# test_weather.py
import asyncio
from mcp import ClientSession
from mcp.client.sse import sse_client

async def main():
    async with sse_client("http://127.0.0.1:8000/sse") as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # List tools
            tools = await session.list_tools()
            print("Tools:", [t.name for t in tools.tools])

            # Test get_alerts
            result = await session.call_tool("get_alerts", {"state": "CA"})
            print("\n--- Alerts ---\n", result.content[0].text[:300])

            # Test get_forecast (San Francisco)
            result = await session.call_tool("get_forecast", {
                "latitude": 37.7749,
                "longitude": -122.4194
            })
            print("\n--- Forecast ---\n", result.content[0].text[:300])

asyncio.run(main())