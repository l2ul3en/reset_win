import pytest
from pathlib import PurePath

path = PurePath('tests','TestFlowReset.py')
pytest.main([str(path), '-s'])