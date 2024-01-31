from module.profile import ProfileManager

class Profile:
    def __init__(self):
        self.profile = ProfileManager()
    def create(self,profile_name, email, password, key):
        result = self.profile.create_profile(profile_name, email, password, key)
        return result
    def find_all(self):
        data = self.profile.get_all_profiles()
        data = data.get("data", {})
        return data
    def delete(self,profile_name):
        response = self.profile.delete_profile(profile_name)
        return response
    def update(self, old_profile_name,new_profile_name,email, password):
        response = self.profile.update_profile(old_profile_name,new_profile_name,email, password)
        return response