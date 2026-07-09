# Create a dictionary named test_settings with some initial values
test_settings = {
    'theme': 'light',
    'volume': 'medium'
}

# Define the add_setting function
def add_setting(settings_dict, setting_pair):
    key, value = setting_pair
    key = key.lower()
    value = value.lower()
    
    if key in settings_dict:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    
    settings_dict[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

# Define the update_setting function
def update_setting(settings_dict, setting_pair):
    key, value = setting_pair
    key = key.lower()
    value = value.lower()
    
    if key not in settings_dict:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
    
    settings_dict[key] = value
    return f"Setting '{key}' updated to '{value}' successfully!"

# Define the delete_setting function
def delete_setting(settings_dict, key):
    key = key.lower()
    
    if key not in settings_dict:
        return "Setting not found!"
    
    del settings_dict[key]
    return f"Setting '{key}' deleted successfully!"

# Define the view_settings function
def view_settings(settings_dict):
    if not settings_dict:
        return "No settings available."
    
    # Start the string with the required header and a newline
    output = "Current User Settings:\n"
    for key, value in settings_dict.items():
        # Capitalize the key while keeping the value lowercase
        output += f"{key.capitalize()}: {value}\n"
        
    return output