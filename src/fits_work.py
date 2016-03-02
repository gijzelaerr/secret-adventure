
# In[ ]:

import pyfits
import numpy as np

class EasyFits(object):
    """class composed of fits file and useful attributes"""
    def __init__(self, input_fits_name):
        print 'creating EasyFits from '+input_fits_name
        self.fits = pyfits.open(input_fits_name)

        self.data = self.fits[0].data
        self.pixelsize = np.abs(self.fits[0].header['CDELT1'])
        self.npix = self.fits[0].header['NAXIS1']
        self.RA0 = self.fits[0].header['CRVAL1'] 
        self.DEC0 = self.fits[0].header['CRVAL2'] 





