from .extdl import *
from .paste import *
from JoKeRUB.helpers.utils import _catutils
from . import _cattools

flag = True
check = 0
while flag:
    try:
        from . import format as _format
        from .events import *
        from .format import *
        break
    except ModuleNotFoundError as e:
        install_pip(e.name)
        check += 1
        if check > 5:
            break