# Kashida
 
Insert Kashidas typographically correct into Arabic text via a nifty Python package:
Only once per word, and following the rules as layed out in Khtt.net’s [Kashida Secret](https://www.khtt.net/en/page/1821/the-big-kashida-secret), which defines rules for typesetting Kashidas in Naskh script.

The implementation is in its infancy because letters are currently hard-coded into the code and should be replaced by a more dynamic Unicode-based recognition. Nonetheless, it should work for most Arabic-script-based languages.

If you find that a word isn’t getting the right amount of Kashida love (according to the Kashida Secret rules), consider to raise an issue at https://github.com/yanone/kashida/issues

# Installation

Obtain it from PyPI: 
```
pip install kashida
```

# Usage

```python
import kashida

# Obtain kashida for single word
>>> kashida.word("كشيدة")
>>> كشـيدة

# Obtain kashidas for a whole text, once per word
>>> kashida.text("انا بحب الكشيدة")
>>> انـا بحـب الكشـيدة
```
