from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.conf import settings

from geotrellis.spark.io.file.FileValueReader import file_value_reader
from geotrellis.spark.SpatialKey import SpatialKey
from geotrellis.spark.LayerId import LayerId
from geotrellis.raster.MultibandTile import MultibandTile
from geotrellis.raster.CellType import DoubleConstantNoDataCellType
from geotrellis.raster.package_scala import isData
from geotrellis.spark.io.package_scala import TileNotFoundError
from geotrellis.raster.render.ColorMap import ColorMap
from geotrellis.raster.render.PngRenderMethods import renderPng

flv = file_value_reader('/home/leroy/landsat/data/catalog')
colorMap = ColorMap.fromStringDouble(settings.TUTORIAL_COLORMAP)

def zxy(request, zoom, x, y):
    zoom, x, y = int(zoom), int(x), int(y)
    try:
        reader = flv.reader(SpatialKey, MultibandTile, LayerId("landsat", zoom))
        tile = reader.read(SpatialKey.fromTuple((x, y)))
    except TileNotFoundError:
        raise Http404("Tile (x={x}, y={y}, zoom={zoom}) not found".format(
            x=x, y=y, zoom=zoom))

    ndvi = tile.convert(DoubleConstantNoDataCellType).combineDouble(0, 1,
            lambda r, ir: (ir - r) / (ir + r) if isData(r) and isData(ir) else float("nan"))
    pic = renderPng(ndvi, colorMap).bytes
    return HttpResponse(pic, 'image/png')
