import arcade
#draws a smiley face

#set window dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# open the window set the tie and the dimetions
arcade.open_window(SCREEN_WIDTH,SCREEN_HEIGHT,"smiley face")


x = 300
y = 300
# start the render process
arcade.start_render()
class Smiley(arcade.Window):
    def __init__(self,width,height):
        super().__init__(width,height,"smiley face game!")
        arcade.set_background_color(arcade.color.WHITE)
    def setup(self):
        # setup your game here
        pass
    def on_draw(self):
        """smiley drawing here."""
        arcade.start_render()
        x = 300
        y = 300
        radius = 200
        arcade.draw_circle_filled(x,y,radius,arcade.color.TAN)

        # make right eye
        x = 378
        y = 355
        radius = 20
        arcade.draw_circle_filled(x,y,radius,arcade.color.BLACK)
        # make left eye
        x = 228
        y = 354
        radius = 20
        arcade.draw_circle_filled(x,y,radius,arcade.color.BLACK)
        # make left eyebrow
        x = 225
        y = 300
        width = 100
        height =120
        arcade.draw_arc_outline(x,y,width,height,arcade.color.BLACK,start_angle=55,end_angle=130)

        # make the right eyebrow
        color = arcade.color.BLACK
        x = 378
        y = 301
        width = 100
        height = 124
        arcade.draw_arc_outline(x,y,width,height,arcade.color.BLACK,start_angle=55,end_angle=130,)
        border_width = 20


        # make the smile
        color = arcade.color.BLACK
        x = 300
        y = 220
        width = 100
        height = 60
        arcade.draw_arc_outline(x,y,width,height,arcade.color.BLACK,start_angle=190,end_angle=350,border_width = 5)

        arcade.finish_render()
    def update(self,delta_time):
        """all the logic to move and game logic goes here."""
        pass
def main():
    game = Smiley(SCREEN_WIDTH,SCREEN_HEIGHT)
    game.setup()
    arcade.run()
if __name__=="__main__":
    main()



