# Setup and Run the C++ OOP Examples

The course uses standard C++17. You need a compiler such as GCC (g++) or Clang, or a C++ toolchain supplied by an IDE.

## Windows with MinGW g++

1. Install a working MinGW-w64/GCC toolchain and ensure g++ is on PATH.
2. Open PowerShell in the folder containing main.cpp.
3. Compile:
```powershell
g++ -std=c++17 -Wall -Wextra -pedantic main.cpp -o main.exe
```
4. Run:
```powershell
.\main.exe
```

If PowerShell says g++ is not recognized, the compiler is not installed or its bin directory is not on PATH. Restart the terminal after changing PATH.

## Linux
```bash
g++ --version
g++ -std=c++17 -Wall -Wextra -pedantic main.cpp -o main
./main
```

## macOS
Install/enable the Apple Command Line Tools and use clang++:
```bash
clang++ --version
clang++ -std=c++17 -Wall -Wextra -pedantic main.cpp -o main
./main
```

## What the flags mean
- -std=c++17 selects the C++17 language standard used by these notes.
- -Wall and -Wextra enable useful compiler warnings.
- -pedantic asks for diagnostics on some non-standard language extensions.
- -o names the output executable.

## Multiple source files
If a lesson has main.cpp plus Student.cpp, compile both files:
```bash
g++ -std=c++17 -Wall -Wextra -pedantic main.cpp Student.cpp -o app
```

## Syntax highlighting
GitHub automatically syntax-highlights Markdown blocks labelled cpp. In VS Code, install/use the built-in C++ language support to colour .cpp files; use Markdown Preview to see the labelled code blocks. A file such as README.md is documentation, not a program to execute directly.
