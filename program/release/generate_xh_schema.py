import zipfile  
import os  
  
def zip_folders_and_files(zip_name, folders, files):  
    """  
    将指定的多个文件夹和文件打包成一个ZIP文件。  
  
    :param zip_name: 输出的ZIP文件名  
    :param folders: 要打包的文件夹名列表  
    :param files: 要打包的文件名列表  
    """  
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:  
        # 添加文件夹  
        for folder in folders:  
            for root, dirs, files_in_folder in os.walk(folder):  
                for file in files_in_folder:  
                    file_path = os.path.join(root, file)  
                    arcname = os.path.relpath(file_path, os.path.dirname(folder))  
                    zipf.write(file_path, arcname)  
          
        # 添加文件  
        for file in files:  
            if os.path.isfile(file):  
                zipf.write(file, os.path.basename(file))  
  
# 使用示例  
folders = ['cn_dicts_xh', 'cn_dicts_common','custom_phrase','lua','opencc']  
files = ['default.yaml', 'flypy_flypy.schema.yaml','flypy_flypy.extended.dict.yaml',
         'symbols_caps_v.yaml','rime.lua','moqi.yaml'
         ]  
zip_folders_and_files('rime-墨奇版小鹤双拼鹤形.zip', folders, files)