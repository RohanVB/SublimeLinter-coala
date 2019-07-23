from SublimeLinter.lint import Linter, PythonLinter
# from run_coala import UseCoala

# todo: fix regex and use coala-on-single-file

class coala(PythonLinter):
    cmd = ('coala --format')
    regex = r'^.*:line:(?P<line>\d+):\w+:(?P<col>\w+):\S+:(?P<message>(.+))'
    multiline = True
    defaults = {
        'selector': 'source.python',
    }

# ^.*:line:(?P<line>\d+):\w+:(?P<col>\d+):\w+:\d:\w+:\d+:\w+:\d:\w+:\w+:\w+:(?P<message>.+