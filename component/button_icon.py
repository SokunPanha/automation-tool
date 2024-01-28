
from flet import *

class Button_Icon(UserControl):
    def __init__(self,page:Page,margin:Margin, text, style: ButtonStyle, icon: Icon, route):
        super().__init__()
        self.page = page
        self.icon = icon
        self.text = text
        self.route = route
        self.style = style
        self.color: colors = colors.GREY_800
        self.margin = margin
    def build(self):
        return Container(
            margin= self.margin,
            content=ElevatedButton("Add", style= self.style,icon= self.icon,
              on_click= lambda _ : self.page.go(self.route)
              )
        )
