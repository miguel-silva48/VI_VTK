# Import all VTK modules
from vtkmodules.all import *

# Function to choose the shape to display
def create_shape(shape_type):
    if shape_type == 'cone' or shape_type == '1':
        shape_name = 'Cone'
        shape_source = vtkConeSource()
        shape_source.SetHeight(2.0) # If increased, without modifying the radius, the cone becomes taller ("stretched")
        shape_source.SetRadius(1.0)
        shape_source.SetResolution(100) # Increases the polygons of the cone (more detail)

    elif shape_type == 'cylinder' or shape_type == '2':
        shape_name = 'Cylinder'
        shape_source = vtkCylinderSource()
        shape_source.SetHeight(3.0)
        shape_source.SetRadius(2.0)
        #shape_source.SetResolution(1) # This way it becomes a triangular prism
        shape_source.SetResolution(100) # Changes the "roundness" of the cylinder

    elif shape_type == 'sphere' or shape_type == '3':
        shape_name = 'Sphere'
        shape_source = vtkSphereSource()
        shape_source.SetRadius(2.0)
        # Here there are 2 resolutions theta and phi
        # Theta is the resolution around the z-axis
        # Phi is the resolution around the y-axis
        # It was set to 10 and 500 to see the difference better
        shape_source.SetThetaResolution(10) 
        shape_source.SetPhiResolution(500)

    elif shape_type == 'cube' or shape_type == '4':
        shape_name = 'Cube'
        shape_source = vtkCubeSource()
        shape_source.SetXLength(2.0)
        shape_source.SetYLength(2.0)
        shape_source.SetZLength(2.0)

    else:
        raise ValueError("Unknown shape type")
    
    return shape_source, shape_name

def main(shape_type):
    shape_source, shape_name = create_shape(shape_type)

    shape_mapper = vtkPolyDataMapper()
    shape_mapper.SetInputConnection(shape_source.GetOutputPort())

    shape_actor = vtkActor()
    shape_actor.SetMapper(shape_mapper)
    #shape_actor.GetProperty().SetColor(0.2, 0.63, 0.79) # Blue color (given code)
    shape_actor.GetProperty().SetColor(0.79, 0.2, 0.2) # Actual Red color
    """Actor representation options:"""
    #shape_actor.GetProperty().SetRepresentationToPoints() # Points - figure lines are dotted
    #shape_actor.GetProperty().SetRepresentationToWireframe() # Wireframe  - only the edges of the figure are shown
    #shape_actor.GetProperty().SetRepresentationToSurface() # Surfaces - the figure is shown as a solid (default)

    # Transparency - 0.0 is completely transparent and 1.0 is completely opaque
    shape_actor.GetProperty().SetOpacity(0.5) # 0.5 is translucid

    ren = vtkRenderer()
    ren.AddActor(shape_actor)
    ren.SetBackground(0.2, 0.2, 0.2)

    renWin = vtkRenderWindow()
    renWin.SetSize(500, 500)  # Default size is 300x300 (left bigger to see better)
    renWin.AddRenderer(ren)
    renWin.SetWindowName(shape_name)

    # Adds a render window interactor to the figure
    # Enables user interaction (e.g. to rotate the scene)
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)
    iren.Initialize()
    iren.Start()
    """VTK Key effects on interaction:"""
    # MLB - Rotates the 3D image
    # RMB - Zooms in and out (there is a hidden slider that can be used to zoom in and out in any part of the screen)
    # ScrollWheel - Zooms in and out
    # F - Erratic and uncontrollable behavior once it kicks in but seems to go to a certain aimed spot
    # P - Allows to pick an object (cube appears around the selected object)
    # R - Resets zoom
    # S - Enables surfaces mode (opposite of wireframe)
    # W - Enables wireframe mode (opposite of surfaces)
    # J/T - Don't seem to work
    # E/Q - Closes the window

if __name__ == '__main__':
    shape_type = input("Enter the shape to display (1-cone, 2-cylinder, 3-sphere, 4-cube): ").strip().lower()
    main(shape_type)