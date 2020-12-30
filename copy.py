import os
import shutil

for dirpath, dirnames, filenames in os.walk('mrlEyes_2018_01'):  # soruce path
    for filename in filenames:
        if filename.endswith("1", 15,
                             17):  # select file that its name end with (0) between index 15 and 17, for example (
            # s0003_00003_0_0_0_0_0_01.png)
            src = os.path.join(dirpath, filename)
            dest = os.path.join('Open', filename)  # destination path
            shutil.copy2(src, dest)
