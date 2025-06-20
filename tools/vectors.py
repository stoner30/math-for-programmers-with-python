from math import sqrt, sin, cos, acos, atan2


def add(*vectors):
    return tuple(map(sum, zip(*vectors)))


def subtract(v1, v2):
    return tuple(v1 - v2 for (v1, v2) in zip(v1, v2))


def length(v):
    return sqrt(sum(coord ** 2 for coord in v))


def dot(u, v):
    return sum([coord1 * coord2 for coord1, coord2 in zip(u, v)])


def distance(v1, v2):
    return length(subtract(v1, v2))


def perimeter(vectors):
    distances = [distance(vectors[i], vectors[(i + 1) % len(vectors)]) for i in range(0, len(vectors))]
    return sum(distances)


def scale(scalar, v):
    return tuple(scalar * coord for coord in v)


def to_cartesian(polar_vector):
    l, angle = polar_vector[0], polar_vector[1]
    return l * cos(angle), l * sin(angle)


def rotate(angle, vectors):
    polars = [to_polar(v) for v in vectors]
    return [to_cartesian((l, a + angle)) for l, a in polars]


def translate(translation, vectors):
    return [add(translation, v) for v in vectors]


def to_polar(vector):
    x, y = vector[0], vector[1]
    angle = atan2(y, x)
    return length(vector), angle


def angle_between(v1, v2):
    return acos(dot(v1, v2) / (length(v1) * length(v2)))


def cross(u, v):
    ux, uy, uz = u
    vx, vy, vz = v
    return uy * vz - uz * vy, uz * vx - ux * vz, ux * vy - uy * vx


def component(v, direction):
    return dot(v, direction) / length(direction)


def unit(v):
    return scale(1. / length(v), v)
