import util
import net

if __name__ == "__main__":
    for i in range(10):
        datas = util.read_data("data/" + str(i) +".txt")
        n = net.Net()    
        for i in datas:
            n.train(i)

    print n.w
    
