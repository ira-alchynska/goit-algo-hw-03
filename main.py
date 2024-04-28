import os
import shutil
import sys

def copy_files(src_dir, dest_dir):
    """ Функція для рекурсивного копіювання файлів з src_dir до dest_dir. """
    try:
      
        os.makedirs(dest_dir, exist_ok=True)
        
     
        for item in os.listdir(src_dir):
            full_path = os.path.join(src_dir, item)
            
            if os.path.isdir(full_path):
              
                copy_files(full_path, dest_dir)
            elif os.path.isfile(full_path):
              
                ext = os.path.splitext(item)[1][1:]  
                if ext == '':
                    ext = 'no_extension'
                ext_dir = os.path.join(dest_dir, ext)
                os.makedirs(ext_dir, exist_ok=True)
                
              
                shutil.copy(full_path, ext_dir)
    except Exception as e:
        print(f"Помилка при копіюванні файлів: {e}")

def main():
  
    if len(sys.argv) < 2:
        print("Будь ласка, вкажіть шлях до вихідної директорії.")
        sys.exit(1)
    
    src_dir = sys.argv[1]
    dest_dir = sys.argv[2] if len(sys.argv) > 2 else "dist"
    

    copy_files(src_dir, dest_dir)

if __name__ == "__main__":
    main()
