import ast
import operator as op
import math

OPERATORS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.Mod: op.mod,
    ast.USub: op.neg,
}

FUNCTIONS = {
    "sqrt": math.sqrt,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "abs": abs,
}


def calculate(expression: str):
    try:
        tree = ast.parse(expression, mode="eval")
        result = _evaluate(tree.body)
        return str(result)
    except Exception as e:
        return f"Calculator Error: {e}"


def _evaluate(node):

    if isinstance(node, ast.Constant):
        return node.value

    elif isinstance(node, ast.BinOp):
        return OPERATORS[type(node.op)](
            _evaluate(node.left),
            _evaluate(node.right)
        )

    elif isinstance(node, ast.UnaryOp):
        return OPERATORS[type(node.op)](
            _evaluate(node.operand)
        )

    elif isinstance(node, ast.Call):

        if not isinstance(node.func, ast.Name):
            raise ValueError("Invalid function")

        func_name = node.func.id

        if func_name not in FUNCTIONS:
            raise ValueError(f"Unsupported function: {func_name}")

        args = [_evaluate(arg) for arg in node.args]

        return FUNCTIONS[func_name](*args)

    raise ValueError("Unsupported expression")


def execute(arguments: dict):

    expression = arguments.get("expression")

    if not expression:
        return "Calculator Error: Expression not provided."

    return calculate(expression)


if __name__ == "__main__":

    print("Calculator Tool\n")

    print(
        execute(
            {
                "expression": "25*18"
            }
        )
    )

    print(
        execute(
            {
                "expression": "sqrt(625)"
            }
        )
    )