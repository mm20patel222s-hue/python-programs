# Write a Python program to work with the following functions/methods which
# operates on dictionary in Python with suitable examples: i) dict( ) ii) len( ) iii) clear( )
# iv) get( ) v) pop( )vi)popitem( ) vii) keys( ) viii) values() ix) items( ) x) copy( ) xi)
# update( )

d = dict(name="Bob", age=22, city="Rajkot")

print("Original Dictionary:", d)
print("Length:", len(d))
print("Get age:", d.get("age"))

d.update({"gender": "Male"})
print("After update:", d)

d.pop("city")
print("After pop('city'):", d)

d["country"] = "India"
print("After adding country:", d)

print("Keys:", d.keys())
print("Values:", d.values())
print("Items:", d.items())

d2 = d.copy()
print("Copied Dictionary:", d2)

d.popitem()
print("After popitem():", d)

d.clear()
print("After clear():", d)