### ft2j

This tool will take the file structure and convert it to a JSON file.

The folders contain files, and each file is represented by a key-value pair.

Consider the following structure
```
|_...__
       |_Hello.txt
       |_W
          |wolrd.txt
```

With the file `Hello.txt` containing `Hello!` and the file `world.txt` inside `W` containing `orld`, the
generated JSON will have:


```
{
    "W": {
        "world.txt": "orld\n"
    },
    "Hello.txt": "Hello!\n"
}
```

#### Command line arguments

  * `-h`, `--help`, show the help message and exit
  * `-d DIRECTORY`, `--directory DIRECTORY` The path of the directory to convert.
  * `-o OUTPUT`, `--output OUTPUT` The path of the output JSON file. Defaults to 'output.json'.
  * `-i JSON_FILE`, `--json_file JSON_FILE` The path of the JSON file containing the directory structure.
  * `-p OUTPUT_DIRECTORY`, `--output_directory OUTPUT_DIRECTORY` The root directory where the structure will be recreated.
  * `-v VERBOSE`, `--verbose VERBOSE` Enable verbose output.
 
