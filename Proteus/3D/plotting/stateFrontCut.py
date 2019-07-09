# state file generated using paraview version 5.4.1

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [3388, 1777]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [1.0, 0.0, 1.3499999642372131]
renderView1.StereoType = 0
renderView1.CameraPosition = [4.392207600387027, -2.4695835894957705, 2.1753079758235785]
renderView1.CameraFocalPoint = [1.0, 0.0, 1.3499999642372131]
renderView1.CameraViewUp = [-0.14833193106462003, 0.12413042988421602, 0.9811163410133381]
renderView1.CameraParallelScale = 1.1067971770199379
renderView1.Background = [1.0, 1.0, 1.0]

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'Outline'
#outline1 = Outline()
#outline1.Bounds = [0.0, 20.0, -0.15, 0.15, 0.45, 0.9]
from paraview import simple
creator = simple._create_func("Outline", simple.servermanager.sources)
outline1 = creator(guiName="outline1", Bounds=[0.0, 20.0, -0.15, 0.15, 0.45, 0.9])

# create a new 'Box'
box1 = Box()
box1.XLength = 20.0
box1.YLength = 0.15
box1.ZLength = 0.05
box1.Center = [10.0, 0.075, 0.475]

# create a new 'XDMF Reader'
gaussian_3D_completexmf = XDMFReader(FileNames=['./gaussian_3D_complete.xmf'])
gaussian_3D_completexmf.PointArrayStatus = ['nodeMaterialTypes', 'p', 'pInc', 'pInit', 'phi', 'phi_s0', 'quantDOFs_for_clsvof0', 'quantDOFs_for_rans3p_p0', 'u', 'v', 'velocity', 'vof0', 'w']
gaussian_3D_completexmf.CellArrayStatus = ['elementMaterialTypes']
gaussian_3D_completexmf.GridStatus = ['Grid_2', 'Grid_5', 'Grid_8', 'Grid_11', 'Grid_14', 'Grid_17', 'Grid_20', 'Grid_23', 'Grid_26', 'Grid_29', 'Grid_32', 'Grid_35', 'Grid_38', 'Grid_41', 'Grid_44', 'Grid_47', 'Grid_50', 'Grid_53', 'Grid_56', 'Grid_59', 'Grid_62', 'Grid_65', 'Grid_68', 'Grid_71', 'Grid_74', 'Grid_77', 'Grid_80', 'Grid_83', 'Grid_86', 'Grid_89', 'Grid_92', 'Grid_95', 'Grid_98', 'Grid_101', 'Grid_104', 'Grid_107', 'Grid_110', 'Grid_113', 'Grid_116', 'Grid_119', 'Grid_122', 'Grid_125', 'Grid_128', 'Grid_131', 'Grid_134', 'Grid_137', 'Grid_140', 'Grid_143', 'Grid_146', 'Grid_149', 'Grid_152', 'Grid_155', 'Grid_158', 'Grid_161', 'Grid_164', 'Grid_167', 'Grid_170', 'Grid_173', 'Grid_176', 'Grid_179', 'Grid_182', 'Grid_185', 'Grid_188', 'Grid_191', 'Grid_194', 'Grid_197', 'Grid_200', 'Grid_203', 'Grid_206', 'Grid_209', 'Grid_212', 'Grid_215', 'Grid_218', 'Grid_221', 'Grid_224', 'Grid_227', 'Grid_230', 'Grid_233', 'Grid_236', 'Grid_239', 'Grid_242', 'Grid_245', 'Grid_248', 'Grid_251', 'Grid_254', 'Grid_257', 'Grid_260', 'Grid_263', 'Grid_266', 'Grid_269', 'Grid_272', 'Grid_c0p2_Lagrange', 'Grid_c0p2_Lagrange[1]', 'Grid_c0p2_Lagrange[2]', 'Grid_c0p2_Lagrange[3]', 'Grid_c0p2_Lagrange[4]', 'Grid_c0p2_Lagrange[5]', 'Grid_c0p2_Lagrange[6]', 'Grid_c0p2_Lagrange[7]', 'Grid_c0p2_Lagrange[8]', 'Grid_c0p2_Lagrange[9]', 'Grid_c0p2_Lagrange[10]', 'Grid_c0p2_Lagrange[11]', 'Grid_c0p2_Lagrange[12]', 'Grid_c0p2_Lagrange[13]', 'Grid_c0p2_Lagrange[14]', 'Grid_c0p2_Lagrange[15]', 'Grid_c0p2_Lagrange[16]', 'Grid_c0p2_Lagrange[17]', 'Grid_c0p2_Lagrange[18]', 'Grid_c0p2_Lagrange[19]', 'Grid_c0p2_Lagrange[20]', 'Grid_c0p2_Lagrange[21]', 'Grid_c0p2_Lagrange[22]', 'Grid_c0p2_Lagrange[23]', 'Grid_c0p2_Lagrange[24]', 'Grid_c0p2_Lagrange[25]', 'Grid_c0p2_Lagrange[26]', 'Grid_c0p2_Lagrange[27]', 'Grid_c0p2_Lagrange[28]', 'Grid_c0p2_Lagrange[29]', 'Grid_c0p2_Lagrange[30]', 'Grid_c0p2_Lagrange[31]', 'Grid_c0p2_Lagrange[32]', 'Grid_c0p2_Lagrange[33]', 'Grid_c0p2_Lagrange[34]', 'Grid_c0p2_Lagrange[35]', 'Grid_c0p2_Lagrange[36]', 'Grid_c0p2_Lagrange[37]', 'Grid_c0p2_Lagrange[38]', 'Grid_c0p2_Lagrange[39]', 'Grid_c0p2_Lagrange[40]', 'Grid_c0p2_Lagrange[41]', 'Grid_c0p2_Lagrange[42]', 'Grid_c0p2_Lagrange[43]', 'Grid_c0p2_Lagrange[44]', 'Grid_c0p2_Lagrange[45]', 'Grid_c0p2_Lagrange[46]', 'Grid_c0p2_Lagrange[47]', 'Grid_c0p2_Lagrange[48]', 'Grid_c0p2_Lagrange[49]', 'Grid_c0p2_Lagrange[50]', 'Grid_c0p2_Lagrange[51]', 'Grid_c0p2_Lagrange[52]', 'Grid_c0p2_Lagrange[53]', 'Grid_c0p2_Lagrange[54]', 'Grid_c0p2_Lagrange[55]', 'Grid_c0p2_Lagrange[56]', 'Grid_c0p2_Lagrange[57]', 'Grid_c0p2_Lagrange[58]', 'Grid_c0p2_Lagrange[59]', 'Grid_c0p2_Lagrange[60]', 'Grid_c0p2_Lagrange[61]', 'Grid_c0p2_Lagrange[62]', 'Grid_c0p2_Lagrange[63]', 'Grid_c0p2_Lagrange[64]', 'Grid_c0p2_Lagrange[65]', 'Grid_c0p2_Lagrange[66]', 'Grid_c0p2_Lagrange[67]', 'Grid_c0p2_Lagrange[68]', 'Grid_c0p2_Lagrange[69]', 'Grid_c0p2_Lagrange[70]', 'Grid_c0p2_Lagrange[71]', 'Grid_c0p2_Lagrange[72]', 'Grid_c0p2_Lagrange[73]', 'Grid_c0p2_Lagrange[74]', 'Grid_c0p2_Lagrange[75]', 'Grid_c0p2_Lagrange[76]', 'Grid_c0p2_Lagrange[77]', 'Grid_c0p2_Lagrange[78]', 'Grid_c0p2_Lagrange[79]', 'Grid_c0p2_Lagrange[80]', 'Grid_c0p2_Lagrange[81]', 'Grid_c0p2_Lagrange[82]', 'Grid_c0p2_Lagrange[83]', 'Grid_c0p2_Lagrange[84]', 'Grid_c0p2_Lagrange[85]', 'Grid_c0p2_Lagrange[86]', 'Grid_c0p2_Lagrange[87]', 'Grid_c0p2_Lagrange[88]', 'Grid_c0p2_Lagrange[89]', 'Grid_c0p2_Lagrange[90]', 'Grid_c0p2_Lagrange[91]']

