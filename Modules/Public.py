import importlib
import os
import platform


def get_obj_by_path(filename):
    if os.path.isfile(filename + '.py'):
        filename = filename + '.py'
        nnnnnnnnnnnn1 = importlib.machinery.SourceFileLoader(
            os.path.splitext(filename)[0], filename).load_module()
    elif os.path.isfile(filename + '.pyc'):
        filename = filename + '.pyc'
        module_spec = importlib.util.spec_from_file_location(filename[:-4],
                                                             filename)
        nnnnnnnnnnnn1 = importlib.util.module_from_spec(module_spec)
        module_spec.loader.exec_module(nnnnnnnnnnnn1)
    else:
        sysstr = platform.system()
        if (sysstr == "Windows"):
            new_filename =  filename + '.pyd'
            # filename = filename + '.pyd'
        elif (sysstr == "Linux"):
            new_filename = filename + '.so'
        else:
            new_filename = filename + '.py'
        if os.path.isfile(new_filename):

            loader_details = (
                importlib.machinery.ExtensionFileLoader,
                importlib.machinery.EXTENSION_SUFFIXES
            )
            tools_finder = importlib.machinery.FileFinder(
                os.path.dirname(new_filename), loader_details)
            # print("FileFinder: ", tools_finder)
            toolbox_specs = tools_finder.find_spec(
                os.path.basename(os.path.splitext(new_filename)[0]))
            # print("find_spec: ", toolbox_specs)
            nnnnnnnnnnnn1 = importlib.util.module_from_spec(toolbox_specs)
            # print("module: ", nnnnnnnnnnnn1)
            toolbox_specs.loader.exec_module(nnnnnnnnnnnn1)
            # print("导入成功 path_import(): ", nnnnnnnnnnnn1)
        else:
            nnnnnnnnnnnn1 =None
    return nnnnnnnnnnnn1