from __future__ import division

from cProfile import run

from brane import Brane
import Pyxis
from Pyxis.ModSupport import *
import numpy as np
from fits_work import EasyFits
import pyfits
import pyrap.tables as pt
from parameter_work import *
import glob

"""Repacking of 'Scatterbrane', see:http://krosenfeld.github.io/scatterbrane/current/user/brane.html"""

deg2muas = 3600e6
pc2m = 3.086e16

def run_scatterbrane(config):

    parameters=load_json_parameters_into_dictionary(config)
    ism_dict = setup_keyword_dictionary('ism_', parameters)
    v.MS = parameters['fitsfolder']+'.MS'
    v.OUTDIR = parameters['fitsfolder']
    x.sh('mkdir '+OUTDIR)
    fits_list = np.sort(glob.glob('input/%s/*.fits' % parameters['fitsfolder'])).tolist()
    model0 = EasyFits(fits_list[0])

    brane = Brane(model0.fits[0].data[0, 0, :, :], model0.pixelsize * deg2muas,
                  nphi=2**ism_dict['nphi_exponent'], wavelength=parameters['wavelength'])
    brane.generatePhases()
    brane.scatter()

    header = pyfits.getheader(model0.fits.filename())
    header['NAXIS1'] = brane.nx
    header['NAXIS2'] = brane.nx
    header['CDELT1'] = -1*brane.dx/float(deg2muas)
    header['CDELT2'] = 1*brane.dx/float(deg2muas)

    pyfits.writeto(OUTDIR+"/scattered.fits", brane.iss.reshape(1, 1, brane.nx, brane.nx),
                   header, clobber=True)

    x.sh('mv %s output/'%OUTDIR)

    print "ISM Scattered"

run_scatterbrane('parameters.json')
