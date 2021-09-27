import random, string

txt = open('codes.txt', 'w+')

for i in range(5000):
    code = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(6)).lower()
    print(code)
    txt.write(f"{code}\n")

txt.close()

# for line in txt:
#     print(line.replace(" ","").replace("\n",""))
