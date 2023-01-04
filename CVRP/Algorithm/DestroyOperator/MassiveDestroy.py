from random import choice
from CVRP.Instances.Route import Route


def massive_destroy(solution, to_remove=None, d=None):
    """
    :param solution: Nghiem can duoc pha
    :return: parital solution

    Ham nay thuc hien xoa tat ca khach hang tu 2 route ngau nhien
    """
    route1 = choice(solution.routes)
    solution.routes.remove(route1)
    route2 = choice(solution.routes)
    solution.routes.remove(route2)

    customers = route1.route + route2.route
    for customer in customers:
        if customer.id != 0:
            solution.extracted_node.append(customer)

    # Bo sung 2 route moi sau khi da xoa 2 route cu di
    a = Route(solution.instance)
    a.finish_route()
    b = Route(solution.instance)
    b.finish_route()
    solution.routes.append(a)
    solution.routes.append(b)

    return solution
