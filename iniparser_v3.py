import configparser #apparently there's the library configparser that can parse ini files!

def parse_ini(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)

    profiles = {}
    non_profiles = {}

    for section in config.sections():
        if section.startswith("Profile"):
            profile_number = int(section.replace("Profile", ""))
            profiles[profile_number] = {k: v for k, v in config.items(section)}
        else:
            non_profiles[section] = {k: v for k, v in config.items(section)}
    profiles_new_positions = list(sorted(profiles.keys(), key=int))
    
    return profiles, non_profiles, profiles_new_positions


def reconstruct_ini(profiles, non_profiles, output_path):
    config = configparser.ConfigParser()

    new_profile_number = 0
    for i in range(len(profiles_new_positions)):
        old_profile_number = profiles_new_positions[i]
        if old_profile_number == 'deleted':
            continue
        elif old_profile_number == 'new':
            section = f"Profile{new_profile_number}"
            config[section] = {'Name':'', 'IsRelative':'','Path':''}
            new_profile_number += 1
        else:
            section = f"Profile{new_profile_number}"
            config[section] = profiles[old_profile_number]
            new_profile_number += 1

    for section, params in non_profiles.items():
        config[section] = params

    with open(output_path, 'w') as configfile:
        config.write(configfile)

#profiler modification functions
def exchange_profiles(profiles_new_positions, profile1, profile2):
    profiles_new_positions[profile1], profiles_new_positions[profile2] = profiles_new_positions[profile2], profiles_new_positions[profile1]
def delete_profile(profiles_new_positions, profile):
    profiles_new_positions[profile] = 'deleted'
def add_profile(profiles_new_positions):
    profiles_new_positions.append('new')
    print('A stub for new profile is appended to ini, fill it later manually')


# Run the script
if __name__ == "__main__":

    path_to_ini = input("Enter path to ini file: ")

    profiles, non_profiles, profiles_new_positions = parse_ini(path_to_ini)
    #print("Profiles:", profiles)
    #print("Non-Profiles:", non_profiles)
    #print(profiles_new_positions)

    # Modify the profiles
    mod_functions = {'add': add_profile, 'delete': delete_profile, 'exchange': exchange_profiles}
    while True:
        command = input("Enter command (add/delete/exchange). Enter to exit: ").split()
        if not command:
            break
        if command[0] not in mod_functions:
            print("Invalid command")
            continue
        try: 
            mod_functions[command[0]](profiles_new_positions, *map(int, command[1:]))
        except:
            print("Invalid arguments")
            continue
    output_path = input("Enter path to save new ini file. Leave empty to rewrite original: ")
    if output_path == '':
        output_path = path_to_ini

    reconstruct_ini(profiles, non_profiles, output_path)
    print(f"New ini file saved to {output_path}")