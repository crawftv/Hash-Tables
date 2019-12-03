from hashtable import HashTable
ht = HashTable(8)

ht.insert("key-0", "val-0")
ht.insert("key-1", "val-1")
ht.insert("key-2", "val-2")
ht.insert("key-3", "val-3")
ht.insert("key-4", "val-4")
ht.insert("key-5", "val-5")
ht.insert("key-6", "val-6")
ht.insert("key-7", "val-7")
ht.insert("key-8", "val-8")
ht.insert("key-9", "val-9")

ht.resize()

len(ht.storage) == 16
import pdb; pdb.set_trace()
return_value = ht.retrieve("key-0")
return_value == "val-0"
return_value = ht.retrieve("key-1")
return_value == "val-1"
return_value = ht.retrieve("key-2")
return_value == "val-2"
return_value = ht.retrieve("key-3")
return_value == "val-3"
