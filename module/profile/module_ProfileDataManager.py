# import os
# import json
# from cryptography.fernet import Fernet, InvalidToken

# class ProfileDataManager:
#     def __init__(self):
#         self.json_file_path = os.path.join(os.getcwd(), "model\\data-user_profile.json")
#         self.key = Fernet.generate_key()
#         self.cipher = Fernet(self.key)
#         self.current_key = None

#     def read_data(self):
#         try:
#             with open(self.json_file_path, 'r') as json_file:
#                 return json.load(json_file)
#         except FileNotFoundError:
#             return {}
#         except json.JSONDecodeError:
#             return {}

#     def write_data(self, data):
#         with open(self.json_file_path, 'w') as json_file:
#             json.dump(data, json_file, indent=2)

#     def encrypt_password(self, password):
#         return self.cipher.encrypt(password.encode()).decode()

#     def decrypt_password(self, encrypted_password):
#         try:
#             return self.cipher.decrypt(encrypted_password.encode()).decode()
#         except InvalidToken:
#             # Handle the case where decryption fails (e.g., data is not encrypted)
#             print(f"Warning: Decryption failed for password: {encrypted_password}")
#             return encrypted_password
#         except Exception as e:
#             # Handle other exceptions, e.g., when the data is not encrypted and cannot be decoded
#             print(f"Error: {e}")
#             return encrypted_password

#     def set_current_key(self, key):
#         self.current_key = key

#     def create_profile(self, profile_name, email, password):
#         existing_data = self.read_data()

#         # Ensure existing_data is a dictionary
#         if not isinstance(existing_data, dict):
#             existing_data = {}

#         # Encrypt password before storing
#         encrypted_password = self.encrypt_password(password)

#         existing_data[profile_name] = {
#             "email": email,
#             "password": encrypted_password
#         }

#         self.write_data(existing_data)
#         self.set_current_key(profile_name)

#     def read_profile(self):
#         existing_data = self.read_data()
#         profile_data = existing_data.get(self.current_key, None)

#         if profile_data:
#             # Decrypt the password before returning
#             profile_data["password"] = self.decrypt_password(profile_data["password"])

#         return profile_data

#     def update_profile(self, new_profile_name=None, email=None, password=None):
#         existing_data = self.read_data()

#         if self.current_key in existing_data:
#             # Update profile name if provided
#             if new_profile_name:
#                 # Create a new entry with the new profile name
#                 existing_data[new_profile_name] = existing_data.pop(self.current_key)
#                 self.set_current_key(new_profile_name)
#             else:
#                 new_profile_name = self.current_key

#             # Update email if provided
#             if email:
#                 existing_data[new_profile_name]["email"] = email

#             # Update password if provided
#             if password:
#                 existing_data[new_profile_name]["password"] = self.encrypt_password(password)

#             self.write_data(existing_data)
#             print(f"Profile '{new_profile_name}' updated successfully.")
#         else:
#             print(f"Profile '{self.current_key}' does not exist.")

#     def delete_profile(self):
#         existing_data = self.read_data()

#         if self.current_key in existing_data:
#             del existing_data[self.current_key]
#             self.write_data(existing_data)
#             print(f"Profile '{self.current_key}' deleted successfully.")
#             self.set_current_key(None)
#         else:
#             print(f"Profile '{self.current_key}' does not exist.")

#     def get_all_profiles(self):
#         existing_data = self.read_data()

#         for profile_name, profile_data in existing_data.items():
#             # Check if the password field is encrypted before decrypting
#             if "password" in profile_data:
#                 profile_data["password"] = self.decrypt_password(profile_data["password"])

#         return existing_data


#     def delete_all_profiles(self):
#         # Deletes all profiles and updates the JSON file
#         self.write_data({})
#         print("All profiles deleted successfully.")

# profile_manager = ProfileDataManager()

# # Test reading a profile
# profile_data = profile_manager.get_all_profiles()
# print("Read Profile:", profile_data)


# import os
# import json
# from cryptography.fernet import Fernet, InvalidToken

# class ProfileDataManager:
#     def __init__(self):
#         self.json_file_path = os.path.join(os.getcwd(), "model\\data-user_profile.json")
#         self.key = Fernet.generate_key()
#         self.cipher = Fernet(self.key)
#         self.current_key = None

#     def read_data(self):
#         try:
#             with open(self.json_file_path, 'r') as json_file:
#                 return json.load(json_file)
#         except FileNotFoundError:
#             return {}
#         except json.JSONDecodeError:
#             return {}

#     def write_data(self, data):
#         with open(self.json_file_path, 'w') as json_file:
#             json.dump(data, json_file, indent=2)

#     def encrypt_password(self, password):
#         return self.cipher.encrypt(password.encode()).decode()

#     def decrypt_password(self, encrypted_password):
#         try:
#             return self.cipher.decrypt(encrypted_password.encode()).decode()
#         except InvalidToken:
#             # Handle the case where decryption fails (e.g., data is not encrypted)
#             print(f"Warning: Decryption failed for password: {encrypted_password}")
#             return encrypted_password
#         except Exception as e:
#             # Handle other exceptions, e.g., when the data is not encrypted and cannot be decoded
#             print(f"Error: {e}")
#             return encrypted_password

