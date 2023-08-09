
from git import Repo
import os

extensions_path = "/content/lite_colab/extensions/"
if not os.path.isdir(extensions_path):
    os.makedirs(extensions_path)
extensions_list_file = '/content/drive/MyDrive/AI/extensions.txt'
if os.path.exists(extensions_list_file):
  with open(extensions_list_file) as f:
    for line in f:
      try:
        git_loc = line.rstrip().split(" ")[0]
        folder_name = line.rstrip().split(" ")[1]
      except IndexError:
        git_loc = line.rstrip()
        folder_name = git_loc.split("/")[-1].split(".")[0]
      except Exception as e:
        print(e)
      Repo.clone_from(git_loc, extensions_path+folder_name)