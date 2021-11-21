from direct.showbase import Audio3DManager
from random import  choice
from random import shuffle
class audio3d():
    def __init__(self):
        self.audio3d = Audio3DManager.Audio3DManager(base.sfxManagerList[0], camera)
        self.sfx3d = {
            'portal_loop': [
                self.audio3d.loadSfx('audio/portal_loop.wav'),
                self.audio3d.loadSfx('audio/portal_loop01.wav'),
                self.audio3d.loadSfx('audio/portal_loop02.wav'),
                self.audio3d.loadSfx('audio/portal_loop03.wav'),
                self.audio3d.loadSfx('audio/portal_loop04.wav'),
                self.audio3d.loadSfx('audio/portal_loop05.wav'),
                self.audio3d.loadSfx('audio/portal_loop.06wav'),
            ]
        }
        self.audio3d.setDistanceFactor(1)
        
    def enter(self):
        base.task_mgr.add(self.update, 'update')
    def playSfx(self, sfx = None, obj = None, loop = False):
        if sfx == None:
            print("No sfx provided...")
        else:
            if obj == None:
                print("No object provide to attach with a sound.")
            else:
                if self.sfx3d.get(sfx):
                    list_copy =  self.sfx3d.get(sfx)
                    shuffle(list_copy)
                    sfx3d = list_copy.pop()
                    print(loop)
                    sfx3d.setLoop(loop)
                    sfx3d.setVolume(5)
                    sfx3d.play()
                    print(str(sfx3d))
                    self.audio3d.attachSoundToObject(sfx3d, obj)
                    self.audio3d.setSoundMinDistance(sfx3d, 1)
                    self.audio3d.setSoundMaxDistance(sfx3d, 50)
                    
                    print("Attached sound to object.")
                    print(str(obj))
                    
    
    def update(self, task):
        self.audio3d.update()
        #print(str(self.audio3d.getListenerVelocity()))
        return task.cont