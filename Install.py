import subprocess

try:
    cmd = 'python -m pip install --disable-pip-version-check -r requirements.txt'
    subprocess.run(cmd.split())
    print('Installation finished!')
except:
    print('Installation failed, please follow the README for setting up a virtual environment')
