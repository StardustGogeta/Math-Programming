import subprocess

def cpp_open(fp='C:/Users/Gerst/Documents/GitHub/Math-Programming/Python/ProbabilitySim/CF.exe ',args= '1 2 15000'):
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    p = subprocess.Popen(fp+args, startupinfo=startupinfo,stdout=subprocess.PIPE)
    stdout, stderr = p.communicate()
    return stdout.split()[1].decode()

print(cpp_open())
