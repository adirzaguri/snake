from directions import Direction
import constants

class Snake:
    def __init__(self,body,direction):
        self.body = body
        self.direction = direction
        self._tail=None

    @property
    def head(self):
        return self.body[0]

    def grow(self):
        self.body.append(self._tail)


    def set_direction(self,direction):
        self.direction = direction
    
    def is_dead():
        pass

    def update(self):    
        self._tail=self.body.pop()
        (x,y) = self.body[0]
        if self.direction == Direction.LEFT :
            if self.in_body((x,(y-1) % constants.Grid_rows)):
                return False
            self.body.insert(0,(x,(y-1) % constants.Grid_rows))
        if self.direction == Direction.UP :
            if self.in_body(((x-1) % constants.Grid_rows,y)):
                return False
            self.body.insert(0,((x-1) % constants.Grid_rows,y))
        if self.direction == Direction.RIGHT :
            if self.in_body((x,(y+1) % constants.Grid_rows)):
                return False
            self.body.insert(0,(x,(y+1) % constants.Grid_rows))
        if self.direction == Direction.DOWN :
            if self.in_body(((x+1) % constants.Grid_rows,y)):
                return False
            self.body.insert(0,((x+1) % constants.Grid_rows,y))
        
        return True

    def in_body(self,apple):
        return apple in self.body
    
    