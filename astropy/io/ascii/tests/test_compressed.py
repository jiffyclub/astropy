import os
import numpy as np

from ....tests.helper import pytest
from .. import read
from .common import numpy_lt_1p5

ROOT = os.path.abspath(os.path.dirname(__file__))


@pytest.mark.parametrize('filename', ['t/daophot.dat.gz', 't/latex1.tex.gz',
                                      't/short.rdb.gz'])
def test_gzip(filename):
    t_comp = read(os.path.join(ROOT, filename))
    t_uncomp = read(os.path.join(ROOT, filename.replace('.gz', '')))
    assert t_comp.dtype.names == t_uncomp.dtype.names
    assert np.all(t_comp._data == t_uncomp._data)


@pytest.mark.parametrize('filename', ['t/short.rdb.bz2', 't/ipac.dat.bz2'])
def test_bzip2(filename):
    # Can't read IPAC file with numpy 1.4
    if numpy_lt_1p5 and filename == 't/ipac.dat.bz2':
        return
    t_comp = read(os.path.join(ROOT, filename))
    t_uncomp = read(os.path.join(ROOT, filename.replace('.bz2', '')))
    assert t_comp.dtype.names == t_uncomp.dtype.names
    assert np.all(t_comp._data == t_uncomp._data)
