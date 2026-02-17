# assignment 1: make the modulo operator work with some test cases
import evaluator
import parser
import tokenizer

def evaluate(ast):
    if ast["tag"] == "number":
        return ast["value"]
    elif ast["tag"] == "+":
        return evaluate(ast["left"]) + evaluate(ast["right"])
    elif ast["tag"] == "-":
        return evaluate(ast["left"]) - evaluate(ast["right"])
    elif ast["tag"] == "*":
        return evaluate(ast["left"]) * evaluate(ast["right"])
    elif ast["tag"] == "/":
        return evaluate(ast["left"]) / evaluate(ast["right"])
    elif ast["tag"] == "%":
        return evaluate(ast["left"]) % evaluate(ast["right"])
    else:
        raise ValueError(f"Unknown AST node: {ast}")
    
    
def test_evaluate():
    print("test evaluate()")
    ast = {"tag": "number", "value": 3}
    assert evaluate(ast) == 3
    ast = {
        "tag": "+",
        "left": {"tag": "number", "value": 3},
        "right": {"tag": "number", "value": 4},
    }
    assert evaluate(ast) == 7
    ast = {
        "tag": "*",
        "left": {
            "tag": "+",
            "left": {"tag": "number", "value": 3},
            "right": {"tag": "number", "value": 4},
        },
        "right": {"tag": "number", "value": 5},
    }
    assert evaluate(ast) == 35
    
    # test modulo operator
    ast = {
        "tag": "%",
        "left": {"tag": "number", "value": 8},
        "right": {"tag": "number", "value": 3},
    }
    assert evaluate(ast) == 2
    # test modulo operator with negative numbers
    ast = {
        "tag": "%",
        "left": {"tag": "number", "value": -8},
        "right": {"tag": "number", "value": 3},
    }
    assert evaluate(ast) == 1
    ast = {
        "tag": "%",
        "left": {"tag": "number", "value": 8},
        "right": {"tag": "number", "value": -3},
    }
    assert evaluate(ast) == -1
    ast = { 
        "tag": "%",
        "left": {"tag": "number", "value": -8},
        "right": {"tag": "number", "value": -3},
    }
    assert evaluate(ast) == -2
    # 0 cases
    ast = {
        "tag": "%",
        "left": {"tag": "number", "value": 20},
        "right": {"tag": "number", "value": 0},
    }
    try:
        evaluate(ast)
        assert False, "Expected ZeroDivisionError"
    except ZeroDivisionError:
        pass
    ast = {
        "tag": "%",
        "left": {"tag": "number", "value": 0},
        "right": {"tag": "number", "value": 10},
    }
    assert evaluate(ast) == 0
    ast = {
        "tag": "%",
        "left": {"tag": "number", "value": 0},
        "right": {"tag": "number", "value": 0},
    }
    try:
        evaluate(ast)
        assert False, "Expected ZeroDivisionError"
    except ZeroDivisionError:
        pass

if __name__ == "__main__":
    test_evaluate()
    print("done.")