'''
Author: Karim Q.
Date: 6/1/21
'''
import numpy as np
import random
from PyGCube import Graphics

#* In CubeList: Index0=Front, Index1=Right, Index2=Back, Index3=Left, Index4=Up, Index5=Down

#* Color Names Follow Same Logic: WOB => W is Front, O is Left, B is Up

#* .Cube returns The Full Cube with Complex Color Structure of Each Face while .Faces returns The Cube's Faces with Simple Color Structure

class MakeCube:
    def __init__(self, Cube = None, AutoUpdateCube = True):
        self._SolvedCube = [[["W"]*3]*3, [["R"]*3]*3, [["Y"]*3]*3, [["O"]*3]*3, [["B"]*3]*3, [["G"]*3]*3]
        self.Cube = Cube if Cube else FaceMatch(self._SolvedCube)
        self.Faces = [[[Color[0] for Color in Row] for Row in Face] for Face in self.Cube]
        self.Flat = np.array(self.Faces).flatten().tolist()
        self.Front, self.Right, self.Back, self.Left, self.Up, self.Down = tuple(self.Cube)
        self.AutoUpdate = AutoUpdateCube
        self._CubeGraphic = None
       
    def UpdateCube(self):
        self.Cube = [self.Front, self.Right, self.Back, self.Left, self.Up, self.Down]
        self.Faces = [[[Color[0] for Color in Row] for Row in Face] for Face in self.Cube]
        self.Flat = np.array(self.Faces).flatten().tolist()
        if self._CubeGraphic: self._CubeGraphic._UpdateCubeGraphics()

    def CheckSolved(self):
        CubeTemp = [[[Color[0] for Color in Row] for Row in Face] for Face in self.Cube] 
        return sorted(CubeTemp) == sorted(self._SolvedCube)

    def StartGraphics(self):
        self._CubeGraphic = Graphics(self)
        self._CubeGraphic.Start()

    def _RearrangeCorners(self, Face, Corners):
        CornerArrangements = {1: (0, 0), 2: (0, 2), 3: (2, 0), 4: (2, 2)}

        Attr = getattr(self, Face)
        for Corner in Corners:
            Y, Z = CornerArrangements[Corner]
            Attr[Y][Z] = list(Attr[Y][Z])
            Attr[Y][Z][1], Attr[Y][Z][-1] = Attr[Y][Z][-1], Attr[Y][Z][1]
            Attr[Y][Z] = "".join(Attr[Y][Z])
        setattr(self, Face, Attr)

    def F(self):
        self.Front = np.rot90(self.Front, axes=(1, 0)).tolist()
        self._RearrangeCorners("Front", [1, 2, 3, 4])

        self.Right = np.dstack(self.Right)[0].tolist()
        self.Left = np.dstack(self.Left)[0].tolist()
        R, U, L, D = list(reversed(self.Right[0])), self.Up[2].copy(), list(reversed(self.Left[2])), self.Down[0].copy()
        self.Up[2], self.Right[0], self.Left[2], self.Down[0] = L, U, D, R
        self.Right = np.dstack(self.Right)[0].tolist()
        self.Left = np.dstack(self.Left)[0].tolist()

        self._RearrangeCorners("Right", [1, 3])
        self._RearrangeCorners("Left", [2, 4])
        self._RearrangeCorners("Up", [3, 4])
        self._RearrangeCorners("Down", [1, 2])
        
        if self.AutoUpdate: self.UpdateCube()

    def FPrime(self):
        self.Front = np.rot90(self.Front).tolist()
        self._RearrangeCorners("Front", [1, 2, 3, 4])

        self.Right = np.dstack(self.Right)[0].tolist()
        self.Left = np.dstack(self.Left)[0].tolist()
        R, U, L, D = self.Right[0].copy(), list(reversed(self.Up[2])), self.Left[2].copy(), list(reversed(self.Down[0]))
        self.Up[2], self.Right[0], self.Left[2], self.Down[0] = R, D, U, L
        self.Right = np.dstack(self.Right)[0].tolist()
        self.Left = np.dstack(self.Left)[0].tolist()

        self._RearrangeCorners("Right", [1, 3])
        self._RearrangeCorners("Left", [2, 4])
        self._RearrangeCorners("Up", [3, 4])
        self._RearrangeCorners("Down", [1, 2])

        if self.AutoUpdate: self.UpdateCube()

    def F2(self):
        self.Front = np.rot90(self.Front, k=2).tolist()

        self.Right = np.dstack(self.Right)[0].tolist()
        self.Left = np.dstack(self.Left)[0].tolist()
        R, U, L, D = list(reversed(self.Right[0])), list(reversed(self.Up[2])), list(reversed(self.Left[2])), list(reversed(self.Down[0]))
        self.Up[2], self.Right[0], self.Left[2], self.Down[0] = D, L, R, U
        self.Right = np.dstack(self.Right)[0].tolist()
        self.Left = np.dstack(self.Left)[0].tolist()
        
        if self.AutoUpdate: self.UpdateCube()

    def R(self):
        self.Right = np.rot90(self.Right, axes=(1, 0)).tolist()
        self._RearrangeCorners("Right", [1, 2, 3, 4])

        self.Front = np.dstack(self.Front)[0].tolist()
        self.Back = np.dstack(self.Back)[0].tolist()
        self.Up = np.dstack(self.Up)[0].tolist()
        self.Down = np.dstack(self.Down)[0].tolist()
        D, U, F, B = self.Down[2].copy(), list(reversed(self.Up[2])), self.Front[2].copy(), list(reversed(self.Back[0]))
        self.Front[2], self.Back[0], self.Up[2], self.Down[2] = D, U, F, B
        self.Front = np.dstack(self.Front)[0].tolist()
        self.Back = np.dstack(self.Back)[0].tolist()
        self.Up = np.dstack(self.Up)[0].tolist()
        self.Down = np.dstack(self.Down)[0].tolist()

        if self.AutoUpdate: self.UpdateCube()

    def RPrime(self):
        self.Right = np.rot90(self.Right).tolist()
        self._RearrangeCorners("Right", [1, 2, 3, 4])

        self.Front = np.dstack(self.Front)[0].tolist()
        self.Back = np.dstack(self.Back)[0].tolist()
        self.Up = np.dstack(self.Up)[0].tolist()
        self.Down = np.dstack(self.Down)[0].tolist()
        D, U, F, B = list(reversed(self.Down[2])), self.Up[2].copy(), self.Front[2].copy(), list(reversed(self.Back[0]))
        self.Front[2], self.Back[0], self.Up[2], self.Down[2] = U, D, B, F
        self.Front = np.dstack(self.Front)[0].tolist()
        self.Back = np.dstack(self.Back)[0].tolist()
        self.Up = np.dstack(self.Up)[0].tolist()
        self.Down = np.dstack(self.Down)[0].tolist()

        if self.AutoUpdate: self.UpdateCube()

    def R2(self):
        self.Right = np.rot90(self.Right, k=2).tolist()

        self.Front = np.dstack(self.Front)[0].tolist()
        self.Back = np.dstack(self.Back)[0].tolist()
        self.Up = np.dstack(self.Up)[0].tolist()
        self.Down = np.dstack(self.Down)[0].tolist()
        D, U, F, B = self.Down[2].copy(), self.Up[2].copy(), list(reversed(self.Front[2])), list(reversed(self.Back[0]))
        self.Front[2], self.Back[0], self.Up[2], self.Down[2] = B, F, D, U
        self.Front = np.dstack(self.Front)[0].tolist()
        self.Back = np.dstack(self.Back)[0].tolist()
        self.Up = np.dstack(self.Up)[0].tolist()
        self.Down = np.dstack(self.Down)[0].tolist()

        if self.AutoUpdate: self.UpdateCube()

    def L(self):
        self.Left = np.rot90(self.Left, axes=(1, 0)).tolist()
        self._RearrangeCorners("Left", [1, 2, 3, 4])
        
        self.Front = np.dstack(self.Front)[0].tolist()
        self.Back = np.dstack(self.Back)[0].tolist()
        self.Up = np.dstack(self.Up)[0].tolist()
        self.Down = np.dstack(self.Down)[0].tolist()
        D, U, F, B = list(reversed(self.Down[0])), self.Up[0].copy(), self.Front[0].copy(), list(reversed(self.Back[2]))
        self.Front[0], self.Back[2], self.Up[0], self.Down[0] = U, D, B, F
        self.Front = np.dstack(self.Front)[0].tolist()
        self.Back = np.dstack(self.Back)[0].tolist()
        self.Up = np.dstack(self.Up)[0].tolist()
        self.Down = np.dstack(self.Down)[0].tolist()

        if self.AutoUpdate: self.UpdateCube()

    def LPrime(self):
        self.Left = np.rot90(self.Left).tolist()
        self._RearrangeCorners("Left", [1, 2, 3, 4])

        self.Front = np.dstack(self.Front)[0].tolist()
        self.Back = np.dstack(self.Back)[0].tolist()
        self.Up = np.dstack(self.Up)[0].tolist()
        self.Down = np.dstack(self.Down)[0].tolist()
        D, U, F, B = self.Down[0].copy(), list(reversed(self.Up[0])), self.Front[0].copy(), list(reversed(self.Back[2]))
        self.Front[0], self.Back[2], self.Up[0], self.Down[0] = D, U, F, B
        self.Front = np.dstack(self.Front)[0].tolist()
        self.Back = np.dstack(self.Back)[0].tolist()
        self.Up = np.dstack(self.Up)[0].tolist()
        self.Down = np.dstack(self.Down)[0].tolist()

        if self.AutoUpdate: self.UpdateCube()

    def L2(self):
        self.Left = np.rot90(self.Left, k=2).tolist()
        
        self.Front = np.dstack(self.Front)[0]
        self.Back = np.dstack(self.Back)[0]
        self.Up = np.dstack(self.Up)[0]
        self.Down = np.dstack(self.Down)[0]
        D, U, F, B = self.Down[0].copy(), self.Up[0].copy(), list(reversed(self.Front[0])), list(reversed(self.Back[2]))
        self.Front[0], self.Back[2], self.Up[0], self.Down[0] = B, F, D, U
        self.Front = np.dstack(self.Front)[0].tolist()
        self.Back = np.dstack(self.Back)[0].tolist()
        self.Up = np.dstack(self.Up)[0].tolist()
        self.Down = np.dstack(self.Down)[0].tolist()

        if self.AutoUpdate: self.UpdateCube()

    def B(self):
        self.Back = np.rot90(self.Back, axes=(1, 0)).tolist()
        self._RearrangeCorners("Back", [1, 2, 3, 4])

        self.Right = np.dstack(self.Right)[0].tolist()
        self.Left = np.dstack(self.Left)[0].tolist()
        R, U, L, D = self.Right[2].copy(), list(reversed(self.Up[0])), self.Left[0].copy(), list(reversed(self.Down[2]))
        self.Up[0], self.Right[2], self.Left[0], self.Down[2] = R, D, U, L
        self.Right = np.dstack(self.Right)[0].tolist()
        self.Left = np.dstack(self.Left)[0].tolist()

        self._RearrangeCorners("Right", [2, 4])
        self._RearrangeCorners("Left", [1, 3])
        self._RearrangeCorners("Up", [1, 2])
        self._RearrangeCorners("Down", [3, 4])

        if self.AutoUpdate: self.UpdateCube()

    def BPrime(self):
        self.Back = np.rot90(self.Back).tolist()
        self._RearrangeCorners("Back", [1, 2, 3, 4])

        self.Right = np.dstack(self.Right)[0].tolist()
        self.Left = np.dstack(self.Left)[0].tolist()
        R, U, L, D = list(reversed(self.Right[2])), self.Up[0].copy(), list(reversed(self.Left[0])), self.Down[2].copy()
        self.Up[0], self.Right[2], self.Left[0], self.Down[2] = L, U, D, R
        self.Right = np.dstack(self.Right)[0].tolist()
        self.Left = np.dstack(self.Left)[0].tolist()

        self._RearrangeCorners("Right", [2, 4])
        self._RearrangeCorners("Left", [1, 3])
        self._RearrangeCorners("Up", [1, 2])
        self._RearrangeCorners("Down", [3, 4])

        if self.AutoUpdate: self.UpdateCube()

    def B2(self):
        self.Back = np.rot90(self.Back, k=2).tolist()

        self.Right = np.dstack(self.Right)[0].tolist()
        self.Left = np.dstack(self.Left)[0].tolist()
        R, U, L, D = list(reversed(self.Right[2])), list(reversed(self.Up[0])), list(reversed(self.Left[0])), list(reversed(self.Down[2]))
        self.Up[0], self.Right[2], self.Left[0], self.Down[2] = D, L, R, U
        self.Right = np.dstack(self.Right)[0].tolist()
        self.Left = np.dstack(self.Left)[0].tolist()

        if self.AutoUpdate: self.UpdateCube()
    
    def U(self):
        self.Up = np.rot90(self.Up, axes=(1, 0)).tolist()
        self._RearrangeCorners("Up", [1, 2, 3, 4])

        R, L, F, B = self.Right[0].copy(), self.Left[0].copy(), self.Front[0].copy(), self.Back[0].copy()
        self.Front[0], self.Right[0], self.Back[0], self.Left[0] = R, B, L, F

        if self.AutoUpdate: self.UpdateCube()

    def UPrime(self):
        self.Up = np.rot90(self.Up).tolist()
        self._RearrangeCorners("Up", [1, 2, 3, 4])

        R, L, F, B = self.Right[0].copy(), self.Left[0].copy(), self.Front[0].copy(), self.Back[0].copy()
        self.Front[0], self.Right[0], self.Back[0], self.Left[0] = L, F, R, B

        if self.AutoUpdate: self.UpdateCube()

    def U2(self):
        self.Up = np.rot90(self.Up, k=2).tolist()
        
        R, L, F, B = self.Right[0].copy(), self.Left[0].copy(), self.Front[0].copy(), self.Back[0].copy()
        self.Front[0], self.Right[0], self.Back[0], self.Left[0] = B, L, F, R

        if self.AutoUpdate: self.UpdateCube()

    def D(self):
        self.Down = np.rot90(self.Down, axes=(1, 0)).tolist()
        self._RearrangeCorners("Down", [1, 2, 3, 4])

        R, L, F, B = self.Right[2].copy(), self.Left[2].copy(), self.Front[2].copy(), self.Back[2].copy()
        self.Front[2], self.Right[2], self.Back[2], self.Left[2] = L, F, R, B

        if self.AutoUpdate: self.UpdateCube()

    def DPrime(self):
        self.Down = np.rot90(self.Down).tolist()
        self._RearrangeCorners("Down", [1, 2, 3, 4])

        R, L, F, B = self.Right[2].copy(), self.Left[2].copy(), self.Front[2].copy(), self.Back[2].copy()
        self.Front[2], self.Right[2], self.Back[2], self.Left[2] = R, B, L, F

        if self.AutoUpdate: self.UpdateCube()

    def D2(self):
        self.Down = np.rot90(self.Down, k=2).tolist()

        R, L, F, B = self.Right[2].copy(), self.Left[2].copy(), self.Front[2].copy(), self.Back[2].copy()
        self.Front[2], self.Right[2], self.Back[2], self.Left[2] = B, L, F, R

        if self.AutoUpdate: self.UpdateCube()

    def u(self):
        self.D()
        self.Y()

        if self.AutoUpdate: self.UpdateCube()

    def uPrime(self):
        self.DPrime()
        self.YPrime()

        if self.AutoUpdate: self.UpdateCube()
        
    def r(self):
        self.L()
        self.X()

        if self.AutoUpdate: self.UpdateCube()

    def rPrime(self):
        self.LPrime()
        self.XPrime()

        if self.AutoUpdate: self.UpdateCube()

    def f(self):
        self.B()
        self.Z()

        if self.AutoUpdate: self.UpdateCube()

    def fPrime(self):
        self.BPrime()
        self.ZPrime()

        if self.AutoUpdate: self.UpdateCube()

    def d(self):
        self.U()
        self.YPrime()

        if self.AutoUpdate: self.UpdateCube()

    def dPrime(self):
        self.UPrime()
        self.Y()

        if self.AutoUpdate: self.UpdateCube()

    def l(self):
        self.R()
        self.XPrime()

        if self.AutoUpdate: self.UpdateCube()

    def lPrime(self):
        self.RPrime()
        self.X()

        if self.AutoUpdate: self.UpdateCube()

    def b(self):
        self.F()
        self.ZPrime()

        if self.AutoUpdate: self.UpdateCube()

    def bPrime(self):
        self.FPrime()
        self.Z()

        if self.AutoUpdate: self.UpdateCube()

    def X(self):
        D, F, U, B, R, L = self.Down.copy(), self.Front.copy(), np.rot90(self.Up, k=2).tolist(), np.rot90(self.Back, k=2).tolist(), np.rot90(self.Right, axes=(1, 0)).tolist(), np.rot90(self.Left).tolist()
        self.Front, self.Up, self.Back, self.Down, self.Right, self.Left = D, F, U, B, R, L

        self._RearrangeCorners("Right", [1, 2, 3, 4])
        self._RearrangeCorners("Left", [1, 2, 3, 4])

        if self.AutoUpdate: self.UpdateCube()

    def XPrime(self):
        D, F, U, B, R, L = np.rot90(self.Down.copy(), k=2).tolist(), self.Front.copy(), self.Up.copy(), np.rot90(self.Back, k=2).tolist(), np.rot90(self.Right).tolist(), np.rot90(self.Left, axes=(1, 0)).tolist()
        self.Front, self.Up, self.Back, self.Down, self.Right, self.Left = U, B, D, F, R, L

        self._RearrangeCorners("Right", [1, 2, 3, 4])
        self._RearrangeCorners("Left", [1, 2, 3, 4])
        
        if self.AutoUpdate: self.UpdateCube()

    def Y(self):
        R, F, L, B, U, D = self.Right.copy(), self.Front.copy(), self.Left.copy(), self.Back.copy(), np.rot90(self.Up, axes=(1, 0)).tolist(), np.rot90(self.Down).tolist()
        self.Front, self.Up, self.Back, self.Down, self.Right, self.Left = R, U, L, D, B, F
        
        self._RearrangeCorners("Up", [1, 2, 3, 4])
        self._RearrangeCorners("Down", [1, 2, 3, 4])

        if self.AutoUpdate: self.UpdateCube()

    def YPrime(self):
        R, F, L, B, U, D = self.Right.copy(), self.Front.copy(), self.Left.copy(), self.Back.copy(), np.rot90(self.Up).tolist(), np.rot90(self.Down, axes=(1, 0)).tolist()
        self.Front, self.Up, self.Back, self.Down, self.Right, self.Left = L, U, R, D, F, B

        self._RearrangeCorners("Up", [1, 2, 3, 4])
        self._RearrangeCorners("Down", [1, 2, 3, 4])
        
        if self.AutoUpdate: self.UpdateCube()

    def Z(self):
        R, U, L, D, F, B = np.rot90(self.Right, axes=(1, 0)).tolist(), np.rot90(self.Up, axes=(1, 0)).tolist(), np.rot90(self.Left, axes=(1, 0)).tolist(), np.rot90(self.Down, axes=(1, 0)).tolist(), np.rot90(self.Front, axes=(1, 0)).tolist(), np.rot90(self.Back).tolist()
        self.Front, self.Up, self.Back, self.Down, self.Right, self.Left = F, L, B, R, U, D
        
        self._RearrangeCorners("Front", [1, 2, 3, 4])
        self._RearrangeCorners("Back", [1, 2, 3, 4])
        self._RearrangeCorners("Right", [1, 2, 3, 4])
        self._RearrangeCorners("Left", [1, 2, 3, 4])
        self._RearrangeCorners("Up", [1, 2, 3, 4])
        self._RearrangeCorners("Down", [1, 2, 3, 4])

        if self.AutoUpdate: self.UpdateCube()

    def ZPrime(self):
        R, U, L, D, F, B = np.rot90(self.Right).tolist(), np.rot90(self.Up).tolist(), np.rot90(self.Left).tolist(), np.rot90(self.Down).tolist(), np.rot90(self.Front).tolist(), np.rot90(self.Back, axes=(1, 0)).tolist()
        self.Front, self.Up, self.Back, self.Down, self.Right, self.Left = F, R, B, L, D, U
        
        self._RearrangeCorners("Front", [1, 2, 3, 4])
        self._RearrangeCorners("Back", [1, 2, 3, 4])
        self._RearrangeCorners("Right", [1, 2, 3, 4])
        self._RearrangeCorners("Up", [1, 2, 3, 4])
        self._RearrangeCorners("Down", [1, 2, 3, 4])
        self._RearrangeCorners("Left", [1, 2, 3, 4])

        if self.AutoUpdate: self.UpdateCube()

    def M(self):
        self.R()
        self.LPrime()
        self.XPrime()

        if self.AutoUpdate: self.UpdateCube()
    
    def MPrime(self):
        self.RPrime()
        self.L()
        self.X()

        if self.AutoUpdate: self.UpdateCube()
    
    def E(self):
        self.U()
        self.DPrime()
        self.YPrime()

        if self.AutoUpdate: self.UpdateCube()
    
    def EPrime(self):
        self.UPrime()
        self.D()
        self.Y()

        if self.AutoUpdate: self.UpdateCube()

    def S(self):
        self.FPrime()
        self.B()
        self.Z()

        if self.AutoUpdate: self.UpdateCube()
    
    def SPrime(self):
        self.F()
        self.BPrime()
        self.ZPrime()

        if self.AutoUpdate: self.UpdateCube()

    def Shuffle(self):
        Moves = ["SPrime", "S", "EPrime", "E", "MPrime", "M", "ZPrime", "Z", "YPrime", "Y", "XPrime", 
                 "X", "bPrime", "b", "lPrime", "l", "dPrime", "d", "fPrime", "f", "rPrime", "r", "uPrime", 
                 "u", "D2", "DPrime", "D", "U2", "UPrime", "U", "B2", "BPrime", "B", "L2", "LPrime", 
                 "L", "R2", "RPrime", "R", "F2", "FPrime", "F"]
        ShufflingMoves = random.choices(Moves, k=random.randint(20, 30))
        for Move in ShufflingMoves: getattr(self, Move)()

