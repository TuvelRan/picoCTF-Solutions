## Description
Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it, and then `ls` once connected to begin. Login via `ssh` as `ctf-player` with the password, `481e7b14`

## Solution
- First of all, run the instance they're giving you and ssh into it.

Now, use the command `ls` to list all of the files at your current working directory, which you can print with `pwd`.
You will find a file starting with "1of3...txt", open that file and copy its content to a text editor.
After that, follow the instructions which are leading to the root directory (`\`). In there, you will find the second file "2of3...txt", copy its content and do the same thing with the file in the home folder.

That's it, you captured the flag (:

#### picoCTF{xxsh_0ut_0f_\/\/4t3r_1118a9a4}
