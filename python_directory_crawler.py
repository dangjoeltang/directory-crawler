import os, sys
import csv


def main():
    path = sys.argv[1]
    # path = os.path.dirname(sys.argv[1])
    print('Start')
    traverse(path)
    print('Finish')

# with open('/tmp/output.csv', 'wb') as csvfile:
#   writer = csv.writer(csvfile)
#   writer.writerow(['Project Name', 'Documents'])
#   for dirpath, _, filenames in os.walk(path):
#     if filenames:
#       writer.writerow([os.path.basename(dirpath)] + filenames)

def traverse(directory):
    with open('output.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Path', 'File'])
        for entry in helper(directory):
            writer.writerow(entry)
        # for path, dirs, files in os.walk(directory):
        #     for filename in files:
        #         # writer.writerow([os.path.dirname(path) + '\\' + filename])
        #         writer.writerow([os.path.relpath(path, os.path.dirname(directory)) + '\\' + filename] + [filename])
        

def helper(directory):
    """Yield directory names not starting with '.' under given path."""
    for entry in os.scandir(directory):
        if entry.is_file():
            yield [entry.path, entry.name]
        elif entry.is_dir():
            yield from helper(entry.path)
        else:
            print(f"Neither a file, nor a dir: {entry.path}")

if __name__ == "__main__":
    main()