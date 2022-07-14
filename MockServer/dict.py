

from responses import __all__ as modules
import importlib
import sys

responses_dict={}

for res in modules:
    module_name = "responses." + res
    module_type = importlib.import_module(module_name)
    responses_dict[module_type.url] = module_type.body
