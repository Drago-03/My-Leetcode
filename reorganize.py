import os
import shutil

def collect_all_solutions():
    """Collect all solution files from subdirectories back to main directory"""
    current_dir = os.getcwd()
    print(f"Working in directory: {current_dir}")
    
    # Get all subdirectories
    subdirs = [d for d in os.listdir(current_dir) 
              if os.path.isdir(os.path.join(current_dir, d))]
    
    moved_files = 0
    print("\nCollecting files from subdirectories...")
    
    # Process each subdirectory
    for subdir in subdirs:
        subdir_path = os.path.join(current_dir, subdir)
        try:
            # Get all Python files in the subdirectory
            files = [f for f in os.listdir(subdir_path) 
                    if f.endswith('.py')]
            
            # Move each file to the main directory
            for file in files:
                source_path = os.path.join(subdir_path, file)
                dest_path = os.path.join(current_dir, file)
                
                # Handle duplicate files
                if os.path.exists(dest_path):
                    base, ext = os.path.splitext(file)
                    i = 1
                    while os.path.exists(dest_path):
                        new_name = f"{base}_{i}{ext}"
                        dest_path = os.path.join(current_dir, new_name)
                        i += 1
                
                shutil.move(source_path, dest_path)
                print(f"Moved {file} to main directory")
                moved_files += 1
                
            # Remove empty directory
            if not os.listdir(subdir_path):
                os.rmdir(subdir_path)
                print(f"Removed empty directory: {subdir}")
                
        except Exception as e:
            print(f"Error processing directory {subdir}: {str(e)}")
    
    print(f"\nMoved {moved_files} files to main directory")
    print("Cleanup complete!")

def delete_empty_categories():
    """Delete all empty category directories"""
    current_dir = os.getcwd()
    
    # Get all subdirectories
    subdirs = [d for d in os.listdir(current_dir) 
              if os.path.isdir(os.path.join(current_dir, d))]
    
    deleted_dirs = 0
    print("\nRemoving empty directories...")
    
    # Delete empty directories
    for subdir in subdirs:
        dir_path = os.path.join(current_dir, subdir)
        try:
            if not os.listdir(dir_path):
                os.rmdir(dir_path)
                print(f"Removed empty directory: {subdir}")
                deleted_dirs += 1
        except Exception as e:
            print(f"Error removing directory {subdir}: {str(e)}")
    
    print(f"Removed {deleted_dirs} empty directories")

if __name__ == "__main__":
    print("LeetCode Solutions Reorganizer")
    print("-----------------------------")
    
    while True:
        print("\nChoose an option:")
        print("1. Collect all solutions into main directory")
        print("2. Remove empty category directories")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == "1":
            collect_all_solutions()
        elif choice == "2":
            delete_empty_categories()
        elif choice == "3":
            print("\nExiting reorganizer...")
            break
        else:
            print("\nInvalid choice. Please try again.")