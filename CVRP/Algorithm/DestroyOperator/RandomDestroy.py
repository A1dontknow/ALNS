from random import choice, randint


def random_destroy(solution, to_remove, d=None):
    """
    :param solution: (Solution) the solution to be destroyed
    :param to_remove: (int) the numbers of customers will be removed
    :return: partial solution

    Ham nay duoc xoa ngau nhien customer tu 1 route bat ki
    """
    removed = 0
    while removed < to_remove:
        random_route = choice(solution.routes)
        # Neu route co customer ngoai depot ra
        if len(random_route.route) > 2:
            random_customer = random_route.route[randint(1, len(random_route.route) - 2)]
            random_route.erase(random_customer.id)
            solution.extracted_node.append(random_customer)
            removed += 1

    return solution
