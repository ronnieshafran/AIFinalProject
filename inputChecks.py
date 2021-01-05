from dataStructures import DataInput, AlgorithmResult


def check_input(data: DataInput):
    root = data.start_point
    goal = data.end_point

    if root.x == goal.x and root.y == goal.y:
        return AlgorithmResult("", 0, 0, 0, True, 0, 0, 0, 0, 0, 0)

    elif root.x < 0 or root.y < 0 or goal.x < 0 or goal.y < 0:
        return None, 1

    elif (root.x > data.matrix_size) or (root.y > data.matrix_size) or (goal.x > data.matrix_size)\
            or (goal.y > data.matrix_size):
        return None, 2

    else:
        return None, 0
