def read_data(path):
    datas = []
    with open(path, "r") as fin:
        for i in fin:
            tmp = [float(num) for num in i.strip().split(" ")]
            tmp = map(lambda x:float(x), tmp)
            datas.append([tmp[:-1], tmp[-1]])
    return datas
