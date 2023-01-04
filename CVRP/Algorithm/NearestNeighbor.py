from CVRP.Instances.Route import Route
from CVRP.Instances.Solution import Solution


class NearestNeighbor:
    """
    :param instance: Representation cua bai toan

    Ham dung nay dung cac thuoc tinh roi sinh nghiem ban dau, chi tiet cac thuoc tinh:
            - customers (list): luu tru cac Node la khach hang
            - distanceMatrix (2D float): Ma tran khoang cach luu thong tin khoang cach giua 2 khach hang bat ki
            - capacity (int): tai trong cua moi xe
            - numberOfVehicle (int): So luong xe
            - depot (Node): depot trong mo hinh CVRP
            - vehicles (list): Cac tuyen duong danh cho moi xe
    """
    def __init__(self, instance):
        self.instance = instance
        self.customers = instance.customers
        self.distanceMatrix = instance.distance_matrix
        self.numberOfVehicle = instance.vehicles

    def get_initial_solution(self):
        """
        :return Nghiem ko can nhat thiet phai tot, mien la dung nghiem nhanh la duoc

        Ham nay dung nghiem ban dau cho bai toan bang Nearest Neighbor Heuristic
        """
        # solution chua tap hop cac route de tra ve
        solution = []
        current_route = Route(self.instance)

        # lap lai cho den khi toan bo khach hang da duoc phuc vu
        while len(self.customers) != 0:
            # Lay ra khach hang cuoi cung trong route hien tai
            current_customer = current_route.last_node()
            min_distance = 999999999
            closet_node = None

            # Tim ra khach hang co vi tri gan nhat voi khach hang cuoi cung cua route hien tai
            for i in self.customers:
                if current_route.can_insert(i):
                    distance = self.distanceMatrix[current_customer.id][i.id]
                    if distance < min_distance:
                        min_distance = distance
                        closet_node = i

            # Xet khach hang gan nhat. Neu ko null thi them vao route va xoa trong danh sach customer can them vao
            if closet_node is not None:
                current_route.insert(closet_node)
                self.customers.remove(closet_node)
            # Neu khong insert duoc thi sang xe khac de insert. Neu day la xe cuoi cung thi return
            else:
                current_route.finish_route()
                solution.append(current_route)
                current_route = Route(self.instance)

                if len(solution) == self.numberOfVehicle:
                    return Solution(solution)

        # Insert route cuoi cung khi het khach hang
        current_route.finish_route()
        solution.append(current_route)

        # khoi tao not cho cac xe neu chua co khach hang nao
        while len(solution) < self.numberOfVehicle:
            solution.append(Route(self.instance).finish_route())

        return Solution(solution, self.instance)
