import os
import shutil
import getpass

def clear_folder(path):
    """Deletes all contents inside the given folder"""
    if os.path.exists(path):
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.remove(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")
    else:
        print(f"Path does not exist: {path}")

def main():
    user = getpass.getuser()

    # FiveM cache folders
    fivem_cache_main = f"C:/Users/{user}/AppData/Local/FiveM/FiveM.app/data/cache"
    fivem_cache_priv = f"C:/Users/{user}/AppData/Local/FiveM/FiveM.app/data/server-cache-priv"
    fivem_cache_priv_cl2 = f"C:/Users/{user}/AppData/Local/FiveM/FiveM.app/data/server-cache-priv-cl2"

    # Common Windows cache/temp folders
    temp_folder = f"C:/Users/{user}/AppData/Local/Temp"
    prefetch_folder = "C:/Windows/Prefetch"  # requires admin
    windows_temp = "C:/Windows/Temp"        # requires admin

    print("Clearing FiveM Cache (main)...")
    clear_folder(fivem_cache_main)

    print("\nClearing FiveM Cache (server-cache-priv)...")
    clear_folder(fivem_cache_priv)

    print("\nClearing FiveM Cache (server-cache-priv-cl2)...")
    clear_folder(fivem_cache_priv_cl2)

    print("\nClearing User Temp...")
    clear_folder(temp_folder)

    print("\nClearing Windows Temp...")
    clear_folder(windows_temp)

    print("\nClearing Prefetch...")
    clear_folder(prefetch_folder)

    print("\n✅ Cache cleaning complete!")

if __name__ == "__main__":
    main()
