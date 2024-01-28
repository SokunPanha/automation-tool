
import os

class ProfileDirectoryManager:
    def __init__(self):
        self.base_path = os.path.join(os.getcwd(),"profile")

    def create_profile(self, directory_name):
        folder_path = os.path.join(self.base_path, directory_name)
        print(folder_path)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Profile name <'{directory_name}'> created successfully")
        else:
            print(f"Profile name <'{directory_name}'> already exists")

    def delete_profile(self, directory_name):
        folder_path = os.path.join(self.base_path, directory_name)
        if os.path.exists(folder_path):
            os.rmdir(folder_path)
            print(f"Folder '{folder_path}' deleted successfully")
        else:
            print(f"Folder '{folder_path}' does not exist")

    def rename_profile(self, old_dir, new_dir):
        current_path = os.path.join(self.base_path, old_dir)
        new_path = os.path.join(os.path.dirname(current_path), new_dir)
        if os.path.exists(current_path):
            os.rename(current_path, new_path)
            print(f"Folder '{current_path}' renamed to '{new_path}' successfully")
        else:
            print(f"Folder '{current_path}' does not exist")

    def get_all_profiles(self):
        directory_path = self.base_path
        all_items = os.listdir(directory_path)
        folder_names = [item for item in all_items if os.path.isdir(os.path.join(directory_path, item))]
        return folder_names

    def delete_all_profiles(self):
        all_items = self.get_all_profiles()
        for item in all_items:
            item_path = os.path.join(self.base_path, item)
            if os.path.isdir(item_path):
                try:
                    os.rmdir(item_path)
                    print(f"Folder '{item_path}' deleted successfully")
                except OSError as e:
                    print(f"Error deleting folder '{item_path}': {e}")
