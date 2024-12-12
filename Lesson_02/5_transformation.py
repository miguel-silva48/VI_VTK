from vtkmodules.all import *

def create_textured_plane(image_file, translation, rotation):
    # Plane source
    planeSource = vtkPlaneSource()

    # Texture reader
    JPGReader = vtkJPEGReader()
    JPGReader.SetFileName(image_file)
    JPGReader.Update()

    # Texture
    aText = vtkTexture()
    aText.SetInputConnection(JPGReader.GetOutputPort())

    # Transformation
    MyTransform = vtkTransform()
    MyTransform.Translate(*translation)
    MyTransform.RotateX(rotation[0])
    MyTransform.RotateY(rotation[1])
    MyTransform.RotateZ(rotation[2])

    # Apply transformation filter
    MyFilter = vtkTransformPolyDataFilter()
    MyFilter.SetTransform(MyTransform)
    MyFilter.SetInputConnection(planeSource.GetOutputPort())

    # Mapper
    planeMapper = vtkPolyDataMapper()
    planeMapper.SetInputConnection(MyFilter.GetOutputPort())

    # Actor
    planeActor = vtkActor()
    planeActor.SetMapper(planeMapper)
    planeActor.SetTexture(aText)

    return planeActor


def main():
    # Renderer
    ren = vtkRenderer()

    # Define the transformations for each face
    transformations = [
        ("./Lesson_02/images/Im1.jpg", [0, 0, 0.5], [0, 0, 0]),        # Front
        ("./Lesson_02/images/Im2.jpg", [0, 0, -0.5], [0, 180, 0]),     # Back
        ("./Lesson_02/images/Im3.jpg", [0, 0.5, 0], [-90, 0, 0]),      # Top
        ("./Lesson_02/images/Im4.jpg", [0, -0.5, 0], [90, 0, 0]),      # Bottom
        ("./Lesson_02/images/Im5.jpg", [-0.5, 0, 0], [0, -90, 0]),     # Left
        ("./Lesson_02/images/Im6.jpg", [0.5, 0, 0], [0, 90, 0]),       # Right
    ]

    # Create and add each face
    for image_file, translation, rotation in transformations:
        planeActor = create_textured_plane(image_file, translation, rotation)
        ren.AddActor(planeActor)

    # Set background and window
    ren.SetBackground(0.1, 0.1, 0.1)

    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren)
    renWin.SetSize(640, 480)
    renWin.SetWindowName('Textured Cube')

    # Interactor
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)
    iren.Initialize()
    iren.Start()


if __name__ == '__main__':
    main()
