from dataclasses import dataclass, field
from pathlib import Path
import os

@dataclass
class DirectoryScanner(): # Don't inherit from dir_path
    directoryPath: str # Use str as the type, not dir_path
    files: list = field(default_factory=list)
    AppleDoubleFiles: dict = field(default_factory=dict)
    dirs: list = field(default_factory=list)
    sizes: dict = field(default_factory=dict)

    def total_size(self):
        """Get total size in bytes"""
        return sum(self.sizes.values())

    def filesizeFormat(self):
        size_bytes = self.total_size()
        # calculate file size in KB, GB, MB, TB
        """Convert bytes to human-readable format"""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.2f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.2f} PB"

def DirectoryInfo(dir_path):
    results = DirectoryScanner(dir_path)

    for item in Path(dir_path).rglob("*"):
        if item.is_file() and not item.name.startswith('._'):
            results.files.append(str(item))  # Changed: Use dot notation
            results.sizes[str(item)] = item.stat().st_size
        elif item.is_file() and item.name.startswith('._'):
            results.AppleDoubleFiles[str(item)] = item.stat().st_size
        elif item.is_dir():
            results.dirs.append(str(item))

    fileSize = results.total_size()
    fileSize_str = results.filesizeFormat()
    return results

def GetChildItem_Recurse_py(dir_path):
    # Basic version - just list all files and directories
    for root, dirs, files in os.walk(dir_path):
        for name in dirs:
            print(os.path.join(root, name))
        for name in files:
            print(os.path.join(root, name))

dir_path = r"D:\日本🇯🇵旅遊2025"
# dir_path = input("Type directory path to list all file contents in: \n").strip()

results = DirectoryInfo(dir_path)

print(f"{results.filesizeFormat()} / {results.total_size()} bytes")
# Print directory names only
print("\n--- Directories ---")
for dirname in results.dirs:
    directory, filename = os.path.split(dirname)
    print(filename)

# Print paired files (note: AppleDouble files may not match 1-to-1)
print("\n--- Files and their AppleDouble counterparts ---")
for file in results.files:
    directory, filename = os.path.split(file)
    # Look for corresponding AppleDouble file
    appledouble_path = os.path.join(directory, f"._{filename}")

    if appledouble_path in results.AppleDoubleFiles:
        _, appledoublefilename = os.path.split(appledouble_path)
        print(f"{filename} → {appledoublefilename}")
    else:
        print(f"{filename} → (no AppleDouble file)")