import ctypes
import sys, os

def getpids():
    import psutil
    pids = []
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name'])
            if "python" in pinfo['name']:
                pids.append(pinfo['pid'])
        except:
            pass
    return pids

def injectdll(pid, dll):
    os.system(f'Injector.exe -p {pid} -i {dll} >nul 2>&1')

    
