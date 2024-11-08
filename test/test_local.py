import openmc
import pytest

from openmc_cad_adapter import to_cubit_journal

from .test_utilities import diff_gold_file
from test import run_in_tmpdir


def test_planes(request, run_in_tmpdir):
    plane1 = openmc.Plane(A=1.0, B=1.0, C=0.0, D=-5.0)
    plane2 = openmc.Plane(A=1.0, B=1.0, C=0.0, D=5.0)
    plane3 = openmc.Plane(A=0.0, B=1.0, C=1.0, D=-5.0)
    plane4 = openmc.Plane(A=0.0, B=1.0, C=1.0, D=5.0)
    plane5 = openmc.Plane(A=1.0, B=0.0, C=1.0, D=-5.0)
    plane6 = openmc.Plane(A=1.0, B=0.0, C=1.0, D=5.0)
    g = openmc.Geometry([openmc.Cell(region=+plane1 & -plane2 & +plane3 & -plane4 & +plane5 & -plane6)])
    to_cubit_journal(g, world=(500, 500, 500), filename='plane.jou')
    diff_gold_file('plane.jou')

# Test the XCylinder and YCylinder classes, the ZCylinder surface is tested
# extensively in the OpenMC example tests
def test_xcylinder(request, run_in_tmpdir):
    x_cyl = openmc.XCylinder(r=1.0, y0=10.0, z0=5.0)
    g = openmc.Geometry([openmc.Cell(region=-x_cyl)])
    to_cubit_journal(g, world=(500, 500, 500), filename='xcylinder.jou')
    diff_gold_file('xcylinder.jou')


def test_ycylinder(request, run_in_tmpdir):
    y_cyl = openmc.YCylinder(r=1.0, x0=10.0, z0=5.0)
    g = openmc.Geometry([openmc.Cell(region=-y_cyl)])
    to_cubit_journal(g, world=(500, 500, 500), filename='ycylinder.jou')
    diff_gold_file('ycylinder.jou')


def test_cylinder(request, run_in_tmpdir):
    cyl = openmc.Cylinder(x0=0.0, y0=0.0, z0=0.0, r=6.0, dx=0.7071, dy=0.7071, dz=0.0)
    g = openmc.Geometry([openmc.Cell(region=-cyl)])
    to_cubit_journal(g, world=(500, 500, 500), filename='cylinder.jou')
    diff_gold_file('cylinder.jou')


def test_x_cone(request, run_in_tmpdir):
    x_cone = openmc.XCone(x0=30.0, y0=3.0, z0=5.0, r2=5.0)
    g = openmc.Geometry([openmc.Cell(region=-x_cone)])
    to_cubit_journal(g, world=(500, 500, 500), filename='x_cone.jou')
    diff_gold_file('x_cone.jou')


def test_y_cone(request, run_in_tmpdir):
    y_cone = openmc.YCone(x0=40.0, y0=20.0, z0=7.0, r2=2.0)
    g = openmc.Geometry([openmc.Cell(region=-y_cone)])
    to_cubit_journal(g, world=(500, 500, 500), filename='y_cone.jou')
    diff_gold_file('y_cone.jou')


def test_z_cone(request, run_in_tmpdir):
    z_cone = openmc.ZCone(x0=50.0, y0=10.0, z0=2.0, r2=1.0)
    g = openmc.Geometry([openmc.Cell(region=-z_cone)])
    to_cubit_journal(g, world=(500, 500, 500), filename='z_cone.jou')
    diff_gold_file('z_cone.jou')


def test_x_torus(request, run_in_tmpdir):
    x_torus = openmc.XTorus(x0=10.0, y0=10.0, z0=10.0, a=5.0, b=2.0, c=2.0)
    g = openmc.Geometry([openmc.Cell(region=-x_torus)])
    to_cubit_journal(g, world=(500, 500, 500), filename='x_torus.jou')
    diff_gold_file('x_torus.jou')


def test_y_torus(request, run_in_tmpdir):
    y_torus = openmc.YTorus(x0=-10.0, y0=-10.0, z0=-10.0, a=5.0, b=2.0, c=2.0)
    g = openmc.Geometry([openmc.Cell(region=-y_torus)])
    to_cubit_journal(g, world=(500, 500, 500), filename='y_torus.jou')
    diff_gold_file('y_torus.jou')


def test_z_torus(request, run_in_tmpdir):
    z_torus = openmc.ZTorus(x0=50.0, y0=50.0, z0=50.0, a=5.0, b=2.0, c=2.0)
    g = openmc.Geometry([openmc.Cell(region=-z_torus)])
    to_cubit_journal(g, world=(500, 500, 500), filename='z_torus.jou')
    diff_gold_file('z_torus.jou')


def test_torus_diff_radii(request, run_in_tmpdir):
    with pytest.raises(ValueError):
        z_torus = openmc.ZTorus(x0=50.0, y0=50.0, z0=50.0, a=5.0, b=2.0, c=3.0)
        g = openmc.Geometry([openmc.Cell(region=-z_torus)])
        to_cubit_journal(g, world=(500, 500, 500), filename='a_torus.jou')


def test_general_cone(request, run_in_tmpdir):
    with pytest.raises(NotImplementedError):
        cone = openmc.Cone(x0=0.0, y0=0.0, z0=0.0, r2=6.0, dx=1, dy=1, dz=1)
        g = openmc.Geometry([openmc.Cell(region=-cone)])
        to_cubit_journal(g, world=(500, 500, 500), filename='cone.jou')