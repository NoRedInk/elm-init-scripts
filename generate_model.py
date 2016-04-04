import os
import os.path

model_template = """
module {module_name}.Model where

type alias Model =
  {{}}
"""

def make_boilerplate(module_name, directory):
    file_path = os.path.join(directory, 'Model.elm')
    templated = model_template.format(module_name=module_name)

    with open(file_path, 'w') as f:
        f.write(templated)

def make_directory(directory):
    try:
        os.makedirs(directory)
    except OSError as e:
        if e.errno == errno.EEXIST and os.path.isdir(actual_path):
            pass
        else:
            raise

def bootstrap(module_name, directory):
    make_directory(directory)
    make_boilerplate(module_name, directory)
