class Solution:
    """
    :param routes: Cac tuyen xe
    :param instance: Mo ta cua bai toan

    Ham xay dung loi giai bao gom:
        - instance (Instance): Mo ta bai toan
        - routes (list): Danh sach cac tuyen xe
        - extracted_node (list): Danh sach cac khach hang bi loai boi destroy operator
        - totalCost (int): Tong chi phi cua nghiem hien tai
    """
    def __init__(self, routes, instance):
        self.instance = instance
        self.routes = routes
        self.extracted_node = []
        self.totalCost = 0
        self.update_total_cost()

    def update_total_cost(self):
        self.totalCost = 0
        for route in self.routes:
            self.totalCost += route.cost

    def __str__(self):
        return f'Solution: Total cost = {"%.2f" %self.totalCost}, Routes = \n{self.routes})'

