class MarblingDrop:
    def __init__(self, x, y, col, size):
        self.x = x
        self.y = y
        self.color = col
        self.size = size
        self.boundary_points = []
        self.generate_boundary(400) # 400 equidistant points on the boundary of the circle to begin with

    def generate_boundary(self, num_points):
        self.boundary_points = []
        for i in range(num_points):
            angle = TWO_PI * i / num_points
            px = self.x + cos(angle) * self.size / 2
            py = self.y + sin(angle) * self.size / 2
            self.boundary_points.append(PVector(px, py))

    def display(self):
        noStroke()
        fill(self.color[0], self.color[1], self.color[2], 180)
        beginShape()
        for p in self.boundary_points:
            vertex(p.x, p.y)
        endShape(CLOSE)
