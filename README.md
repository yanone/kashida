# Kashida
 
Insert kashidas correctly into Arabic text: Only once per word, and following the rules as layed out in the [Kashida Secret](https://www.khtt.net/en/page/1821/the-big-kashida-secret)

# Usage

```python
import kashida

# Obtain kashida for single word
>>> kashida.word("كشيدة")
>>> كشـيدة

# Obtain kashida for whole text at once
>>> kashida.text("انا بحب الكشيدة")
>>> انـا بحـب الكشـيدة
```
