###############################################################################
#       						Poligonal.py
###############################################################################

# Import all VTK modules
from vtkmodules.all import *


def main():

    # tetra
    coords = [[0, 0, 0], [1, 0, 0], [0.5, 1, 0], [0.5, 0.5, 1]]
    vect = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 1]]
    vals = [0.1, 0.3, 0.5, 0.8]
    aTetra = [0, 1, 2, 3]

    #################################
    # VTKUnstructuredGrid Definition
    Ugrid = vtkUnstructuredGrid()
    points = vtkPoints()

    # Vertex
    for i in range(len(coords)):
        points.InsertPoint(i, coords[i])

    Ugrid.InsertNextCell(VTK_VERTEX, 4, aTetra)
    Ugrid.SetPoints(points)

    coneSource = vtkConeSource()
    coneSource.SetHeight(0.2)
    coneSource.SetRadius(0.12)
    coneSource.SetResolution(6)

    arr = vtkFloatArray()
    arr.SetNumberOfComponents(3)

    scalar = vtkFloatArray()

    # Vertex
    for i in range(len(vect)):
        arr.InsertTuple3(i, *vect[i])
        scalar.InsertNextValue(vals[i])

    Ugrid.GetPointData().SetScalars(scalar)
    Ugrid.GetPointData().SetVectors(arr)

    glyph3D = vtkHedgeHog()
    # Align the cones with the normals, without this line the cones will be aligned with the x-axis
    glyph3D.SetInputData(Ugrid)
    glyph3D.SetVectorModeToUseVector()
    glyph3D.SetInputData(Ugrid)
    glyph3D.Update()

    # Mapper and actor
    glyphMapper = vtkDataSetMapper()
    glyphMapper.SetInputConnection(glyph3D.GetOutputPort())

    glyphActor = vtkActor()
    glyphActor.SetMapper(glyphMapper)

    # Creation of renderer, render window, and interactor.
    ren1 = vtkRenderer()
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren1)

    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    ren1.AddActor(glyphActor)
    ren1.SetBackground(1.0, 0.55, 0.41)

    # render
    renWin.Render()

    # Start of interaction
    iren.Start()


if __name__ == '__main__':
    main()
