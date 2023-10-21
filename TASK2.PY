class Triangle:
    def __init__(self):
        self.points = []

    def add_point(self, x, y):
        self.points.append((x, y))

    def perimeter(self):
        if len(self.points) != 3:
            return 0
        return sum(((self.points[i][0] - self.points[(i + 1) % 3][0]) ** 2 + (self.points[i][1] - self.points[(i + 1) % 3][1]) ** 2) ** 0.5 for i in range(3))

    def is_equal(self, other):
        return self.points == other.points

    def __eq__(self, other):
        return self.is_equal(other)

t1 = Triangle()
t1.add_point(0, 0)
t1.add_point(0, 3)
t1.add_point(4, 0)

perimeter_t1 = t1.perimeter()
print("Perimeter of t1:", perimeter_t1)

t2 = Triangle()
t2.add_point(1, 2)
t2.add_point(2, 1)
t2.add_point(1, 5)

perimeter_t2 = t2.perimeter()
print("Perimeter of t2:", perimeter_t2)

print("t1 and t2 are equal:", t1.is_equal(t2))

t3 = Triangle()
t3.add_point(1, 2)
t3.add_point(2, 1)
t3.add_point(1, 5)

print("t1 == t3:", t1 == t3)
print("t1.is_equal(t3):", t1.is_equal(t3))
print("t3.is_equal(t1):", t3.is_equal(t1))

