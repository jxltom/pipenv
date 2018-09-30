import sys

import pipenv as project


if __name__ == '__main__':
    sys.argv = sys.argv[1:] if len(sys.argv) > 1 \
        else raw_input('manage.py@{} > '.format(project.__name__)).split()

    if sys.argv[0] == 'test':
        import pytest

        sys.argv[0] = 'py.test'
        sys.exit(pytest.main())
