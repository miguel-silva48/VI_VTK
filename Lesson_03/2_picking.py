from vtkmodules.all import *

# Create the main sphere
sphereSource = vtkSphereSource()
sphereSource.SetRadius(1.0)
sphereSource.SetThetaResolution(8)
sphereSource.SetPhiResolution(8)
sphereSource.Update()

# Create a cone (glyph)
coneSource = vtkConeSource()
coneSource.SetHeight(0.2)
coneSource.SetRadius(0.12)
coneSource.SetResolution(6)

# Configure Glyph3D for the cones
glyph3D = vtkGlyph3D()
glyph3D.SetSourceConnection(coneSource.GetOutputPort())
glyph3D.SetInputConnection(sphereSource.GetOutputPort())
glyph3D.SetVectorModeToUseNormal()  # Align the cones with the normals
glyph3D.SetScaleFactor(2)

# Mapper and actor for the cones (glyphs)
glyphMapper = vtkPolyDataMapper()
glyphMapper.SetInputConnection(glyph3D.GetOutputPort())

glyphActor = vtkActor()
glyphActor.SetMapper(glyphMapper)

# Mapper and actor for the main sphere
sphereMapper = vtkPolyDataMapper()
sphereMapper.SetInputConnection(sphereSource.GetOutputPort())

sphereActor = vtkActor()
sphereActor.SetMapper(sphereMapper)
sphereActor.GetProperty().SetColor(1.0, 1.0, 1.0)  # White sphere

# **Indicator Sphere for the Selected Point**
pickSphereSource = vtkSphereSource()
pickSphereSource.SetRadius(0.05)
pickSphereSource.SetThetaResolution(8)
pickSphereSource.SetPhiResolution(8)

pickSphereMapper = vtkPolyDataMapper()
pickSphereMapper.SetInputConnection(pickSphereSource.GetOutputPort())

pickSphereActor = vtkActor()
pickSphereActor.SetMapper(pickSphereMapper)
pickSphereActor.GetProperty().SetColor(1.0, 0, 0)  # Red sphere
pickSphereActor.VisibilityOff()                    # Initially invisible

# Custom callback to show coordinates and move the sphere
class PointPickerCallback:
    def __init__(self, picker, sphere_actor):
        self.picker = picker
        self.sphere_actor = sphere_actor

    def __call__(self, caller, event):
        # Get the position of the selected point
        picked_position = self.picker.GetPickPosition()
        print(f"Picked Point Coordinates: {picked_position}")
        
        # Update the position of the indicator sphere
        self.sphere_actor.SetPosition(picked_position)
        self.sphere_actor.VisibilityOn()

# Renderer, render window, and interactor
renderer = vtkRenderer()
renderWindow = vtkRenderWindow()
renderWindow.AddRenderer(renderer)

renderWindowInteractor = vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)

# **Configure the picker and the callback**
pointPicker = vtkPointPicker()
renderWindowInteractor.SetPicker(pointPicker)

callback = PointPickerCallback(pointPicker, pickSphereActor)
pointPicker.AddObserver(vtkCommand.EndPickEvent, callback)

# Add the actors to the renderer
renderer.AddActor(sphereActor)      # Main sphere
renderer.AddActor(glyphActor)       # Cones
renderer.AddActor(pickSphereActor)  # Indicator sphere for the selected point
renderer.SetBackground(0, 0, 0)     # Black background

# Render and start interaction
renderWindow.Render()
renderWindowInteractor.Start()