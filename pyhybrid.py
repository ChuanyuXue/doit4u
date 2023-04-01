import re
import openai

INSTRUCTIONS = "\n".join([
    "\n\n"
    "Requirements:",
    "Please make sure the answer is a single Python function without anything outside of it.",
    "Please do not add any comments.",
    "Please do not print statements to the code.",
    "Please pay attention to the boundaries.",
])


class PyHybrid:

    def __init__(self, model="text-davinci-003", **kwargs):
        check_args(kwargs)

        self.model = model
        self.instructions = INSTRUCTIONS
        self.model_kwargs = complete_args(kwargs)
        self.funcs = {}

    def hybrid(self, prompt: str):
        func_key = hash(prompt)
        if func_key in self.funcs:
            return self.funcs[func_key]
        else:
            response = self._request_gpt(prompt + self.instructions)
            code_text = response["choices"][0]["text"]
            func = self._convert_str_to_code(code_text)
            self.funcs[func_key] = func
            return func

    def _request_gpt(self, prompt: str) -> dict:
        response = openai.Completion.create(
            engine=self.model,
            prompt=prompt,
            max_tokens=self.model_kwargs['max_tokens'],
            n=self.model_kwargs['n'],
            stop=self.model_kwargs['stop'],
            temperature=self.model_kwargs['temperature'],
        )
        check_response(response)
        return response

    def _convert_str_to_code(self, code_text: str) -> callable:
        func_name = extract_function_name(code_text)
        try:
            exec(code_text, locals())
        except Exception as e:
            raise ValueError(f"Error executing code: {e}")
        return locals()[func_name]


def check_model(model: str) -> None:
    models = openai.Model.list()["data"]
    model_ids = [model["id"] for model in models]
    if model not in model_ids:
        raise ValueError(
            f"Model {model} not found. Available models: {model_ids}")


def check_args(args: dict) -> None:
    expected_args = {
        'max_tokens',
        'n',
        'stop',
        'temperature',
    }
    for key in args:
        if key not in expected_args:
            raise ValueError(f"Unexpected argument: {key}")


def complete_args(args: dict) -> dict:
    default_args = {
        'max_tokens': 256,
        'n': 1,
        'stop': None,
        'temperature': 0.5,
    }
    for key in default_args:
        if key not in args:
            args[key] = default_args[key]
    return args


def check_response(response: dict) -> None:
    if response["object"] != "text_completion":
        raise ValueError(f"Unexpected response object: {response['object']}")
    if response["choices"] == []:
        raise ValueError("Model returned no choices.")
    if response["choices"][0]["finish_reason"] != "stop":
        raise ValueError(
            f"Model did not stop. Finish reason: {response['choices'][0]['finish_reason']}"
        )


def extract_function_name(code_string):
    pattern = r"def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\("
    match = re.search(pattern, code_string)

    if match:
        return match.group(1)
    else:
        return None
