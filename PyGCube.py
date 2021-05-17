from ursina import *

Colors = {"W":color.white, "R":color.red, "Y":color.yellow, "O":color.orange, "B":color.blue, "G":color.green}

class Graphics:
    def __init__(self, Cube):
        self._Win = Ursina()
        self._Cube = Cube
        self._Flat = Cube.Flat
        self._SetupCube()
        self._SetupArrows()
        self.Cam = EditorCamera()

    def Start(self):
        self._Win.run()

    def Stop(self):
        self._Win.quit()

    def _SendOrientedMove(self, Move):
        # self._ReOrient()
        getattr(self._Cube, Move)()

    def _UpdateCubeGraphics(self):
        for i in range(9*6):
            self._Flat[i].color = Colors[self._Cube.Flat[i]]

    # def _ReOrient(self):
    #     print("="*23)

    def _MakeMove(self, Position=(0,0,0), Color=color.black, Rot=(0, 0, 0), Ext="arrow_down"):
        return Draggable(parent = camera.ui, model="cube", color = Color, position = Position, texture = Ext, scale = Vec2(.07, .07), rotation = Rot, require_key = "left shift")

    def _MakePiece(self, Position=(0,0,0), Color=color.black, Rotation=(0,0,0)):
        return Entity(parent = scene, model="quad", color = Color, position = Position, texture = "white_cube", rotation = Rotation)

    def _SetupCube(self):
        FaceColor = iter(self._Flat)
        self._Front = [self._MakePiece((x-1, y-1, -1.5), Colors[next(FaceColor)]) for y in reversed(range(3)) for x in range(3)]     
        self._Right = [self._MakePiece((1.5, y-1, z-1), Colors[next(FaceColor)], (0, -90, 0)) for y in reversed(range(3)) for z in range(3)]
        self._Back = [self._MakePiece((x-1, y-1, 1.5), Colors[next(FaceColor)], (180, 0, 0)) for y in reversed(range(3)) for x in reversed(range(3))]
        self._Left = [self._MakePiece((-1.5, y-1, z-1), Colors[next(FaceColor)], (0, 90, 0)) for y in reversed(range(3)) for z in reversed(range(3))]
        self._Up = [self._MakePiece((x-1, 1.5, z-1), Colors[next(FaceColor)], (90, 0, 0)) for z in reversed(range(3)) for x in range(3)]
        self._Down = [self._MakePiece((x-1, -1.5, z-1), Colors[next(FaceColor)], (-90, 0, 0)) for z in range(3) for x in range(3)]
        self._Flat = self._Front + self._Right + self._Back + self._Left + self._Up + self._Down
        
    def _SetupArrows(self):
        RMove = self._MakeMove((self._Front[2].screen_position[0], self._Front[2].screen_position[1]+.1, 0), color.red, (180, 0, 0))
        RMove.tooltip = Tooltip("R", scale = Vec2(0.7, 0.7))
        RMove.on_click = lambda: self._SendOrientedMove("R")()
        MMove = self._MakeMove((self._Front[1].screen_position[0], self._Front[1].screen_position[1]+.1, 0), color.red, (180, 0, 0))
        MMove.tooltip = Tooltip("M", scale = Vec2(0.7, 0.7))
        MMove.on_click = lambda: self._SendOrientedMove("M")()
        LMove = self._MakeMove((self._Front[0].screen_position[0], self._Front[0].screen_position[1]+.1, 0), color.red, (180, 0, 0))
        LMove.tooltip = Tooltip("L", scale = Vec2(0.7, 0.7))
        LMove.on_click = lambda: self._SendOrientedMove("L")()

        RPMove = self._MakeMove((self._Front[8].screen_position[0], self._Front[8].screen_position[1]-.1, 0), color.red, (0, 0, 0))
        RPMove.tooltip = Tooltip("R'", scale = Vec2(0.7, 0.7))
        RPMove.on_click = lambda: self._SendOrientedMove("RPrime")()
        MPMove = self._MakeMove((self._Front[7].screen_position[0], self._Front[7].screen_position[1]-.1, 0), color.red, (0, 0, 0))
        MPMove.tooltip = Tooltip("M'", scale = Vec2(0.7, 0.7))
        MPMove.on_click = lambda: self._SendOrientedMove("MPrime")()
        LPMove = self._MakeMove((self._Front[6].screen_position[0], self._Front[6].screen_position[1]-.1, 0), color.red, (0, 0, 0))
        LPMove.tooltip = Tooltip("L'", scale = Vec2(0.7, 0.7))
        LPMove.on_click = lambda: self._SendOrientedMove("LPrime")()

        UMove = self._MakeMove((self._Front[0].screen_position[0]-.1, self._Front[0].screen_position[1], 0), color.red, (0, 0, 90))
        UMove.tooltip = Tooltip("U", scale = Vec2(0.7, 0.7))
        UMove.on_click = lambda: self._SendOrientedMove("U")()
        EMove = self._MakeMove((self._Front[3].screen_position[0]-.1, self._Front[3].screen_position[1], 0), color.red, (0, 0, 90))
        EMove.tooltip = Tooltip("E", scale = Vec2(0.7, 0.7))
        EMove.on_click = lambda: self._SendOrientedMove("E")()
        DMove = self._MakeMove((self._Front[6].screen_position[0]-.1, self._Front[6].screen_position[1], 0), color.red, (0, 0, 90))
        DMove.tooltip = Tooltip("D", scale = Vec2(0.7, 0.7))
        DMove.on_click = lambda: self._SendOrientedMove("D")()

        UPMove = self._MakeMove((self._Front[2].screen_position[0]+.1, self._Front[2].screen_position[1], 0), color.red, (0, 0, -90))
        UPMove.tooltip = Tooltip("U'", scale = Vec2(0.7, 0.7))
        UPMove.on_click = lambda: self._SendOrientedMove("UPrime")()
        EPMove = self._MakeMove((self._Front[5].screen_position[0]+.1, self._Front[5].screen_position[1], 0), color.red, (0, 0, -90))
        EPMove.tooltip = Tooltip("E'", scale = Vec2(0.7, 0.7))
        EPMove.on_click = lambda: self._SendOrientedMove("EPrime")()
        DPMove = self._MakeMove((self._Front[8].screen_position[0]+.1, self._Front[8].screen_position[1], 0), color.red, (0, 0, -90))
        DPMove.tooltip = Tooltip("D'", scale = Vec2(0.7, 0.7))
        DPMove.on_click = lambda: self._SendOrientedMove("DPrime")()

        FMove = self._MakeMove((self._Front[0].screen_position[0]-.1, self._Front[0].screen_position[1]+.1, 0), color.red, (0, 180, 0), "Turn")
        FMove.tooltip = Tooltip("F", scale = Vec2(0.7, 0.7))
        FMove.on_click = lambda: self._SendOrientedMove("F")()
        FPMove = self._MakeMove((self._Front[2].screen_position[0]+.1, self._Front[2].screen_position[1]+.1, 0), color.red, (0, 0, 0), "Turn")
        FPMove.tooltip = Tooltip("F'", scale = Vec2(0.7, 0.7))
        FPMove.on_click = lambda: self._SendOrientedMove("FPrime")()

        BMove = self._MakeMove((self._Front[6].screen_position[0]-.1, self._Front[6].screen_position[1]-.1, 0), color.red, (180, 180, 0), "Turn")
        BMove.tooltip = Tooltip("B", scale = Vec2(0.7, 0.7))
        BMove.on_click = lambda: self._SendOrientedMove("B")()
        BPMove = self._MakeMove((self._Front[8].screen_position[0]+.1, self._Front[8].screen_position[1]-.1, 0), color.red, (180, 0, 0), "Turn")
        BPMove.tooltip = Tooltip("B'", scale = Vec2(0.7, 0.7))
        BPMove.on_click = lambda: self._SendOrientedMove("BPrime")()
