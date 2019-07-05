from SublimeLinter.lint import Linter


class newcoalalinter(Linter):
    cmd = ('coala --format')
    regex = r'^.+?:(?P<line>\d+):'
    multiline = True
    defaults = {
        'selector': 'source.python',
        '--select=,': '',
        '--ignore=,': '',
        '--max-line-length=': None
    }
