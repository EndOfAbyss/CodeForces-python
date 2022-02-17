from decimal import DivisionByZero
import math

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __add__(self, v):
        return Point(self.x + v.x, self.y + v.y, self.z + v.z)
    
    def __sub__(self, v):
        return Point(self.x - v.x, self.y - v.y, self.z - v.z)
    
class Vector:
    def __init__(self, components=None, points=None):
        self.x = None
        self.y = None
        self.z = None
        
        if components:
            self.x = components[0]
            self.y = components[1]
            self.z = components[2]
        else:
            self.x = points[1].x - points[0].x
            self.y = points[1].y - points[0].y
            self.z = points[1].z - points[0].z
    
    def __add__(self, v):
        return Vector(components=[self.x + v.x, self.y + v.y, self.z + v.z])
    
    def __mul__(self, k):
        return Vector(components=[self.x * k, self.y * k, self.z * k])
    
    def __truediv__(self, k):
        try:
            return Vector(components=[self.x / k, self.y / k, self.z / k])
        except DivisionByZero:
            print("División por cero")
    
    def orthogonal(self):
        return Vector(components=[-self.y, self.x, 0])
    
    def length(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def vector_unitary(self):
        tam = self.length()

        return Vector(components=[self.x / tam, self.y / tam, self.z / tam])

class Line:
    def __init__(self, p: Point, v: Vector) -> None:
        self.p = p
        self.v = v
    
    def __str__(self) -> str:
        return f"({self.p.x}, {self.p.y}) + t({self.v.x}, {self.v.y})"

class Circle:
    def __init__(self, p: Point, r):
        self.center = p
        self.r = r
    
    def __str__(self) -> str:
        return f"{self.center.__str__()} Radio: {self.r}"

def solve_ecuation_cuadratic(a, b, c):
    discriminant = (b ** 2 - 4 * a * c) ** 0.5
    return (-b + discriminant) / (2 * a), (-b - discriminant) / (2 * a)

def cross_product(v1: Vector, v2: Vector):
    return Vector(components=[v1.y*v2.z-v1.z*v2.y, v1.z*v2.x-v1.x*v2.z, v1.x*v2.y-v1.y*v2.x])

def distance_between_two_points(p1: Point, p2: Point):
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

def distance_point_to_line(point: Point, line: Line):
    return cross_product(line.v, Vector(points=[line.p, point])).length() / line.v.length()

def midpoint(p1: Point, p2: Point):
    return Point((p1.x + p2.x) / 2, (p1.y + p2.y) / 2, (p1.z + p2.z) / 2)

def intersection_of_two_lines(l1: Line, l2: Line):
    return l1.p + l1.v * ((l2.p.x - l1.p.x) * l2.v.y + l2.v.x * (l1.p.y - l2.p.y)) / (l2.v.y * l1.v.x - l2.v.x * l1.v.y)

def intersection_line_circle(l: Line, c: Circle):
    a = l.p.x - c.center.x
    b = l.p.y - c.center.y

    A = l.v.x ** 2 + l.v.y ** 2
    B = 2 * a * l.v.x + 2 * b * l.v.y
    C = a ** 2 + b ** 2 - c.r ** 2

    s1, s2 = solve_ecuation_cuadratic(A, B, C)
    
    p1 = l.p + l.v * s1
    p2 = l.p + l.v * s2

    return p1, p2

def print_point_result(p):
    p_x_str = str(round(p.x, 5))
    p_y_str = str(round(p.y, 5))

    p_x_part_int, p_x_part_dec = p_x_str.split('.')
    p_x_part_dec = (p_x_part_dec + "00000")[:5]

    p_y_part_int, p_y_part_dec = p_y_str.split('.')
    p_y_part_dec = (p_y_part_dec + "00000")[:5]

    final_x_str = p_x_part_int + "." + p_x_part_dec
    final_y_str = p_y_part_int + "." + p_y_part_dec

    print(final_x_str, final_y_str)

ax, ay, ra = list(map(int, input().split()))
bx, by, rb = list(map(int, input().split()))
cx, cy, rc = list(map(int, input().split()))

c1 = Circle(Point(ax, ay, 0), ra)
c2 = Circle(Point(bx, by, 0), rb)
c3 = Circle(Point(cx, cy, 0), rc)

p_result_1 = None
p_result_2 = None

if c1.r == c2.r and c1.r == c3.r:
    m1 = midpoint(c1.center, c2.center)
    m2 = midpoint(c1.center, c3.center)

    l1 = Line(m1, Vector(points=[c1.center, c2.center]).orthogonal())
    l2 = Line(m2, Vector(points=[c1.center, c3.center]).orthogonal())

    p_result_1 = intersection_of_two_lines(l1, l2)
    p_result_2 = intersection_of_two_lines(l1, l2)
elif c1.r == c2.r:
    t = midpoint(c1.center, c2.center)
    l = Line(t, Vector(points=[t, c2.center]).orthogonal())

    m = c1.center + Vector(points=[c1.center, c3.center]) * c1.r / (c1.r + c3.r)
    n = c1.center + Vector(points=[c1.center, c3.center]) * c1.r / (c1.r - c3.r)
    q = midpoint(m, n)
    c = Circle(q, distance_between_two_points(q, m))
    
    if distance_point_to_line(c.center, l) <= c.r:
        p_result_1, p_result_2 = intersection_line_circle(l, c)
    else:
        p_result_1 = None
        p_result_2 = None
elif c1.r == c3.r:
    t = midpoint(c1.center, c3.center)
    l = Line(t, Vector(points=[t, c3.center]).orthogonal())

    m = c1.center + Vector(points=[c1.center, c2.center]) * c1.r / (c1.r + c2.r)
    n = c1.center + Vector(points=[c1.center, c2.center]) * c1.r / (c1.r - c2.r)
    q = midpoint(m, n)
    c = Circle(q, distance_between_two_points(q, m))
    
    if distance_point_to_line(c.center, l) <= c.r:
        p_result_1, p_result_2 = intersection_line_circle(l, c)
    else:
        p_result_1 = None
        p_result_2 = None
elif c2.r == c3.r:
    t = midpoint(c2.center, c3.center)
    l = Line(t, Vector(points=[t, c3.center]).orthogonal())

    m = c1.center + Vector(points=[c1.center, c3.center]) * c1.r / (c1.r + c3.r)
    n = c1.center + Vector(points=[c1.center, c3.center]) * c1.r / (c1.r - c3.r)
    q = midpoint(m, n)
    c = Circle(q, distance_between_two_points(q, m))
    
    if distance_point_to_line(c.center, l) <= c.r:
        p_result_1, p_result_2 = intersection_line_circle(l, c)
    else:
        p_result_1 = None
        p_result_2 = None
else:
    m1 = c1.center + Vector(points=[c1.center, c2.center]) * c1.r / (c1.r + c2.r)
    n1 = c1.center + Vector(points=[c1.center, c2.center]) * c1.r / (c1.r - c2.r)
    q1 = midpoint(m1, n1)

    m2 = c1.center + Vector(points=[c1.center, c3.center]) * c1.r / (c1.r + c3.r)
    n2 = c1.center + Vector(points=[c1.center, c3.center]) * c1.r / (c1.r - c3.r)
    q2 = midpoint(m2, n2)

    c4 = Circle(q1, distance_between_two_points(q1, m1))
    c5 = Circle(q2, distance_between_two_points(q2, m2))

    distance_c4_c5 = distance_between_two_points(c4.center, c5.center)

    if distance_c4_c5 <= (c4.r + c5.r) and distance_c4_c5 >= abs(c4.r - c5.r):
        vector_c4c5 = Vector(points=[c4.center, c5.center])
        vector_c4c5_orthogonal = vector_c4c5.orthogonal()

        distance_c4_c5 = distance_between_two_points(c4.center, c5.center)

        theta = math.acos((c4.r ** 2 + distance_c4_c5 ** 2 - c5.r ** 2) / (2 * distance_c4_c5 * c4.r))

        point_m = c4.center + vector_c4c5.vector_unitary() * c4.r * math.cos(theta)

        p_result_1 = point_m + vector_c4c5_orthogonal.vector_unitary() * c4.r * math.sin(theta)
        p_result_2 = point_m - vector_c4c5_orthogonal.vector_unitary() * c4.r * math.sin(theta)

if p_result_1 and p_result_2:
    d1 = distance_between_two_points(c1.center, p_result_1)
    d2 = distance_between_two_points(c1.center, p_result_2)

    if d1 < d2:
        print_point_result(p_result_1)
    else:
        print_point_result(p_result_2)
    


