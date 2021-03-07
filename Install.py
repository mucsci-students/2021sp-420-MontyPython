import subprocess

cmd = 'python -m pip install --disable-pip-version-check -r requirements.txt'
subprocess.run(cmd.split())
print('Installation finished!')
