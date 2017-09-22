from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.mites import mites


def test_mites():
  """Test module mites.py by downloading
   mites.csv and testing shape of
   extracted data has 47 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = mites(test_path)
  try:
    assert x_train.shape == (47, 2)
  except:
    shutil.rmtree(test_path)
    raise()
