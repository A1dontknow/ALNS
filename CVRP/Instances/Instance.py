from sys import platform
import numpy as np
import re
from CVRP.Config import Config
from CVRP.Instances.Node import Node


class Instance:
    """
    :param file_name: File bai toan de giai

    Ham nay de dung cac thuoc tinh cho bai toan
        - optimal (float): Gia tri toi uu biet truoc
        - vehicles (int): So xe
        - capacity (int): Tai trong cua xe
        - dimensions (int): So luong khach hang (= so luong yeu cau)
        - customers (list Node): Thong tin cua cac khach hang
        - depot (Node): Diem lay hang cua moi xe
        - distance_matrix (2D float): Ma tran khoang cach giua cac khach hang va kho voi nhau
    """
    def __init__(self, file_name):
        self.optimal = None
        self.vehicles = None
        self.capacity = None
        self.dimensions = 0
        # Customers are mapped with nodes
        self.customers = []
        self.depot = None
        self.distance_matrix = []
        self.load_data(file_name)
        self.create_distance_matrix()

    def load_data(self, file_name):
        try:
            f = None
            if platform == "linux" or platform == "linux2":
                try:
                    f = open(Config.PROJECT_PATH + "/Dataset/" + file_name)
                except FileNotFoundError:
                    try:
                        f = open(Config.PROJECT_PATH + "/Dataset/" + file_name + ".txt")
                    except FileNotFoundError:
                        print("Ten file khong dung")
                        exit(-1)
            elif platform == "win32":
                try:
                    f = open(Config.PROJECT_PATH + "\\Dataset\\" + file_name)
                except FileNotFoundError:
                    try:
                        f = open(Config.PROJECT_PATH + "\\Dataset\\" + file_name + ".txt")
                    except FileNotFoundError:
                        print("Ten file khong dung")
                        exit(-1)

            lines = f.readlines()
            line_two = re.findall(r'\d+',lines[1])
            # Input binh thuong co the khong co thong tin ve optimal
            try:
                self.optimal = int(line_two[1])
            except Exception:
                self.optimal = -1
            self.vehicles = int(line_two[0])
            self.dimensions = int(re.findall(r'\d+', lines[3])[0])
            self.capacity = int(re.findall(r'\d+', lines[5])[0])

            # Tu dong 8 lay thong tin vi tri kho, khach hang va nhu cau cua khach
            for i in range(self.dimensions):
                demand = int(lines[8 + self.dimensions + i].split().pop())
                node = lines[7 + i].split()
                y = node.pop()
                x = node.pop()
                # Truong hop kho. Gia su rang kho se co demand = 0
                if demand == 0:
                    self.depot = Node(i, x, y, demand)
                else:
                    self.customers.append(Node(i, x, y, demand))
        except Exception:
            print("Loi nhap du lieu: Du lieu khong khop dinh dang")
            exit(-1)

    # Tao ma tran khoang cach giua khach hang va depot voi nhau
    def create_distance_matrix(self):
        nodes = [self.depot] + self.customers
        for i in range(len(nodes)):
            row = []
            for j in range(len(nodes)):
                if i == j:
                    row.append(0)
                else:
                    vector = np.array([nodes[i].x - nodes[j].x, nodes[i].y - nodes[j].y])
                    row.append(np.linalg.norm(vector))
            self.distance_matrix.append(row)
        self.distance_matrix = np.array(self.distance_matrix)
