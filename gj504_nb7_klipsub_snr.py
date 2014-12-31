#! /usr/bin/env python

from adiklip import *
import astropy.io.fits as pyfits

res_coadd_fname = '/disk1/zimmerman/GJ504/apr21_longL/klipsub_results_fall2014/gj504_longL_octcanon_globalklip_rad215-255_mode010-010_res_coadd.fits'

#res_coadd_fname = '/disk1/zimmerman/GJ504/apr21_longL/klipsub_results/gj504_longL_octcanon_srcklip_rad260_dphi90_mode000_res_coadd.fits'
#res_coadd_fname = '/disk1/zimmerman/GJ504/apr21_longL/klipsub_results/gj504_longL_octcanon_srcklip_rad255_dphi50_mode000_res_coadd.fits'
#res_coadd_fname = '/disk1/zimmerman/GJ504/apr21_longL/klipsub_results/gj504_longL_octcanon_srcklip_rad260_dphi50_mode010_res_coadd.fits'

#res_coadd_fname = '/disk1/zimmerman/GJ504/apr21_longL/klipsub_results_fall2014/gj504_longL_octcanon_globalklip_rad215-255_mode005-005_res_coadd.fits'

x_p = 130.4
y_p = 196.7

res_img_hdulist = pyfits.open(res_coadd_fname, 'readonly')
res_img = res_img_hdulist[0].data
res_img_hdulist.close()
xy_src = (res_img.shape[0]/2 - 0.5 + x_p, res_img.shape[0]/2 - 0.5 + y_p)
src_rad_map = np.sqrt(get_radius_sqrd(res_img.shape, c = xy_src))
bg_ind = np.where( src_rad_map > 10. )
rms = np.sqrt( nanmean( res_img[bg_ind]**2 ) )
print 'background RMS, min, max for %s:\n %.3e, %.3e, %.3e' % (res_coadd_fname, rms, np.nanmin(res_img[bg_ind]), np.nanmax(res_img[bg_ind]))
