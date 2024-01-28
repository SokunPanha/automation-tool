import os
import pickle
from cryptography.fernet import Fernet

class ProfileDataManager:
    def __init__(self):
        self.binary_file_path = os.path.join(os.getcwd(), "model\\data-user_profile.bin")
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)
        self.current_key = None

    def read_data(self):
        try:
            with open(self.binary_file_path, 'rb') as binary_file:
                return pickle.load(binary_file)
        except FileNotFoundError:
            return {}
        except (pickle.UnpicklingError, EOFError):
            return {}

    def write_data(self, data):
        with open(self.binary_file_path, 'wb') as binary_file:
            pickle.dump(data, binary_file)

    def encrypt(self, data):
        return self.cipher.encrypt(data.encode()).decode()

    def decrypt(self, data):
        return self.cipher.decrypt(data.encode()).decode()

    def set_current_key(self, key):
        self.current_key = key

    def create_profile(self, profile_name, email, password):
        existing_data = self.read_data()

        # Ensure existing_data is a dictionary
        if not isinstance(existing_data, dict):
            existing_data = {}

        # Encrypt the password before storing
        encrypted_password = self.encrypt(password)

        existing_data[profile_name] = {
            "email": email,
            "password": encrypted_password
        }

        self.write_data(existing_data)
        self.set_current_key(profile_name)

    def read_profile(self):
        existing_data = self.read_data()
        profile_data = existing_data.get(self.current_key, None)

        if profile_data:
            # Decrypt the password before returning
            profile_data["password"] = self.decrypt(profile_data["password"])

        return profile_data

    def update_profile(self, new_profile_name=None, email=None, password=None):
        existing_data = self.read_data()

        if self.current_key in existing_data:
            # Update profile name if provided
            if new_profile_name:
                # Create a new entry with the new profile name
                existing_data[new_profile_name] = existing_data.pop(self.current_key)
                self.set_current_key(new_profile_name)
            else:
                new_profile_name = self.current_key

            # Update email if provided
            if email:
                existing_data[new_profile_name]["email"] = email

            # Update password if provided
            if password:
                existing_data[new_profile_name]["password"] = self.encrypt(password)

            self.write_data(existing_data)
            print(f"Profile '{new_profile_name}' updated successfully.")
        else:
            print(f"Profile '{self.current_key}' does not exist.")

    def delete_profile(self):
        existing_data = self.read_data()

        if self.current_key in existing_data:
            del existing_data[self.current_key]
            self.write_data(existing_data)
            print(f"Profile '{self.current_key}' deleted successfully.")
            self.set_current_key(None)
        else:
            print(f"Profile '{self.current_key}' does not exist.")

    def get_all_profiles(self):
        existing_data = self.read_data()

        for profile_name, profile_data in existing_data.items():
            profile_data["password"] = self.decrypt(profile_data["password"])

        return existing_data

    def delete_all_profiles(self):
        # Deletes all profiles and updates the binary file
        self.write_data({})
        print("All profiles deleted successfully.")
