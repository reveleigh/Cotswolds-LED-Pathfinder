class Town:
    def __init__(self, name, x, y, leds):
        self.name = name
        self.x = x
        self.y = y
        self.leds = leds
        self.neighbours = []  # List of neighboring Town objects
        self.previous = None  # Previous town in the shortest path
        self._distance = 9999  # Initial distance from the starting town
        self._visited = False  # Whether the town has been visited

    def get_previous(self):
        """Returns the previous town in the shortest path."""
        return self.previous

    def set_previous(self, town):
        """Sets the previous town in the shortest path."""
        self.previous = town

    @property
    def distance(self):
        """Returns the current distance from the starting town."""
        return self._distance

    @distance.setter
    def distance(self, value):
        """Sets the distance from the starting town."""
        self._distance = value

    @property
    def visited(self):
        """Returns True if the town has been visited, False otherwise."""
        return self._visited

    @visited.setter
    def visited(self, value):
        """Sets the visited status of the town."""
        self._visited = value


    def __repr__(self):
        """Returns a string representation of the Town object."""
        return f"Town({self.name})"
        


# Create all Town instances:
A = Town("Faringdon", 1020, 180, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
B = Town("Upper Inglesham", 690, 120, [12, 13])
C = Town("Lechlade", 800, 265, [10, 11])
D = Town("Kingston Bagpuize", 1160, 370, [53, 54, 55])
E = Town("Carterton", 995, 460, [50, 51, 52])
F = Town("Cricklade", 545, 195, [14, 15, 16])
G = Town("Fairford", 640, 340, [17, 18])
H = Town("Oxford", 1235, 500, [56])
I = Town("Witney", 1190, 675, [57, 58, 59, 60])
J = Town("Burford", 760, 600, [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49])
K = Town("Cirencester", 390, 305, [19, 20, 21, 22, 23])
L = Town("Kemble", 180, 175, [24, 25, 26])
M = Town("Stroud", 105, 450, [27, 28,29, 30, 31, 32])
N = Town("Straton", 260, 500, [33])
O = Town("Bibury", 460, 580, [36, 37, 38])
P = Town("Charlbury", 950, 815, [66, 67, 68])
Q = Town("Woodstock", 1145, 950, [63, 64, 65])
R = Town("Tackley", 1250, 1065, [61, 62])
S = Town("Duntisbourne Abbots", 290, 620, [34, 35])
T = Town("Gloucester", 95, 805, [129, 130, 131])
U = Town("Brockworth", 380, 890, [132, 133, 134, 135, 136, 137, 138, 139, 140])
V = Town("Northleach", 550, 800, [141, 142, 143, 144])
W = Town("Stow-on-the-Wold", 700, 1000, [69, 70, 71])
X = Town("Chipping Norton", 915, 1095, [72, 73, 74])
Y = Town("Middle Barton", 1090, 1160, [75, 76])
Z = Town("Steeple Aston", 1205, 1250, [77, 78])
AA = Town("Cheltenham", 80, 980, [127, 128])
AB = Town("Bishops Cleeve", 280, 1085, [124, 125, 126])
AC = Town("Broadway", 530, 1220, [116, 117, 118, 119, 120, 121, 122, 123])
AD = Town("Moreton-in-Marsh", 870, 1260, [112, 113, 114, 115])
AE = Town("Shipston-on-Stour", 1140, 1385, [79, 80, 81])
AF = Town("Tewkesbury", 100, 1245, [99, 100, 101, 102, 103])
AG = Town("Winchcombe", 295, 1330, [104, 105])
AH = Town("Honeybourne", 540, 1440, [106])
AI = Town("Chipping Camden", 870, 1380, [107, 108, 109, 110, 111])
AJ = Town("Stratford-upon-Avon", 1180, 1580, [82, 83, 84])
AK = Town("Welford-on-Avon", 900, 1530, [85, 86, 87])
AL = Town("Bidford-on-Avon", 705, 1550, [88, 89, 90])
AM = Town("Harington", 580, 1615, [91])
AN = Town("Evesham", 420, 1530, [92, 93, 94])
AO = Town("Pershore", 175, 1550, [95, 96, 97, 98])


# Now, add the neighbour objects:
A.neighbours = [B, C, D]
B.neighbours = [F, C, A]
C.neighbours = [A, B, G, E]
D.neighbours = [A, E, H]
E.neighbours = [D, C, I, J]
F.neighbours = [B, G, K]
G.neighbours = [F, K, J, C]
H.neighbours = [D, I]
I.neighbours = [H, E, P, Q, R]
J.neighbours = [E, G, O, V, W, P]
K.neighbours = [F, L, M, N, O, G]
L.neighbours = [M, K]
M.neighbours = [L, T, S, N]
N.neighbours = [K, M, S]
O.neighbours = [K, S, V, J]
P.neighbours = [J, W, X, Q, I]
Q.neighbours = [P, X, Y, R, I]
R.neighbours = [Q, Z, I]
S.neighbours = [N, M, U, O]  
T.neighbours = [M, AA, U]
U.neighbours = [S, T, AB, AC, W, V]
V.neighbours = [O, U, W, J]
W.neighbours = [J, V, U, AC, X, P]
X.neighbours = [P, W, AD, Y]
Y.neighbours = [Q, X, AE, Z]
Z.neighbours = [R, Y, AE]
AA.neighbours = [T, AF, AB]
AB.neighbours = [U, AA, AF, AG, AC]
AC.neighbours = [U, AB, AG, AH, AI, AD, W]
AD.neighbours = [X, AC, AI, AE]
AE.neighbours = [Z, Y, AD, AI, AK, AJ]
AF.neighbours = [AA, AO, AG, AB]
AG.neighbours = [AB, AF, AN, AC]
AH.neighbours = [AC, AN, AL, AI]
AI.neighbours = [AD, AC, AH, AL, AK, AE]
AJ.neighbours = [AE, AK]
AK.neighbours = [AI, AL, AJ, AE]
AL.neighbours = [AI, AH, AM, AK]
AM.neighbours = [AN, AL]
AN.neighbours = [AG, AO, AM, AH]
AO.neighbours = [AF, AN]

# Create a list of all towns in the Cotswolds
towns = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, 
                  AA, AB, AC, AD, AE, AF, AG, AH, AI, AJ, AK, AL, AM, AN, AO]
