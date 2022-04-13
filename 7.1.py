import  os

folder_1 = 'settings', 'mainapp', 'adminapp', 'authapp'
folder_2 = 'mu_project'

# for folders in folder_2:
if not os.path.exists(folder_2):
    # os.mkdir(folder_2)
    for folder in folder_1:
        folders = os.path.join(folder_2, folder)
        os.makedirs(folders)