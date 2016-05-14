from StringIO import StringIO

from graver.lib import Lib
from graver.reader.xml_reader import XMLReader

libSource = '\
    <dict>                                      \
      <key>com.letterror.somestuff</key>        \
      <string>arbitrary custom data!</string>   \
      <key>public.markColor</key>               \
      <string>1,0,0,0.5</string>                \
    </dict>                                     \
  '


class TestLib(object):

    def test_attribute_access(self):
        lib = Lib(libSource)
        assert lib['com.letterror.somestuff'] == "arbitrary custom data!"
        assert lib['public.markColor'] == "1,0,0,0.5"
