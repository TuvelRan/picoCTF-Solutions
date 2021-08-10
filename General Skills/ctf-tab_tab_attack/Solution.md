## CTF Description
Using tabcomplete in the Terminal will add years to your life, esp. when dealing with long rambling directory structures and filenames: [Addadshashanammu.zip](https://mercury.picoctf.net/static/e38f6a5b69b45d21e33cf7281d8c2531/Addadshashanammu.zip)

## Solution
Using the Terminal:
```
wget https://mercury.picoctf.net/static/e38f6a5b69b45d21e33cf7281d8c2531/Addadshashanammu.zip
unzip Addadshashanammu.zip
```
Changing the directory to /Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/, you will find an ELF file. I tried getting the strings from the file itself using the strings command.
```
strings fang-of-haynekhtnamet
```
In there, you will find the flag.

#### picoCTF{l3v3l_up!_t4k3_4_r35t!_f3553887}
