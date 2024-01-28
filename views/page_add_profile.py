from flet import *
from flet_route import Params, Routing, Basket
from module.module_profile.module_ProfileManager import ProfileManager
def Add_Profile(page :Page,  params: Params, basket: Basket):
    profile_name = TextField(prefix_icon=icons.PERSON_3, width=350, hint_text= "Profile Name", border_color= "white")
    email =  TextField(prefix_icon=icons.EMAIL, width=350, hint_text="Email",  border_color= "white")
    password =  TextField(password= True, prefix_icon=icons.PASSWORD, hint_text= "Password", width=350, border_color= "white")
    def button_clicked(e):
        create_profile(page,profile_name.value,email.value, password.value)
        page.go("/profile")
        page.update()
    return Column(
        horizontal_alignment= "center" ,
        alignment= CrossAxisAlignment.CENTER,
        controls=[
            Text("Add Profile"),
            profile_name,
            email,
            password,
            Container(
                width = 350,
                content=Row(
                    controls=[
                        ElevatedButton(text="Cancel", bgcolor="red", color="white"),
                        ElevatedButton(text="Add", bgcolor="indigo", color="white",  on_click= button_clicked)  
                        
                        ],
                        alignment= MainAxisAlignment.END
            )
            )
        ],
    )

def create_profile(page,profile_name, email, password):
    profile = ProfileManager()
    result = profile.create_profile(profile_name, email, password)
    print(result)
    

