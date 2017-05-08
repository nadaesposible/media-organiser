from os.path import splitext
from MediaName import MediaName
from MediaDate import MediaDate

class DefaultFilenameParser:
    """Parse a filename generated by the Media Organiser application: yyyy-mm-dd_hh.mm.ss_nnnnnn.ext"""

    @staticmethod
    def parse(filename):
        """This parser assumes that all fields are mandatory. If there is any field missing, it will fail."""
        name = DefaultFilenameParser.__removeFileExtension(filename)
        dateFromName = DefaultFilenameParser.__removeCounter(name)
        standardMetadataDateFormat = DefaultFilenameParser.__convertToMetadataFormat(dateFromName)
        return MediaName(MediaDate(standardMetadataDateFormat))

    @staticmethod
    def __removeFileExtension(filename):
        return splitext(filename)[0]

    @staticmethod
    def __removeCounter(name):
        parts = name.split('_')
        return '_'.join(parts[:2])

    @staticmethod
    def __convertToMetadataFormat(dateFromName):
        return dateFromName.replace('-', ':').replace('.', ':').replace('_', ' ')