#     def set_current_key(self, key):
#         self.current_key = key

#     def create_profile(self, profile_name, email, password):
#         existing_data = self.read_data()

#         # Ensure existing_data is a dictionary
#         if not isinstance(existing_data, dict):
#             existing_data = {}

#         existing_data[profile_name] = {
#             "email": email,
#             "password": password  # Store the password without encryption
#         }

#         self.write_data(existing_data)
#         self.set_current_key(profile_name)

#     def read_profile(self, profile_name=None):
#         existing_data = self.read_data()

#         if profile_name is None:
#             profile_name = self.current_key

#         profile_data = existing_data.get(profile_name, None)

#         if profile_data:
#             # Decrypt the password before returning
#             profile_data["password"] = self.decrypt_password(profile_data["password"])

#         return profile_data


#     def update_profile(self, old_profile_name, new_profile_name=None, email=None, password=None):
#         existing_data = self.read_data()

#         if old_profile_name in existing_data:
#             # Update profile name if provided
#             if new_profile_name:
#                 # Create a new entry with the new profile name
#                 existing_data[new_profile_name] = existing_data.pop(old_profile_name)
#                 self.set_current_key(new_profile_name)
#             else:
#                 new_profile_name = old_profile_name

#             # Update email if provided
#             if email:
#                 existing_data[new_profile_name]["email"] = email

#             # Update password if provided
#             if password:
#                 existing_data[new_profile_name]["password"] = password  # Store the password without encryption

#             self.write_data(existing_data)
#             print(f"Profile '{new_profile_name}' updated successfully.")
#         else:
#             print(f"Profile '{old_profile_name}' does not exist.")


#     def delete_profile(self, profile_name=None):
#         existing_data = self.read_data()

#         if profile_name is None:
#             profile_name = self.current_key

#         if profile_name in existing_data:
#             del existing_data[profile_name]
#             self.write_data(existing_data)
#             print(f"Profile '{profile_name}' deleted successfully.")
#             self.set_current_key(None)
#         else:
#             print(f"Profile '{profile_name}' does not exist.")


#     def get_all_profiles(self):
#         existing_data = self.read_data()

#         return existing_data

#     def delete_all_profiles(self):
#         # Deletes all profiles and updates the JSON file
#         self.write_data({})
#         print("All profiles deleted successfully.")


import os
import json

import os
import json

class ProfileDataManager:
    def __init__(self):
        self.file_path = os.path.join(os.getcwd(), "model\\data-user_profile.bin")
        self.current_key = None

    def read_data(self):
        try:
            with open(self.file_path, 'rb') as binary_file:
                data_bytes = binary_file.read()
                if data_bytes:
                    data_str = data_bytes.decode()
                    return json.loads(data_str)
                else:
                    return {}
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {}

    def write_data(self, data):
        with open(self.file_path, 'wb') as binary_file:
            json_string = json.dumps(data, indent=2)
            binary_file.write(json_string.encode())

    def set_current_key(self, key):
        self.current_key = key

    def create_profile(self, profile_name, email, password, key):
        existing_data = self.read_data()

        if not isinstance(existing_data, dict):
            existing_data = {}

        existing_data[profile_name] = {
            "email": email,
            "password": password,
            "key": key
        }

        self.write_data(existing_data)
        self.set_current_key(profile_name)


    def set_current_key(self, key):
        self.current_key = key

    def create_profile(self, profile_name, email, password, key):
        existing_data = self.read_data()

        if not isinstance(existing_data, dict):
            existing_data = {}

        existing_data[profile_name] = {
            "email": email,
            "password": password,
            "key": key
        }

        self.write_data(existing_data)
        self.set_current_key(profile_name)

    def read_profile(self, profile_name=None):
        existing_data = self.read_data()

        if profile_name is None:
            profile_name = self.current_key

        return existing_data.get(profile_name, None)

    def update_profile(self, old_profile_name, new_profile_name=None, email=None, password=None):
        existing_data = self.read_data()

        if old_profile_name in existing_data:
            if new_profile_name:
                existing_data[new_profile_name] = existing_data.pop(old_profile_name)
                self.set_current_key(new_profile_name)
            else:
                new_profile_name = old_profile_name

            if email:
                existing_data[new_profile_name]["email"] = email

            if password:
                existing_data[new_profile_name]["password"] = password

            self.write_data(existing_data)
            print(f"Profile '{new_profile_name}' updated successfully.")
        else:
            print(f"Profile '{old_profile_name}' does not exist.")

    def delete_profile(self, profile_name=None):
        existing_data = self.read_data()

        if profile_name is None:
            profile_name = self.current_key

        if profile_name in existing_data:
            del existing_data[profile_name]
            self.write_data(existing_data)
            print(f"Profile '{profile_name}' deleted successfully.")
            self.set_current_key(None)
        else:
            print(f"Profile '{profile_name}' does not exist.")

    def get_all_profiles(self):
        existing_data = self.read_data()
        return existing_data

    def delete_all_profiles(self):
        self.write_data({})
        print("All profiles deleted successfully.")

