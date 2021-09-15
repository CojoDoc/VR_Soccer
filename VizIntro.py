import viz

#Enable full screen anti-aliasing (FSAA) to smooth edges
viz.setMultiSample(4)

viz.go()

#Increase the Field of View
viz.MainWindow.fov(60)

#Add assets
stadium = viz.addChild('stadium1.fbx')

ball = viz.addChild('ball.fbx')

#change view point of scenary 
viz.MainView.move([0,0,80])

#Add avatar
male = viz.addAvatar('vcc_male.cfg')
male.setPosition([0, 0, 85])
male.setEuler([0,0,0])

#Add avatar animation
def walkAvatars():

    walk2 = vizact.walkTo([0,0,95])
    male.addAction(walk2)

vizact.onkeydown('w',walkAvatars)

