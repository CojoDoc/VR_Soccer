import viz

#Enable full screen anti-aliasing (FSAA) to smooth edges
viz.setMultiSample(4)

viz.go()

#Increase the Field of View
viz.MainWindow.fov(60)

stadium = viz.addChild('stadium1.fbx')

ball = viz.addChild('ball.fbx')

viz.MainView.move([0,0,80])


