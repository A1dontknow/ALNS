from random import choice, randint


def random_repair(solution):
    for node in solution.extracted_node:
        insert_route = []
        for route in solution.routes:
            if route.can_insert(node):
                insert_route.append(route)

        # Nghiem co mot ti le thap khong sua duoc nen se phai xu ly neu phat sinh
        if len(insert_route) == 0:
            return
        else:
            route = choice(insert_route)
            position = randint(0, len(route.route) - 2)
            route.insert(node, position)

    solution.extracted_node = []
    solution.update_total_cost()
    return solution
