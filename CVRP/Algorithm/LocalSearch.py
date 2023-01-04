def improve(solution):
    cost = solution.instance.distance_matrix
    for route in solution.routes:
        customers = route.route
        if len(customers) >= 4:
            # Toi uu 1 tuyen xe bang cach xem xet viec dao cac duong cho nhau
            for x in range(1, len(customers) - 3):
                for v in range(x + 1, len(customers) - 2):
                    # Danh gia chi phi truoc va sau khi dao 2 duong
                    delta = cost[customers[x - 1].id][customers[v].id] + cost[customers[x].id][customers[v + 1].id] - cost[customers[x - 1].id][customers[x].id] - cost[customers[v].id][customers[v + 1].id]
                    if delta < -0.01:
                        # Trong truong hop chi phi co giam se doi 2 duong (not 2 khach hang)
                        i = x
                        j = v
                        route.cost += delta
                        while i < j:
                            tmp = customers[i]
                            customers[i] = customers[j]
                            customers[j] = tmp
                            i += 1
                            j -= 1
                        return True
    return False


def local_search(solution):
    """

    :param solution:
    :return: solution duoc cai tien boi local search

    Thuat toan local search (Hill climbing) su dung move 2-opt first improve
    """
    improved = True
    while improved:
        improved = improve(solution)
    return solution
