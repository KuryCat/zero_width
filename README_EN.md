# zero_width 1.0

A Python utility that enables you to hide and reveal secret messages within text using Zero-Width Characters. Text containing hidden payloads appears entirely normal to the human eye, but systems and the tool can still read the original content.

## Key Features

1. Reveal hidden words within a text string.
2. Merge words to be hidden into regular text in an invisible format.

## Installation

The tool runs directly via Python 3 without requiring any third-party libraries:

```bash
python main.py
```

## Usage

### 1. Merge Hidden Words into Text (Merge)

Use the `merge` command to embed a word at a specific location within the original text. The embedded word converts into invisible zero-width characters.

Full syntax:
```bash
python main.py merge "hello [___] world" "beautiful"
```

Shorthand syntax:
```bash
python main.py "hello [___] world" "beautiful"
```

Screen output:
```text
hello world
```
*Note: The word "beautiful" has been embedded into the square bracket placeholder in an invisible format without occupying visual display space.*

If the original text does not contain the `[___]` placeholder, the tool automatically appends the hidden word to the end of the text:
```bash
python main.py merge "hello" "world"
```
Screen output remains:
```text
hello
```

### 2. Reveal Hidden Words in Text (Reveal)

Use the `reveal` command and pass the text string containing the hidden characters (obtained from the previous merge command) to extract the secret message.

Full syntax:
```bash
python main.py reveal "hello world"
```

Shorthand syntax:
```bash
python main.py "hello world"
```

Screen output:
```text
beautiful
```

Supported placeholder formats for identifying the hidden position during merging include:
* `[___]` or `[hidden]`
* `<hidden>text</hidden>`
* `{hidden}`

### 3. Using the zw.cmd Batch File on Windows

If you use Windows Command Prompt (CMD), you can use the bundled `zw.cmd` file for shorter commands. Run commands directly from the project directory:

```cmd
zw "hello [___] world" "beautiful"
zw "hello world"
zw merge "hello [___] world" "awesome"
zw reveal "hello world"
```

To use the tool from any directory on your computer, copy the `zw.cmd` file along with `main.py` into a permanent folder and add that folder path to your Windows PATH environment variable.

## Security Notices and Source Code Inspection

### False Positive Virus Warning
Embedding invisible Unicode (Zero-Width) characters can sometimes trigger false positives in security software like Windows Defender, flagging it as hidden malware. You can use this tool with total confidence based on the following factors:

* The entire source code is written in pure Python text (`.py`), allowing you to inspect every line of logic directly.
* The project contains no pre-compiled binary files (`.exe`, `.dll`) or obfuscated code.
* You can execute and fully control the tool's behavior using the official Python interpreter.

### Running from Source Code Instructions
1. Download the entire project folder to your computer.
2. Ensure your computer has Python version 3.6 or higher installed.
3. Open a command line interface in the project directory and execute the commands according to the syntax above.

## License

This project is licensed under the terms of the MIT License - see the `LICENSE_EN` file for details.
