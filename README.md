# Saturn Backup Memory Padder
** Backup your save data before use **<br><br>
Expand and Contract Sega Saturn Internal Memory image file: 32kb <-> 64kb by adding or removing the alternating '0xFF' bytes.

### Saturn_Backup_Memory_Padder_gui.py

![GUI](https://github.com/kevh182/Saturn_Memory_Padder/blob/main/screenshots/Saturn_Backup_Memory_Padder_gui.png)

### Saturn_Backup_Memory_Padder.py (Command Line)

Usage:<br>
Expand 32kb to 64kb:<br>
``python Saturn_Backup_Memory_Padder.py --expand <input_file> <output_file>``<br>

Contract 64kb to 32kb:<br>
``python Saturn_Backup_Memory_Padder.py --contract <input_file> <output_file>``<br>

### 32kb unpadded save file.
![32kb unpadded](https://github.com/kevh182/Saturn_Memory_Padder/blob/main/screenshots/Saturn_Backup_Memory_Padder_32kb.png)

### 64kb 0xFF 'byte-expanded' padded file (MiSTer (.sav) format)
![64kb expanded](https://github.com/kevh182/Saturn_Memory_Padder/blob/main/screenshots/Saturn_Backup_Memory_Padder_64kb.png)
