import collections

from math import ceil
from kivy.uix.label import Label

MapCoords = collections.namedtuple('MapCoords', ['row', 'col'])

class HexMapCell(Label):
    def __init__(self, row=0, col=0, **kwargs):
        super(HexMapCell, self).__init__(**kwargs)
        self.coords = MapCoords(row, col)
        ## set the cube coordinates of the hexagon
        ## as [x, y, z]
        self.cube_coords = self.even_r_to_cube(self.coords.row / 3, self.coords.col / 2)

    def even_r_to_cube(self, row, col):
        '''compute cube coordinates from even-r hex coordinates'''
        x = int(col - ceil(float(row)/2))
        z = row
        y = - x - z
        return([x, y, z])

    def cube_to_even_r(self, x, y, z):
        row = int(x + ceil(z / 2))
        col = z
        return ([row, col])

    @property
    def even_r_coords(self):
        '''return even-r coordinates of the hexagon.'''
        return(self.cube_to_even_r(*self.cube_coords))

    @even_r_coords.setter
    def even_r_coords(self, value):
        self.cube_coords = self.even_r_to_cube(*value)

    def coordinate_text(self):
        return '({}, {})'.format(self.coords.row, self.coords.col)

    def even_r_coordinate_text(self):
        return '{}'.format(self.even_r_coords)

    def cube_coordinate_text(self):
        return '{}\n{}\n{}'.format(*self.cube_coords)

    def map_display_text(self):
        return "{}\n{}".format(self.even_r_coordinate_text(), self.cube_coordinate_text())

    def update_pos(self, instance, value):
        # Determine the location of the solid hexagon cell.  Needs to be offset from the centre of the hex.
        radius = 2 * self.height
        solid_x = self.x - self.height*2
        solid_y = self.y - self.height*2
        solid_size = (4*self.height, 4*self.height)

        # Resize the outline of the cell.
        self.ell.circle = (self.x, self.y, radius, 0, 360, 6)

        # Resize the actual cell.
        self.solid.pos = (solid_x, solid_y)
        self.solid.size = solid_size

        self.coord_label.center_x = self.x
        self.coord_label.center_y = self.y

