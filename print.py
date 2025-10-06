#doing a def practice without return
def name(thename):
    kingname = thename + " king"
    print(kingname)

#this is the return code practice
name("almog")

print("return method now")

def name(thename):
    kingname = thename + " king"
    return kingname

result = name("almog")
print(result)
