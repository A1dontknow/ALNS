from CVRP.Algorithm.DestroyOperator import *
from CVRP.Algorithm.RepairOperator import *
from CVRP.Config import Config
from random import choices


class AdaptiveMechanism:
    def __init__(self):
        self.destroy_operator = [ShawDestroy.shaw_destroy, RandomDestroy.random_destroy, WorstDestroy.worst_destroy, MassiveDestroy.massive_destroy]
        self.repair_operator = [GreedyRepair.greedy_repair, RandomRepair.random_repair]

        self.destroy_weight = [1, 1, 1, 1]
        self.repair_weight = [1, 1]

        self.destroy_score = [0, 0, 0, 0]
        self.repair_score = [0, 0]

        self.destroy_used = [0, 0, 0, 0]
        self.repair_used = [0, 0]

    def select_operator(self):
        """
        :return: Tra ve 1 cap destroy - repair operator theo co che roulette-wheel (uu tien chon operator co trong so cao)
        """
        return choices(self.destroy_operator, weights=self.destroy_weight, k=1)[0], choices(self.repair_operator, weights=self.repair_weight, k=1)[0]

    def update_score(self, operator, phi):
        """
        :param operator: 1 cap destroy - repair
        :param phi: performance
        :return:

        Ham update diem dua tren performance phi va so lan da su dung operator
        """
        destroy_index = self.destroy_operator.index(operator[0])
        repair_index = self.repair_operator.index(operator[1])
        self.destroy_score[destroy_index] += phi
        self.destroy_used[destroy_index] += 1
        self.repair_score[repair_index] += phi
        self.repair_used[repair_index] += 1

    def update_weight(self):
        """
        :return:

        Ham update trong so cua cac operator dua tren past performance
        """
        # Update destroy
        for i in range(len(self.destroy_operator)):
            if self.destroy_used[i] != 0:
                w = self.destroy_weight[i]
                pi = self.destroy_score[i]
                o = self.destroy_used[i]
                self.destroy_weight[i] = (1 - Config.N) * w + Config.N * pi / (Config.V * o)

        # Update repair
        for i in range(len(self.repair_operator)):
            if self.repair_used[i] != 0:
                w = self.repair_weight[i]
                pi = self.repair_score[i]
                o = self.repair_used[i]
                self.repair_weight[i] = (1 - Config.N) * w + Config.N * pi / (Config.V * o)

        # Reset het diem va so lan da dung
        self.destroy_score = [0, 0, 0, 0]
        self.repair_score = [0, 0]
        self.destroy_used = [0, 0, 0, 0]
        self.repair_used = [0, 0]

