
from kivy import app, properties
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Ellipse, Line
import kivy.utils
from hexmap import HexMapCell



class StrategyGame(FloatLayout):
    main_map = properties.ObjectProperty(None)
    map_rows = properties.NumericProperty(0)
    map_cols = properties.NumericProperty(0)

    def __init__(self, **kwargs):
        super(StrategyGame, self).__init__(**kwargs)

        number_of_regions = self.map_rows * self.map_cols
        for region in xrange(0, number_of_regions):
            row = region / self.map_cols
            col = region % self.map_cols

            # Add hex cells to make up the map.
            hex_cell = HexMapCell(row, col)
            self.main_map.add_widget(hex_cell)

            # Add overlay conditionally.
            if (row % 6 == 1 and col % 2 == 1) or (row % 6 == 4 and col % 2 == 0) and (col > 0):
                print('({}, {})'.format(row, col))

                # Determine the location of the solid hexagon cell.  Needs to be offset from the centre of the hex.
                radius = 2 * hex_cell.height
                solid_x = hex_cell.x - hex_cell.height*2
                solid_y = hex_cell.y - hex_cell.height*2
                solid_size = (4*hex_cell.height, 4*hex_cell.height)

                with hex_cell.canvas.after:

                    # Create the outline of hexagon, based off the centre of the hex.
                    Color(1, 0, 1, 1)
                    hex_cell.ell = Line(circle=(hex_cell.x, hex_cell.y, radius, 0, 360, 6), width=2)

                    # Create the solid background of the hexagon, from the bottom left coordinate of the hex.
                    Color(*kivy.utils.get_random_color(alpha=.5))
                    hex_cell.solid = Ellipse(pos=(solid_x, solid_y), size=solid_size, segments=6)

                    Color(1, 1, 1, 1)
                    hex_cell.coord_label = Label(
                        text=hex_cell.map_display_text(),
                        center_x=hex_cell.x,
                        center_y=hex_cell.y)

                # Bind the cell code so as to update its position and size when the parent widget resizes.
                hex_cell.bind(pos=hex_cell.update_pos, size=hex_cell.update_pos)


class StrategyGameApp(app.App):
    def build(self):
        return StrategyGame()

if __name__ == '__main__':
    StrategyGameApp().run()
