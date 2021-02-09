from ClassCollection import ClassCollection

col = ClassCollection()

col.addClass("foo")
col.addClass("bar")

col.addRelationship("foo", "bar")

print(col.getRelationship("foo", "bar"))

for k,v in col.relationshipDict.items():
    print(k,v)

