from vtkmodules.all import *

# Callback class definition
class vtkMyCallback(object):
    def __init__(self, renderer):
        self.ren = renderer

    def __call__(self, caller, event_id):
        # Print the type of event and the camera position
        print(caller.GetClassName(), 'Event Id:', event_id)
        print("Camera Position: %f, %f, %f" % (
            self.ren.GetActiveCamera().GetPosition()[0],
            self.ren.GetActiveCamera().GetPosition()[1],
            self.ren.GetActiveCamera().GetPosition()[2]
        ))

def main():
    # Create a cone source
    coneSource = vtkConeSource()

    # Create a mapper and connect it to the cone source
    coneMapper = vtkPolyDataMapper()
    coneMapper.SetInputConnection(coneSource.GetOutputPort())

    # Create an actor and set its mapper
    coneActor = vtkActor()
    coneActor.SetMapper(coneMapper)

    # Create a renderer and add the actor
    ren = vtkRenderer()
    ren.AddActor(coneActor)
    ren.SetBackground(1.0, 0.55, 0.41)

    # Create a render window
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren)
    renWin.SetSize(640, 480)
    renWin.SetWindowName('Cone')

    # Create a render window interactor
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    # Add the callback observer
    mo1 = vtkMyCallback(ren)
    #renWin.AddObserver(vtkCommand.StartEvent, mo1)
    #renWin.AddObserver(vtkCommand.EndEvent, mo1)
    #renWin.AddObserver(vtkCommand.ResetCameraEvent, mo1)
    renWin.AddObserver(vtkCommand.ModifiedEvent, mo1)

    # Start interaction
    iren.Initialize()
    iren.Start()

if __name__ == '__main__':
    main()
