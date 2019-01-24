import sys
import argparse
import json
import os

def process_token_file(filepath):
    tokens = dict()

    with open(filepath, 'r+') as f:
        lines = f.readlines()

        # for each line, get the key value pairs
        for line in lines:
            key, value = line.rstrip("\n").split(";")
            tokens.update({key: value})

    return tokens

def process_target_file(filepath, token={"#env#": "DEV"}):
    print("### PROCESSING THE FILE ###", filepath)
    with open(filepath, 'r+') as f:
        contents = f.read()
        
        # replace all key-value pairs
        for k, v in token.items():
            contents = contents.replace(k, v)

        # Go to the 0 initials
        f.seek(0)

        # write the replaced contents
        f.write(contents)
        f.truncate()
    return

def main():
    # filepath = 'test_folder.xml'

    # arguments
    target_folder = 'target_folder'
    token_file = 'token_file'

    parser = argparse.ArgumentParser(
        description="Detokeniser target_file according to the token_file"
        )

    parser.add_argument(target_folder, help="The target file needs to be detokenised")
    parser.add_argument(token_file, help="The token file contains the key-value pairs")
    args = parser.parse_args()

    token_dict = process_token_file(args.token_file)
    print("This is the token_dict", token_dict)

    for root, dirs, files in os.walk(args.target_folder):
        for filename in files:
            print("#####", root, filename, "#####")
            processing_filename = root+"/"+filename
            process_target_file(processing_filename, token=token_dict)

    return


if __name__ == '__main__':
    main()

