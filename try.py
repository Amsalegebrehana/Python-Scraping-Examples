import ast
import json

def parse_argument(arg):
    if isinstance(arg, ast.keyword):
        value = parse_value(arg.value)
        return {"name": arg.arg, "value": value}
    else:
        raise ValueError("Unexpected argument type: {}".format(type(arg)))

def parse_value(value):
    if isinstance(value, ast.Call):
        return parse_function(value)
    elif isinstance(value, ast.Num):
        return value.n
    elif isinstance(value, ast.Str):
        return value.s
    else:
        raise ValueError("Unexpected value type: {}".format(type(value)))

def parse_function(func):
    return {
        "name": func.func.id,
        "args": [parse_argument(arg) for arg in func.keywords]
    }

def parse_string(input_string):
    tree = ast.parse(input_string, mode='eval')
    return parse_function(tree.body)

def main():
    input_string = "myfun1(arg1=7, arg2=8, arg3=myfun3(barg1='one', barg2='two'))"
    result = parse_string(input_string)
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()