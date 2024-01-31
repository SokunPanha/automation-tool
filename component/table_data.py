from flet import *
from api.profile import Profile
from flet_route import Basket, Params
class ProfileDataTable(UserControl):
    def __init__(self,page:Page, params:Params, basket:Basket, route):
        super().__init__()
        self.profile = Profile()
        self.data = self.profile.find_all()
        self.page =page
        self.params =params 
        self.basket = basket
        self.route = route
    def Delete(self,e):
            pname = e.control.data
            self.profile.delete(pname)
            self.page.update()
    def edit(self,  e):
        self.basket.data =e.control.data
        print(self.basket.data)
        self.page.update()
        self.page.go(self.route)

    def build(self):
        # page.update()

        data_table = DataTable(
                columns=[DataColumn(Text("Profile Name")),DataColumn(Text("Email")), DataColumn(Text("Action", text_align= alignment.center)),]
            )
    
        for pname, user_data in self.data.items():
            data_table.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(pname)),
                        DataCell(Text(user_data["email"])),
                        DataCell(Row(controls=[IconButton("EDIT", on_click= self.edit, data = [pname, user_data]) ,IconButton(icon=icons.DELETE, on_click= self.Delete, data= pname)]))
                    ],
                )
            )    

        return data_table
           