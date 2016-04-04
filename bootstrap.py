import argparse
import errno
import os
import os.path

model_template = """
module {module_name}.Model where

type alias Model =
  {{}}
""".lstrip()

def make_boilerplate(module_name, directory):
    file_path = os.path.join(directory, 'Model.elm')
    templated = model_template.format(module_name=module_name)

    with open(file_path, 'w') as f:
        f.write(templated)

def make_directory(directory):
    try:
        os.makedirs(directory)
    except OSError as e:
        if e.errno == errno.EEXIST and os.path.isdir(directory):
            pass
        else:
            raise

def bootstrap(module_name, root_directory):
    directory = os.path.join(root_directory, *module_name.split('.'))

    make_directory(directory)
    make_boilerplate(module_name, directory)

def main():
    parser = argparse.ArgumentParser(description='Initialize an Elm page')

    parser.add_argument('module_name', help='the component name e.g Some.Module.Name')
    parser.add_argument('destination', help='the destination folder. Defaults to current', default="./")
    args = parser.parse_args()

    bootstrap(args.module_name, args.destination)

if __name__ == '__main__':
    main()
