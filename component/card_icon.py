from flet import *

class Card_Icon(UserControl):
    def __init__(self,page:Page, icon:Icon, text, route):
        super().__init__()
        self.page = page
        self.icon = icon
        self.text = text
        self.route = route
        self.color: colors = colors.GREY_800
    def build(self):
        return  Card(
            content= Container(
            on_click= lambda _ : self.page.go(self.route),
            bgcolor= self.color,
            width= 100,
            # on_hover= lambda _ : self.color = "red",
            border_radius=20,
            height=100,
            padding= 10,
            alignment= alignment.center,
            content= Column(
                spacing=0.5,
                controls=[
                    Icon(name= self.icon, size=50),
                    Text(value= self.text)
                ],
                horizontal_alignment= CrossAxisAlignment.CENTER
            )
            )
        )