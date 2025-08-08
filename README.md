# File Renamer

A file renamer utility is a command-line tool that automates the process of renaming multiple files in a directory. Instead of manually renaming each file, you can write a Python script that applies a specific set of rules to all the files at once.

## Project Description

Tool to mass rename files with patterns.


## Use Cases
This utility is surprising useful for a variety of real-world scenarios.

1. **Photo Organization**: Imagine you've downloaded hundreds of photos from a camera. They might have generic names like `DSC_0001.JPG`, `DSC_0002.JPG`, etc. You can use your utility to rename them to something more descriptive like `Vacation_202508_001.JPG`
2. **Batch Renaming Downloads**: Your downloads folder is probably a mess of files with unreadable names. You can use the script to remove common prefixes or suffixes like "(1)" or " - Copy".
3. **Code and Data Management**: When working on a project, you might need to rename a large set of data files or scripts to follow a new naming convention (e.g., changing "report_v1.txt" to "data_report_2024_Q1.txt").
4. **Audio File Management**: For music lovers, this tool can be used to rename a batch of audio files to a consistent format, such as "Artist - Title.mp3", by extracting information from the existing filenames.
5. **Learning and Practice**: This project is a fantastic learning tool. It forces you to think about error handling (what if a file with the new name already exists?), user experience (how to make the command-line interface easy to use?), and system interaction in a controlled environment.


#### Sample

`renamer rename . "DCE_\w*_SUF\.log" -p NEW_PREFIX -s NEW_SUFFIX --replace DCE ABC`
