### CVP Delivery Data

This code scrapes the water supply delivery data from here:
https://usbr.gov/mp/cvo/deliv.html

And attempts to convert it all to CSV. This does not work yet. Overview of main issues with data:

* Years 2011-present are in PDF form. The code to convert this to CSV seems to work thanks to the extremely useful [tabula-py](https://github.com/chezou/tabula-py). (Note for OSX: use Homebrew Java instead of default).
* Years 2001-2010 are in `.prn` format. These can be downloaded, but I'm still figuring out how to convert to CSV. Mixed delimiter problem.
* Years 1993-2000 are in TXT format. Same as above, these can be downloaded but not converted.

Prior to 1998 the tables were numbered 30-38. Beginning in 1998 they are numbered 21-29.
