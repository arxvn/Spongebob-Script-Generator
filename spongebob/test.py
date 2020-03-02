output = open("output.csv", "a")

for line in open("yeet.csv"):
    output.write(line)

for num in range(2,3):
    f = open("yeet" + str(num)+ ".csv")
    for line in f:
        output.write(line)
    f.close()
output.close()