with open("output.txt", "w") as fw:
    with open("sample.csv") as fr:
        for line in fr:
            print(line, end="", file=fw)
