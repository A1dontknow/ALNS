import time
from matplotlib import pyplot as plt
from CVRP.Algorithm.NearestNeighbor import NearestNeighbor
from CVRP.Algorithm.AdaptiveMechanism import AdaptiveMechanism
from CVRP.Algorithm.LocalSearch import local_search
from CVRP.Instances.Instance import Instance
from copy import deepcopy
from CVRP.Config import *


def solve(filename):
    """
    :param filename: Ten file bai toan
    :return:

    Ham nay giai bai toan VRP bang thuat toan Adaptive Large Neighborhood Search. Ket qua thuat
    toan se phu thuoc vao cac tham so nam trong file /Instance/Config.py. Khi chay xong, ket qua
    se duoc luu vao /Dataset/Solution/<ten file>/
    """

    adt = AdaptiveMechanism()
    # Tao nghiem ban dau cho bai toan
    best = NearestNeighbor(Instance(filename)).get_initial_solution()
    ips = Config.ITERATION / Config.SEGMENT

    s = deepcopy(best)
    print("Ket qua sinh nghiem ban dau:")
    print(best)
    test = 0
    print("ALNS Process...")

    # Lap thuat toan den so luong lan lap nhat dinh
    for i in range(Config.ITERATION):
        # test la co che thu nghiem
        test += 1
        s2 = deepcopy(s)
        # Chon ra cap operator tu co che Roulette wheel
        operators = adt.select_operator()
        # destroy
        s2 = operators[0](s2, int(Config.DESTROY_RATIO * s2.instance.dimensions), d=Config.D)
        # repair
        s2 = operators[1](s2)

        # Trong truong hop nghiem s2 sau khi sua khong cp van de gi
        if s2 is not None:
            # Neu nghiem moi tot hon nghiem cu -> accept
            if s2.totalCost < s.totalCost:
                s2 = local_search(s2)
                s = deepcopy(s2)
                # Neu nghiem cu tot hon nghiem tot nhat tim duoc -> cap nhat trang thai ALNS len console
                if s2.totalCost < best.totalCost:
                    print(s2.totalCost)
                    test = 0
                    best = deepcopy(s2)
                    # Cap nhat diem dua tren performance
                    adt.update_score(operators, Config.PHI_1)
                else:
                    adt.update_score(operators, Config.PHI_2)
            else:
                adt.update_score(operators, Config.PHI_3)

            # Co che chap nhan nghiem dang duoc thu nghiem (Inspire tu thuat toan Record-to-Record)
            if s2.totalCost < best.totalCost + Config.DEVIATION:
                s = deepcopy(s2)

            # Considering very good effect (+150 for 2k total cost) (+100 for n39k6). Con time thi phat trien
            if test >= 1000 and s2.totalCost <= best.totalCost + Config.BIG_DEVIATION:
                s = deepcopy(s2)
                test = 0
        else:
            adt.update_score(operators, Config.PHI_3)

        # Vao dau moi segment, cap nhat trong so cac operator va tien hanh Local Search len nghiem hien tai
        if (i + 1) % ips == 0:
            adt.update_weight()
            s = local_search(s)
            if s.totalCost < best.totalCost:
                best = deepcopy(s)

    # In ra nghiem tot nhat tim duoc
    print(best)

    # Luu ket qua vao file
    t = time.localtime()
    current_time = time.strftime("%H_%M_%S", t)
    if not os.path.exists(Config.PROJECT_PATH + "\\Dataset\\Solution\\" + filename.split(".txt")[0]):
        os.mkdir(Config.PROJECT_PATH + "\\Dataset\\Solution\\" + filename.split(".txt")[0])
    f = open(Config.PROJECT_PATH + "\\Dataset\\Solution\\" + filename.split(".txt")[0] + "\\" + current_time + ".txt", "wt")
    f.write(best.__str__())
    f.close()

    for route in best.routes:
        x = []
        y = []
        for node in route.route:
            x.append(node.x)
            y.append(node.y)
        plt.plot(x, y)
        plt.plot(x, y, 'or')
        plt.plot(best.routes[0].route[0].x, best.routes[0].route[0].y, "sk")
    plt.title("VRP Solution (Cost = " + str("%.2f" % best.totalCost) + ")")
    plt.savefig(Config.PROJECT_PATH + "\\Dataset\\Solution\\" + filename.split(".txt")[0] + "\\" + current_time + ".png")
    print("Anh va file da duoc luu vao trong thu muc <ProjectPath>\\CVRP\\Dataset\\Solution\\<Ten file>\\")
    plt.show()


