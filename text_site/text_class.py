class text:


    def captilize(value):
        val = value.upper()
        return (val)

    def lower(value):
        val = value.lower()
        return (val)

    def length(value):
        val = len(value)
        return (val)

    def removepun(value):
        spclchr = '''~`!@#$%^&*()_+-={}[]|\:";'<>?,./*-'''
        new_str = ''
        for i in value:
            if i not in spclchr:
                new_str = new_str + i
        return new_str
'''str1 = "achu"
str2 = str1.upper()
print(str2)'''