### FIX STATE IN PARAVIEW: provide final_time ###
final_time=18
num_frames=int(10*final_time+2)
newGridStatus=[]
for i in range(num_frames):
    newGridStatus.append('Grid_'+str(2+3*i))
newGridStatus.append('Grid_c0p2_Lagrange')
for i in range(num_frames):
    newGridStatus.append('Grid_c0p2_Lagrange['+str(i+1)+']')
#
gaussian_3D_completexmf.GridStatus = newGridStatus
### END OF FIX OF STATE IN PARAVIEW ###

# create a new 'Iso Volume'
isoVolume1 = IsoVolume(Input=gaussian_3D_completexmf)
isoVolume1.InputScalars = ['POINTS', 'phi']
isoVolume1.ThresholdRange = [-1000.0, 0.0]

# create a new 'Clip'
clip1 = Clip(Input=isoVolume1)
clip1.ClipType = 'Plane'
clip1.Scalars = ['POINTS', 'nodeMaterialTypes']
clip1.Value = 3.0

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [10.0, 0.0, 0.45]
clip1.ClipType.Normal = [0.0, 0.0, 1.0]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

if False:
    # show data from outline1
    outline1Display = Show(outline1, renderView1)
    # trace defaults for the display properties.
    outline1Display.Representation = 'Surface'
    outline1Display.ColorArrayName = [None, '']
    outline1Display.DiffuseColor = [0.0, 0.0, 0.0]
    outline1Display.LineWidth = 6.0
    outline1Display.Scale = [0.1, 1.0, 2.0]
    outline1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    outline1Display.SelectOrientationVectors = 'None'
    outline1Display.ScaleFactor = 2.0
    outline1Display.SelectScaleArray = 'None'
    outline1Display.GlyphType = 'Arrow'
    outline1Display.GlyphTableIndexArray = 'None'
    outline1Display.DataAxesGrid = 'GridAxesRepresentation'
    outline1Display.PolarAxes = 'PolarAxesRepresentation'
    outline1Display.GaussianRadius = 1.0
    outline1Display.SetScaleArray = [None, '']
    outline1Display.ScaleTransferFunction = 'PiecewiseFunction'
    outline1Display.OpacityArray = [None, '']
    outline1Display.OpacityTransferFunction = 'PiecewiseFunction'

    # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
    outline1Display.PolarAxes.Scale = [0.1, 1.0, 2.0]
