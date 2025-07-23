# Linux Command Line Cheat Sheet

Below is a summary of the Linux commands covered in the tutorial video, organized by category. Each command is listed with a short, practical description.

---

## System Information

| Command             | Description                                                         |
|---------------------|---------------------------------------------------------------------|
| `uname`             | Shows the system's kernel name (e.g., Linux).                       |
| `uname -a`          | Shows all system info (kernel, version, architecture, etc.).        |
| `mount`             | Lists mounted filesystems/devices or mounts a device.               |
| `whoami`            | Displays the current username.                                      |
| `ifconfig`          | Shows network interface settings and IP addresses.                  |
| `date`              | Displays or sets the system date and time.                          |
| `uptime`            | Shows how long the system has been running.                         |
| `man [command]`     | Opens the manual page for the specified command.                    |

---

## Navigation & Display

| Command                  | Description                                                   |
|--------------------------|--------------------------------------------------------------|
| `pwd`                    | Prints the current working directory.                        |
| `ls`                     | Lists files/directories in the current directory.            |
| `ls -a`                  | Lists all files, including hidden ones.                      |
| `ls -la`                 | Long list, shows permissions, owner, size, and dates.        |
| `ls -R`                  | Lists files/directories recursively.                         |
| `ls -r`                  | Lists files in reverse order.                                |
| `ls -t`                  | Sorts files by modification time.                            |
| `ls -S`                  | Sorts files by size.                                         |
| `ls -1`                  | Lists one file per line.                                     |
| `cd [directory]`         | Changes to the specified directory.                          |
| `cd ..`                  | Goes up one directory level.                                 |
| `cd ../..`               | Goes up two directory levels.                                |
| `clear`                  | Clears the terminal screen.                                  |
| `tree`                   | Visualizes directory structure as a tree.                    |
| `echo [text/variable]`   | Prints text or variable value to the terminal.               |

---

## File & Directory Management

| Command                                 | Description                                      |
|------------------------------------------|--------------------------------------------------|
| `mkdir [directory_name]`                 | Creates a new directory.                         |
| `touch [file_name]`                      | Creates an empty file or updates timestamp.      |
| `cat [file_name]`                        | Displays content of a file.                      |
| `echo "[text]" > [file_name]`            | Writes text to a file (overwrites existing).     |
| `nano [file_name]`                       | Opens a file in Nano text editor.                |
| `cp [src] [dest]`                        | Copies a file to another location.               |
| `mv [src] [dest]`                        | Moves or renames a file.                         |
| `rm [file_name]`                         | Removes (deletes) a file.                        |
| `rmdir [directory_name]`                 | Deletes an empty directory.                      |
| `head [file_name]`                       | Shows first 10 lines of a file.                  |
| `tail [file_name]`                       | Shows last 10 lines of a file.                   |
| `head -n [num] [file_name]`              | Shows first n lines of a file.                   |
| `tail -n [num] [file_name]`              | Shows last n lines of a file.                    |

---

## Finding Files & Searching Content

| Command                                               | Description                                               |
|-------------------------------------------------------|-----------------------------------------------------------|
| `find [path] -name "[pattern]"`                       | Finds files by name. Supports wildcards.                  |
| `2>/dev/null`                                         | Suppresses error messages.                                |
| `find [path] -user [username]`                        | Finds files owned by a user.                              |
| `find [path] -perm [permissions]`                     | Finds files with specific permissions.                    |
| `find [path] -type f`                                 | Finds only files.                                         |
| `find [path] -type d`                                 | Finds only directories.                                   |
| `find [path] -mmin -[minutes]`                        | Finds files modified within n minutes.                    |
| `grep "[pattern]" [file_name]`                        | Searches for a pattern in a file.                         |
| `cat [file_name] | grep "[pattern]"`                  | Pipes output of cat to grep for searching.                |
| `grep -n "[pattern]" [file_name]`                     | Shows line numbers where pattern is found.                |
| `grep -c "[pattern]" [file_name]`                     | Counts lines matching the pattern.                        |
| `locate [pattern]`                                    | Finds files quickly using a system index.                 |
| `Ctrl+C`                                              | Stops a running command.                                  |

---

## User & Group Management

| Command                                   | Description                                                  |
|--------------------------------------------|--------------------------------------------------------------|
| `cat /etc/passwd`                         | Lists all users on the system.                               |
| `chmod [permissions] [file/directory]`     | Changes file/directory permissions.                          |
| `chmod +x/-x/u+x/g+x [file]`               | Adds/removes execute permissions for user/group.             |
| `sudo useradd [username]`                  | Adds a new user (may require sudo/root).                     |
| `passwd [username]`                        | Sets/changes a user's password.                              |
| `passwd -e [username]`                     | Expires a user's password (forces reset at next login).      |
| `userdel [username]`                       | Deletes a user.                                              |
| `usermod -aG [groupname] [username]`       | Adds user to a supplementary group.                          |
| `usermod -g [groupname] [username]`        | Changes user's primary group.                                |
| `groupadd [groupname]`                     | Creates a new group.                                         |
| `groupdel [groupname]`                     | Deletes a group.                                             |
| `groups [username]`                        | Shows groups for a user.                                     |
| `cat /etc/group`                           | Lists all groups.                                            |
| `getent group [groupname]`                 | Info about a group and its members.                          |
| `gpasswd -a [username] [groupname]`        | Adds user to group (alternative to usermod).                 |
| `chown [user:group] [file/directory]`      | Changes owner/group of a file or directory.                  |
| `chown :[groupname] [directory]`           | Changes group ownership of a directory.                      |

---

## Workflow Example

**Typical steps to create a shared group directory:**
1. Add user: `sudo useradd username`
2. Set/expire password: `passwd username`, `passwd -e username`
3. Create group: `groupadd groupname`
4. Add user to group: `usermod -aG groupname username`
5. Create directory: `mkdir /shared`
6. Change group ownership: `chown :groupname /shared`
7. Set permissions: `chmod g+rw /shared`

---

## Fun Fact

Did you know?  
The `tree` command is not always installed by default on Linux, but it's a favorite for visualizing directory structures—just run `sudo apt install tree` on Ubuntu to get it.

---

*Watch the full tutorial here: [Linux Command Line Crash Course](https://youtu.be/fwGqm8T9drI?si=yc4Sn0OJMA-uYlam)*

