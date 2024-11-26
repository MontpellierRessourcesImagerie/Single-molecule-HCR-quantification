"""
This module is an example of a barebones sample data provider for napari.

It implements the "sample data" specification.
see: https://napari.org/stable/plugins/guides.html?#sample-data

Replace code below according to your needs.
"""

from __future__ import annotations

import numpy
from skimage import io


def make_sample_data():
    """Generates an image"""
    # Return list of tuples
    # [(data1, add_image_kwargs1), (data2, add_image_kwargs2)]
    # Check the documentation for more information about the
    # add_image_kwargs
    # https://napari.org/stable/api/napari.Viewer.html#napari.Viewer.add_image
    scale = (1000, 76.0005, 76.0005	)
    nucleiData = io.imread('https://dev.mri.cnrs.fr/attachments/download/3597/C1-240628_DAPI_MEMBRITE-546_EPHA-488_TBXT-594_OTX-647_SLOWFADE_2.tif')
    nuclei = numpy.array(nucleiData)
    spotsData = io.imread('https://dev.mri.cnrs.fr/attachments/download/3595/C4-240628_DAPI_MEMBRITE-546_EPHA-488_TBXT-594_OTX-647_SLOWFADE_2.tif')
    spots = numpy.array(spotsData)
    membranesData = io.imread('https://dev.mri.cnrs.fr/attachments/download/3596/C5-240628_DAPI_MEMBRITE-546_EPHA-488_TBXT-594_OTX-647_SLOWFADE_2.tif')
    membranes = numpy.array(membranesData)

    return [(nuclei,
             {'scale': scale,
              'name': 'nuclei (segment-embryo example image)'}),
            (spots,
             {'scale': scale,
              'name': 'spots (segment-embryo example image)'},
             ),
            (membranes,
             {'scale': scale,
              'name': 'membranes (segment-embryo example image)'},
             )
            ]
