try:
    import os
    import re
    import inspect
except (ModuleNotFoundError, ImportError) as error:
    print("The following error was raised while trying to import the modules: " + error)


def _get_parser_list(dirname: str) -> list[str]:
    """readts the parsers available"""
    files = [f.replace('.py', '')
             for f in os.listdir(dirname)
             if not f.startswith('__')]

    return files


def _import_parsers(parserfiles: [str]):
    """import the parsers"""
    m = re.compile('.+parser$', re.I)

    _modules = __import__('climaterm.parsers',
                          globals(),
                          locals(),
                          parserfiles,
                          0)

    _parsers = [(k, v) for k, v in inspect.getmembers(_modules)
                if inspect.ismodule(v) and m.match(k)]

    _classes = dict()

    for k, v in _parsers:
        _classes.update({k: v for k, v in inspect.getmembers(v)
                         if inspect.isclass(v) and m.match(k)})

    return _classes


def load(dirname):
    parserfiles = _get_parser_list(dirname)
    return _import_parsers(parserfiles)