#
# show data from box1
box1Display = Show(box1, renderView1)
# trace defaults for the display properties.
box1Display.Representation = 'Surface'
box1Display.ColorArrayName = [None, '']
box1Display.Ambient = 0.2
box1Display.Scale = [0.1, 1.0, 2.0]
box1Display.OSPRayScaleArray = 'Normals'
box1Display.OSPRayScaleFunction = 'PiecewiseFunction'
box1Display.SelectOrientationVectors = 'None'
box1Display.ScaleFactor = 2.0
box1Display.SelectScaleArray = 'None'
box1Display.GlyphType = 'Arrow'
box1Display.GlyphTableIndexArray = 'None'
box1Display.DataAxesGrid = 'GridAxesRepresentation'
box1Display.PolarAxes = 'PolarAxesRepresentation'
box1Display.GaussianRadius = 1.0
box1Display.SetScaleArray = [None, '']
box1Display.ScaleTransferFunction = 'PiecewiseFunction'
box1Display.OpacityArray = [None, '']
box1Display.OpacityTransferFunction = 'PiecewiseFunction'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
box1Display.PolarAxes.Scale = [0.1, 1.0, 2.0]

# show data from clip1
clip1Display = Show(clip1, renderView1)
# trace defaults for the display properties.
clip1Display.Representation = 'Surface'
clip1Display.ColorArrayName = ['POINTS', '']
clip1Display.DiffuseColor = [0.0, 0.6666666666666666, 1.0]
clip1Display.Scale = [0.1, 1.0, 2.0]
clip1Display.OSPRayScaleArray = 'nodeMaterialTypes'
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.SelectOrientationVectors = 'None'
clip1Display.ScaleFactor = 2.0
clip1Display.SelectScaleArray = 'nodeMaterialTypes'
clip1Display.GlyphType = 'Arrow'
clip1Display.GlyphTableIndexArray = 'nodeMaterialTypes'
clip1Display.DataAxesGrid = 'GridAxesRepresentation'
clip1Display.PolarAxes = 'PolarAxesRepresentation'
clip1Display.ScalarOpacityUnitDistance = 0.09834055077094629
clip1Display.GaussianRadius = 1.0
clip1Display.SetScaleArray = ['POINTS', 'nodeMaterialTypes']
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityArray = ['POINTS', 'nodeMaterialTypes']
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
clip1Display.PolarAxes.Scale = [0.1, 1.0, 2.0]

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(box1)
# ----------------------------------------------------------------

timeKeeper1 = GetTimeKeeper()
#DT = timeKeeper1.TimestepValues
T0=0 # 0,1,2,3,...
DT=[]
for i in range(10):
    DT.append(T0+i/10.0)
#

for t in DT:
    print (t)
    timeKeeper1.Time=t
    Render(renderView1)
    SaveScreenshot('frameFrontCut_'+str(t)+'.png', renderView1, ImageResolution=[3388, 1777])
#
