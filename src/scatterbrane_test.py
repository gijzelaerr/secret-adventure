from Pyxis.ModSupport import *
import numpy as np
from fits_work import EasyFits
import pyfits
from parameter_work import *
import kliko


def run_test(config):
    schema_string = open('../kliko.yml', 'r').read()
    parameters = open(config, 'r').read()
    schema = kliko.validate_kliko(schema_string)

    kliko.validate_parameters(parameters, schema)

    parameters = load_json_parameters_into_dictionary(config)
    v.OUTDIR = parameters['fits'].split('.fits')[0]
    x.sh('mkdir '+ OUTDIR)
    fits = 'input/'+parameters['fits']
    model0 = EasyFits(fits)
    new = model0.data+np.random.normal(0, parameters['scale'], size=model0.data.shape)
    pyfits.writeto(OUTDIR+"/scattered.fits", new,
                   pyfits.getheader(model0.fits.filename()), clobber=True)

    x.sh('mv %s output/' % OUTDIR)


run_test('input/parameters.json')