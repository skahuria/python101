from pathlib import Path

# Absolute path
# c:\Program Files\Microsoft

# Relative path
path = Path("ecommerce")
print(path.exists())

#  create directory
# path = Path("emails")
# print(path.mkdir())

# remove directory
# path = Path("emails")
# print(path.rmdir())

# Search for file in current directory
path = Path()
for file in (path.glob('*')):
    print(file)



