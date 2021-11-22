import os
import subprocess
import platform

from SetupRequirements import Configuration as Requirements
from SetupPremake import Premake as PremakeRequirements


os.chdir('./../')  # Change from devtools/scripts directory to root
Requirements.Validate()  # Make sure everything we need for the setup is installed

premakeInstalled = PremakeRequirements.Validate()

print("\nUpdating submodules...")
subprocess.call(["git", "submodule", "update", "--init", "--recursive"])

if (premakeInstalled):
    if platform.system() == "Windows":
        print("\nRunning premake...")
        subprocess.call(
            [os.path.abspath("./scripts/Bootstrap.bat"), "nopause"])

    print("\nSetup completed!")
else:
    print("Premake is require to generate project files.")
