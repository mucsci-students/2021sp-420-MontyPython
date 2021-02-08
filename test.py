from ClassCollection import ClassCollection
import interface

col = ClassCollection()

col.addClass("foo")
col.addAttribute("foo", "attr1")
col.addAttribute("foo", "attr2")
col.addClass("bar")
col.addAttribute("bar", "attr1")
col.addAttribute("bar", "attr3")
col.addClass("fox")

interface.listClass(col, "foo")
interface.listClass(col, "bar")
interface.listClass(col, "fox")
