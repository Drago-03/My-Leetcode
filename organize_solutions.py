import os
import shutil
import re

def create_directory_structure():
    """Create the main directory structure for organized solutions."""
    categories = {
        'arrays_strings': ['Array', 'String', 'Two Pointers', 'Sliding Window'],
        'linked_lists': ['Linked List'],
        'trees_graphs': ['Tree', 'Binary Tree', 'Graph', 'Binary Search Tree'],
        'dynamic_programming': ['Dynamic Programming'],
        'binary_search': ['Binary Search'],
        'hash_tables': ['Hash Table', 'Hash Set', 'Hash Map'],
        'stack_queue': ['Stack', 'Queue', 'Monotonic Stack'],
        'heap': ['Heap', 'Priority Queue'],
        'greedy': ['Greedy'],
        'backtracking': ['Backtracking'],
        'math_bit': ['Math', 'Bit Manipulation'],
        'other': ['Other']
    }
    
    # Create directories and print status
    for category in categories:
        try:
            os.makedirs(category, exist_ok=True)
            print(f"Created directory: {category}")
        except Exception as e:
            print(f"Error creating directory {category}: {str(e)}")
    
    return categories

def get_problem_category(filename, problem_categories):
    """Determine the appropriate category for a problem based on its filename."""
    filename_lower = filename.lower()
    
    # Example mapping (extend this based on your actual solutions)
    if any(x in filename_lower for x in ['array', 'string', 'substring']):
        return 'arrays_strings'
    elif 'list' in filename_lower:
        return 'linked_lists'
    elif any(x in filename_lower for x in ['tree', 'graph']):
        return 'trees_graphs'
    elif 'dp' in filename_lower or 'dynamic' in filename_lower:
        return 'dynamic_programming'
    elif 'search' in filename_lower:
        return 'binary_search'
    elif 'hash' in filename_lower or 'map' in filename_lower:
        return 'hash_tables'
    elif 'stack' in filename_lower or 'queue' in filename_lower:
        return 'stack_queue'
    elif 'heap' in filename_lower:
        return 'heap'
    elif 'greedy' in filename_lower:
        return 'greedy'
    elif 'backtrack' in filename_lower:
        return 'backtracking'
    elif any(x in filename_lower for x in ['math', 'bit', 'number']):
        return 'math_bit'
    else:
        return 'other'

def organize_solutions():
    """
    Organize solutions from the current directory into appropriate category directories.
    """
    # Get the current directory
    current_dir = os.getcwd()
    print(f"Working in directory: {current_dir}")
    
    # Create directory structure
    categories = create_directory_structure()
    
    # Get all Python files in the current directory
    try:
        files = [f for f in os.listdir(current_dir) 
                if os.path.isfile(os.path.join(current_dir, f)) 
                and f.endswith('.py')
                and f != os.path.basename(__file__)]  # Exclude this script itself
        
        print(f"Found {len(files)} Python files to organize")
        
        # Process each file
        for file in files:
            try:
                # Determine category
                category = get_problem_category(file, categories)
                
                # Create source and destination paths
                source_path = os.path.join(current_dir, file)
                dest_path = os.path.join(current_dir, category, file)
                
                # Move file to appropriate directory
                shutil.move(source_path, dest_path)
                print(f"Moved {file} to {category}/")
            except Exception as e:
                print(f"Error processing file {file}: {str(e)}")
                
    except Exception as e:
        print(f"Error listing directory: {str(e)}")

if __name__ == "__main__":
    # Add error handling for the main execution
    try:
        organize_solutions()
        print("\nOrganization complete! Please check the categories to ensure files are correctly placed.")
    except Exception as e:
        print(f"An error occurred during execution: {str(e)}")