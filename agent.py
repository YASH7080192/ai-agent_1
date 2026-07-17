from main import chat
from memory import load_memory, save_memory
from prompts import SYSTEM_PROMPT
from parse import parse_tool_call
from tools.registry import execute_tool


class Agent:

    def run(self, user_input: str):

        print("\n" + "=" * 80)
        print("USER INPUT:")
        print(user_input)
        print("=" * 80)

        # -----------------------------
        # Load Memory
        # -----------------------------
        memory = load_memory()

        # Sirf last 10 messages use karo
        memory = memory[-10:]

        print("\nMEMORY:")
        print(memory)

        # -----------------------------
        # Prepare Messages
        # -----------------------------
        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

        messages.extend(memory)

        messages.append(
            {
                "role": "user",
                "content": user_input
            }
        )

        print("\nMESSAGES SENT TO LLM:")
        for message in messages:
            print(message)

        # -----------------------------
        # Ask LLM
        # -----------------------------
        llm_response = chat(messages)

        print("\n" + "=" * 80)
        print("LLM RESPONSE:")
        print(llm_response)
        print("=" * 80)

        # -----------------------------
        # Parse Tool Call
        # -----------------------------
        tool_request = parse_tool_call(llm_response)

        print("\nPARSED TOOL REQUEST:")
        print(tool_request)
        print("=" * 80)

        # -----------------------------
        # No Tool Needed
        # -----------------------------
        if tool_request is None:

            memory.append(
                {
                    "role": "user",
                    "content": user_input
                }
            )

            memory.append(
                {
                    "role": "assistant",
                    "content": llm_response
                }
            )

            save_memory(memory)

            return llm_response

        # -----------------------------
        # Tool Required
        # -----------------------------
        print("\nTOOL REQUEST FOUND")

        tool_name = tool_request.get("tool")

        arguments = tool_request.copy()
        arguments.pop("tool", None)

        print("Tool Name:", tool_name)
        print("Arguments:", arguments)

        tool_result = execute_tool(tool_name, arguments)

        qr_path = None

        if isinstance(tool_result, dict):

            if tool_result.get("status") == "success":

                if tool_name == "qrcode":
                    qr_path = tool_result.get("path")

                tool_result = tool_result.get("message", "")

            else:

                tool_result = tool_result.get("message", "")

        else:

            tool_result = str(tool_result)

        print("\nTOOL RESULT:")
        print(tool_result)

        # -----------------------------
        # Send Tool Result Back To LLM
        # -----------------------------
        messages.append(
            {
                "role": "assistant",
                "content": llm_response
            }
        )

        messages.append(
            {
                "role": "user",
                "content": f"""
Tool Result:

{tool_result}

IMPORTANT:
- Use the tool result exactly.
- Do not invent values.
- If the tool generated a file, mention its path.
- Answer naturally.
"""
            }
        )

        final_response = chat(messages)

        print("\n" + "=" * 80)
        print("FINAL RESPONSE:")
        print(final_response)
        print("=" * 80)

        # -----------------------------
        # Save Memory
        # -----------------------------
        memory.append(
            {
                "role": "user",
                "content": user_input
            }
        )

        memory.append(
            {
                "role": "assistant",
                "content": final_response
            }
        )

        save_memory(memory)

        return {
            "response": final_response,
            "tool": tool_name,
            "qr_path": qr_path
        }