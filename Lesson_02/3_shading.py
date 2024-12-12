from vtkmodules.all import *

def main():

    sphereSource = vtkSphereSource()
    sphereSource.SetThetaResolution(10)
    sphereSource.SetPhiResolution(10)

    sphereSource2 = vtkSphereSource()
    sphereSource2.SetThetaResolution(10)
    sphereSource2.SetPhiResolution(10)

    # We create an instance of vtkPolyDataMapper to map the polygonal data
    # into graphics primitives. We connect the output of the cone source
    # to the input of this mapper.

    sphereMapper = vtkPolyDataMapper()
    sphereMapper.SetInputConnection(sphereSource.GetOutputPort())

    sphereMapper2 = vtkPolyDataMapper()
    sphereMapper2.SetInputConnection(sphereSource2.GetOutputPort())

    # We create an actor to represent the cone. The actor orchestrates rendering
    # of the mapper's graphics primitives. An actor also refers to properties
    # via a vtkProperty instance, and includes an internal transformation
    # matrix. We set this actor's mapper to be coneMapper which we created
    # above.

    sphereActor = vtkActor()
    sphereActor.SetMapper(sphereMapper)
    sphereActor.GetProperty().SetInterpolationToFlat()

    sphereActor2 = vtkActor()
    sphereActor2.SetMapper(sphereMapper2)
    #sphereActor2.GetProperty().SetInterpolationToGouraud()
    sphereActor2.GetProperty().SetInterpolationToPhong()

    # Create the Renderer and assign actors to it. A renderer is like a
    # viewport. It is part or all of a window on the screen and it is
    # responsible for drawing the actors it has.  We also set the background
    # color here.
    ren = vtkRenderer()
    ren.AddActor(sphereActor)
    ren.SetBackground(0.1, 0.2, 0.4)
    ren.SetViewport(0, 0, 0.5, 1)

    ren2 = vtkRenderer()
    ren2.AddActor(sphereActor2)
    ren2.SetBackground(0.2, 0.3, 0.4)
    ren2.SetViewport(0.5, 0, 1, 1)

    camera = ren2.GetActiveCamera()
    camera.SetPosition(0, 0, 10)
    camera.SetViewUp(0, 0, 0)
    camera.Azimuth(-90)

    # Finally we create the render window which will show up on the screen.
    # We put our renderer into the render window using AddRenderer. We also
    # set the size to be 300 pixels by 300.
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren)
    renWin.AddRenderer(ren2)
    renWin.SetSize(600, 300)
    renWin.SetWindowName('Spheres')

    # Adds a render window interactor to the cone example to
    # enable user interaction (e.g. to rotate the scene)
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)
    iren.Initialize()
    iren.Start()


if __name__ == '__main__':
    main()
