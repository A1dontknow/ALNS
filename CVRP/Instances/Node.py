import numpy as np


class Node:
    """
    :param id: ID cua khach hang
    :param x: Hoanh do khach hang
    :param y: Tung do khach hang
    :param demand: Nhu cau khoi luong hang hoa cua khach hang

    Ham xay dung cac thuoc tinh da neu o tren cua khach hang
    """
    def __init__(self, id, x, y, demand):
        # id of the customers
        self.id = int(id)
        # Coordinate of the customers
        self.x = np.array(int(x))
        self.y = np.array(int(y))
        # Demand of customers
        self.demand = int(demand)

    def __str__(self):
        return f'Customer: ID = {self.id}\t (x, y) = {"%2d" %self.x} {"%2d" %self.y}\t\t demand = {self.demand}\n'

    def __repr__(self):
        return str(self)
