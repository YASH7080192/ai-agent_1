from .calculater import execute as calculator
from .weather import execute as weather
from .time_tool import execute as time_tool
from .currency import execute as currency
from .qrcode_tool import execute as qrcode


tools = {
    "calculator": calculator,
    "weather": weather,
    "time": time_tool,
    "currency": currency,
    "qrcode": qrcode,

}


def execute_tool(tool_name: str, arguments: dict):
    tool = tools.get(tool_name)

    if tool is None:
        return f"Unknown tool: {tool_name}"

    return tool(arguments)


def list_tools():
    return list(tools.keys())


if __name__ == "__main__":

    print("===== Registered Tools =====\n")
    print(list_tools())

    print("\n===== Calculator =====")
    print(
        execute_tool(
            "calculator",
            {
                "expression": "25*18"
            }
        )
    )

    print("\n===== Time =====")
    print(
        execute_tool(
            "time",
            {}
        )
    )

    print("\n===== Weather =====")
    print(
        execute_tool(
            "weather",
            {
                "city": "London"
            }
        )
    )

    print("\n===== Currency =====")
    print(
        execute_tool(
            "currency",
            {
                "amount": 100,
                "from": "USD",
                "to": "INR"
            }
        )
    )

    print("\n===== QR Code =====")
    print(
        execute_tool(
            "qrcode",
            {
                "text": "https://google.com"
            }
        )
    )