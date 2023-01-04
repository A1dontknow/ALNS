class Route:
    """
    :param instance: Mo ta bai toan

    Ham xay dung tuyen duong danh cho xe
        - depot (Node): Diem do
        - route (list): Tuyen duong hien tai
        - cost (int): Chi phi van tai (tinh theo quang duong)
        - load (int): Luong hang hoa tren xe
        - max_load (int) luong hang hoa duoc phep toi da tren xe
        - distance_matrix (2D list): luu ma tran khoang cach giua cac khach hang
    """
    def __init__(self, instance):
        self.depot = instance.depot
        self.route = [instance.depot]
        self.cost = 0
        self.load = 0
        self.max_load = instance.capacity
        self.distance_matrix = instance.distance_matrix

    def last_node(self):
        return self.route[len(self.route) - 1]

    def can_insert(self, node):
        return node.demand + self.load <= self.max_load

    def insert(self, node, position=-1):
        if self.can_insert(node):
            self.load += node.demand
            if position != -1:
                #print(position)
                #print(self)
                self.cost = self.cost + self.distance_matrix[self.route[position].id][node.id] + self.distance_matrix[self.route[position + 1].id][node.id] - self.distance_matrix[self.route[position].id][self.route[position + 1].id]
                self.route.insert(position + 1, node)
                #print(self)
            else:
                self.cost += self.distance_matrix[self.last_node().id][node.id]
                self.route.append(node)

    def erase(self, customer_id):
        for i in range(0, len(self.route)):
            if self.route[i].id == customer_id:
                prev_customer = self.route[i-1].id
                removing_customer = self.route[i].id
                after_customer = self.route[i+1].id
                #copy = self.cost
                #copy2 = self.distance_matrix[prev_customer][removing_customer]
                #copy3 = self.distance_matrix[removing_customer][after_customer]
                #copy4 = self.distance_matrix[prev_customer][after_customer]
                self.cost = self.cost - self.distance_matrix[prev_customer][removing_customer] - self.distance_matrix[removing_customer][after_customer] + self.distance_matrix[prev_customer][after_customer]
                self.load -= self.route[i].demand
                self.route.remove(self.route[i])
                #if self.cost < 0:
                #    print(copy, copy2, copy3, copy4, self.cost)
                #    exit(999)
                break

    def finish_route(self):
        self.cost += self.distance_matrix[self.last_node().id][self.depot.id]
        self.route.append(self.depot)

    def __str__(self):
        return f'Route: Total cost = {"%.2f" %self.cost}, load = {"%.2f" %self.load}, Customers = \n{self.route}'

    def __repr__(self):
        return str(self)
