from vtkmodules.all import *

# Create the sphere
sphereSource = vtkSphereSource()
sphereSource.SetRadius(1.0)
sphereSource.SetThetaResolution(8)  # Sets the number of cones around the longitudinal axis (y-axis)
sphereSource.SetPhiResolution(8)    # Sets the number of cones around the latitudinal axis (x-axis)
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
glyph3D.SetVectorModeToUseNormal()  # Align the cones with the normals, without this line the cones will be aligned with the x-axis
glyph3D.SetScaleFactor(2)           # Adjust the size of the cones

# Mapper and actor for the cones (glyphs)
glyphMapper = vtkPolyDataMapper()
glyphMapper.SetInputConnection(glyph3D.GetOutputPort())

glyphActor = vtkActor()
glyphActor.SetMapper(glyphMapper)

# Mapper and actor for the solid sphere
sphereMapper = vtkPolyDataMapper()
sphereMapper.SetInputConnection(sphereSource.GetOutputPort())

sphereActor = vtkActor()
sphereActor.SetMapper(sphereMapper)
sphereActor.GetProperty().SetColor(1.0, 1.0, 1.0)  # White color for the sphere

# Renderer, render window, and interactor
renderer = vtkRenderer()
renderWindow = vtkRenderWindow()
renderWindow.AddRenderer(renderer)

renderWindowInteractor = vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)

# Add the actors to the renderer
renderer.AddActor(sphereActor)      # Solid sphere
renderer.AddActor(glyphActor)       # Cones
renderer.SetBackground(0, 0, 0)     # Black background

# Render and start interaction
renderWindow.Render()
renderWindowInteractor.Start()
