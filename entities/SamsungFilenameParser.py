from os.path import splitext
from MediaName import MediaName
from MediaDate import MediaDate

class SamsungFilenameParser:
    """Parse a filename generated by a Samsung application: yyyymmdd_xxxxxxxxxxx.jpg"""

    @staticmethod
    def parse(filename):
        """This parser assumes that all fields are mandatory. If there is any field missing, it will fail."""
        name = SamsungFilenameParser.__removeFileExtension(filename)
        dateFromName = SamsungFilenameParser.__removeCounter(name)
        standardMetadataDateFormat = SamsungFilenameParser.__convertToMetadataFormat(dateFromName)
        return MediaName(MediaDate(standardMetadataDateFormat, "Filename"))

    @staticmethod
    def __removeFileExtension(filename):
        return splitext(filename)[0]

    @staticmethod
    def __removeCounter(name):
        date = name.split('_')[0]
        if len(date) != 8:
            raise ValueError('File name ' + date + ' cannot be parsed.')
        return date


    @staticmethod
    def __convertToMetadataFormat(dateFromName):
        return dateFromName[0:4] + ':' + dateFromName[4:6] + ':' + dateFromName[6:8]