def FaceMatch(Faces):
    Accordances = {(0, 0, 0): [(3, 0, 2), (4, 2, 0)], (0, 0, 1): [(4, 2, 1)], (0, 0, 2): [(1, 0, 0), (4, 2, 2)],
                   (0, 1, 0): [(3, 1, 2)], (0, 1, 2): [(1, 1, 0)], 
                   (0, 2, 0): [(3, 2, 2), (5, 0, 0)], (0, 2, 1): [(5, 0, 1)], (0, 2, 2): [(1, 2, 0), (5, 0, 2)],
               
                   (1, 0, 0): [(0, 0, 2), (4, 2, 2)], (1, 0, 1): [(4, 1, 2)], (1, 0, 2): [(2, 0, 0), (4, 0, 2)],
                   (1, 1, 0): [(0, 1, 2)], (1, 1, 2): [(2, 1, 0)], 
                   (1, 2, 0): [(0, 2, 2), (5, 0, 2)], (1, 2, 1): [(5, 1, 2)], (1, 2, 2): [(2, 2, 0), (5, 2, 2)],
               
                   (2, 0, 0): [(1, 0, 2), (4, 0, 2)], (2, 0, 1): [(4, 0, 1)], (2, 0, 2): [(3, 0, 0), (4, 0, 0)],
                   (2, 1, 0): [(1, 1, 2)], (2, 1, 2): [(3, 1, 0)], 
                   (2, 2, 0): [(1, 2, 2), (5, 2, 2)], (2, 2, 1): [(5, 2, 1)], (2, 2, 2): [(3, 2, 0), (5, 2, 0)],
               
                   (3, 0, 0): [(2, 0, 2), (4, 0, 0)], (3, 0, 1): [(4, 1, 0)], (3, 0, 2): [(0, 0, 0), (4, 2, 0)],
                   (3, 1, 0): [(2, 1, 2)], (3, 1, 2): [(0, 1, 0)], 
                   (3, 2, 0): [(2, 2, 2), (5, 2, 0)], (3, 2, 1): [(5, 1, 0)], (3, 2, 2): [(0, 2, 0), (5, 0, 0)],
               
                   (4, 0, 0): [(3, 0, 0), (2, 0, 2)], (4, 0, 1): [(2, 0, 1)], (4, 0, 2): [(1, 0, 2), (2, 0, 0)],
                   (4, 1, 0): [(3, 0, 1)], (4, 1, 2): [(1, 0, 1)], 
                   (4, 2, 0): [(3, 0, 2), (0, 0, 0)], (4, 2, 1): [(0, 0, 1)], (4, 2, 2): [(1, 0, 0), (0, 0, 2)],
               
                   (5, 0, 0): [(3, 2, 2), (0, 2, 0)], (5, 0, 1): [(0, 2, 1)], (5, 0, 2): [(1, 2, 0), (0, 2, 2)],
                   (5, 1, 0): [(3, 2, 1)], (5, 1, 2): [(1, 2, 1)], 
                   (5, 2, 0): [(3, 2, 0), (2, 2, 2)], (5, 2, 1): [(2, 2, 1)], (5, 2, 2): [(1, 2, 2), (2, 2, 0)]}

    ArangedFaces = []
    for Fn, Face in enumerate(Faces):
        ArangedFaces.append([])
        for Rn, Row in enumerate(Face):
            ArangedFaces[-1].append([])
            for Cn, Color in enumerate(Row):
                TempC = "".join(Faces[a][b][c] for a, b, c in Accordances[(Fn, Rn, Cn)]) if (Rn, Cn) != (1, 1) else ""
                ArangedFaces[-1][-1].append(Color+TempC)
    return ArangedFaces

Cube1 = MakeCube() # Clean Cube

Faces = [[["R", "W", "O"], ["B", "O", "O"], ["B", "R", "O"]], # Front Face
         [["Y", "W", "R"], ["Y", "W", "R"], ["Y", "W", "G"]], # Right Face
         [["B", "Y", "G"], ["B", "R", "G"], ["R", "O", "G"]], # Back Face
         [["W", "Y", "B"], ["W", "Y", "O"], ["W", "Y", "O"]], # Left Face
         [["O", "R", "W"], ["G", "B", "O"], ["Y", "B", "G"]], # Top Face
         [["W", "G", "B"], ["B", "G", "R"], ["R", "G", "Y"]]] # Bottom Face

Cube2 = MakeCube(FaceMatch(Faces)) # Use Faces as Cube

Cube1.StartGraphics() # Run The Graphics
