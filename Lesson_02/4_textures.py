from vtkmodules.all import *

def main():

    planeSource = vtkPlaneSource()
    planeSource.SetOrigin(2, 8, 0)
    planeSource.SetPoint1(0.5, 0.5, 0.5)
    planeSource.SetPoint2(10.0, 1.0, 1.0)

    # We create an instance of vtkPolyDataMapper to map the polygonal data
    # into graphics primitives. We connect the output of the cone source
    # to the input of this mapper.

    planeMapper = vtkPolyDataMapper()
    planeMapper.SetInputConnection(planeSource.GetOutputPort())

    # We create an actor to represent the cone. The actor orchestrates rendering
    # of the mapper's graphics primitives. An actor also refers to properties
    # via a vtkProperty instance, and includes an internal transformation
    # matrix. We set this actor's mapper to be coneMapper which we created
    # above.

    planeActor = vtkActor()
    planeActor.SetMapper(planeMapper)

    JPGReader = vtkJPEGReader()
    JPGReader.SetFileName("./Lesson_02/images/lena.JPG")
    JPGReader.Update()

    aText = vtkTexture()
    aText.SetInputConnection(JPGReader.GetOutputPort())

    planeActor.SetTexture(aText)

    # Create the Renderer and assign actors to it. A renderer is like a
    # viewport. It is part or all of a window on the screen and it is
    # responsible for drawing the actors it has.  We also set the background
    # color here.
    ren = vtkRenderer()
    # ren.AddActor(coneActor)
    ren.AddActor(planeActor)
    ren.SetBackground(1.0, 0.55, 0.41)

    # Finally we create the render window which will show up on the screen.
    # We put our renderer into the render window using AddRenderer. We also
    # set the size to be 300 pixels by 300.

    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren)

    renWin.SetSize(640, 480)
    renWin.SetWindowName('Lena')

    # Adds a render window interactor to the cone example to
    # enable user interaction (e.g. to rotate the scene)
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)
    iren.Initialize()
    iren.Start()


if __name__ == '__main__':
    main()
