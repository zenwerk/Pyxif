"""EXIF is a set of several IFDs.
Oth IFD can include "Make", "Model" and more...
Exif IFD can include "ExposureTime", "ISOSpeed" and more...
GPS IFD can include GPS information.

Pass dict(s), that shows several IFD, to "dump" function.
exifbytes = pyxif.dump(0th_dict, exif_dict, gps_dict) # second and third are optional.

To use dict as IFD data, it needs...
  A tag number means which property? - 256: ImageWidth, 272: Model...
  Appropriate type for property. - long for ImageWidth, str for Model...
    zeroth_ifd = {pyxif.ImageGroup.Make: "Canon",
                  pyxif.ImageGroup.XResolution: (96, 1),
                  pyxif.ImageGroup.YResolution: (96, 1),
                  pyxif.ImageGroup.Software: "Photoshop x.x.x",
                  }

Property name and tag number
  For 0th IFD - under "pyxif.ImageGroup"
  For Exif IFD - under "pyxif.PhotoGroup"
  For GPS IFD - under "pyxif.GPSInfoGroup"

Property and appropriate type
  See variable"TAGS" in this script.

"Byte": int
"Ascii": str
"Short": int
"Long": Long
"Rational": (long, long)
"Undefined": str
"SLong": long
"SRational": (long, long)
"""

import os

import pyxif
from PIL import Image


def dump_sample(input_file, output_file):
    zeroth_ifd = {pyxif.ImageGroup.Make: "fooooooooooooo",
                  pyxif.ImageGroup.XResolution: (96, 1),
                  pyxif.ImageGroup.YResolution: (96, 1),
                  pyxif.ImageGroup.Software: "paint.net 4.0.3",
                  }

    exif_ifd = {pyxif.PhotoGroup.ExifVersion: "0111",
                pyxif.PhotoGroup.DateTimeOriginal: "1999:09:99 99:99:99",
                pyxif.PhotoGroup.CameraOwnerName: "Mr. John Doe",
                }

    gps_ifd = {pyxif.GPSInfoGroup.GPSDateStamp: "1999:99:99",
               pyxif.GPSInfoGroup.GPSDifferential: 90,
               }
    exif_bytes = pyxif.dump(zeroth_ifd=zeroth_ifd, exif_ifd=exif_ifd, gps_ifd=gps_ifd)

    im = Image.open(input_file)
    im.thumbnail((100, 100), Image.ANTIALIAS)
    im.save(output_file, exif=exif_bytes)

    z, e, g = pyxif.load(output_file)
    print(z, e, g)


TAGS = {
 'Image': {11: {'group': 'ProcessingSoftware', 'type': 'Ascii'},
           254: {'group': 'NewSubfileType', 'type': 'Long'},
           255: {'group': 'SubfileType', 'type': 'Short'},
           256: {'group': 'ImageWidth', 'type': 'Long'},
           257: {'group': 'ImageLength', 'type': 'Long'},
           258: {'group': 'BitsPerSample', 'type': 'Short'},
           259: {'group': 'Compression', 'type': 'Short'},
           262: {'group': 'PhotometricInterpretation', 'type': 'Short'},
           263: {'group': 'Threshholding', 'type': 'Short'},
           264: {'group': 'CellWidth', 'type': 'Short'},
           265: {'group': 'CellLength', 'type': 'Short'},
           266: {'group': 'FillOrder', 'type': 'Short'},
           269: {'group': 'DocumentName', 'type': 'Ascii'},
           270: {'group': 'ImageDescription', 'type': 'Ascii'},
           271: {'group': 'Make', 'type': 'Ascii'},
           272: {'group': 'Model', 'type': 'Ascii'},
           273: {'group': 'StripOffsets', 'type': 'Long'},
           274: {'group': 'Orientation', 'type': 'Short'},
           277: {'group': 'SamplesPerPixel', 'type': 'Short'},
           278: {'group': 'RowsPerStrip', 'type': 'Long'},
           279: {'group': 'StripByteCounts', 'type': 'Long'},
           282: {'group': 'XResolution', 'type': 'Rational'},
           283: {'group': 'YResolution', 'type': 'Rational'},
           284: {'group': 'PlanarConfiguration', 'type': 'Short'},
           290: {'group': 'GrayResponseUnit', 'type': 'Short'},
           291: {'group': 'GrayResponseCurve', 'type': 'Short'},
           292: {'group': 'T4Options', 'type': 'Long'},
           293: {'group': 'T6Options', 'type': 'Long'},
           296: {'group': 'ResolutionUnit', 'type': 'Short'},
           301: {'group': 'TransferFunction', 'type': 'Short'},
           305: {'group': 'Software', 'type': 'Ascii'},
           306: {'group': 'DateTime', 'type': 'Ascii'},
           315: {'group': 'Artist', 'type': 'Ascii'},
           316: {'group': 'HostComputer', 'type': 'Ascii'},
           317: {'group': 'Predictor', 'type': 'Short'},
           318: {'group': 'WhitePoint', 'type': 'Rational'},
           319: {'group': 'PrimaryChromaticities', 'type': 'Rational'},
           320: {'group': 'ColorMap', 'type': 'Short'},
           321: {'group': 'HalftoneHints', 'type': 'Short'},
           322: {'group': 'TileWidth', 'type': 'Short'},
           323: {'group': 'TileLength', 'type': 'Short'},
           324: {'group': 'TileOffsets', 'type': 'Short'},
           325: {'group': 'TileByteCounts', 'type': 'Short'},
           330: {'group': 'SubIFDs', 'type': 'Long'},
           332: {'group': 'InkSet', 'type': 'Short'},
           333: {'group': 'InkNames', 'type': 'Ascii'},
           334: {'group': 'NumberOfInks', 'type': 'Short'},
           336: {'group': 'DotRange', 'type': 'Byte'},
           337: {'group': 'TargetPrinter', 'type': 'Ascii'},
           338: {'group': 'ExtraSamples', 'type': 'Short'},
           339: {'group': 'SampleFormat', 'type': 'Short'},
           340: {'group': 'SMinSampleValue', 'type': 'Short'},
           341: {'group': 'SMaxSampleValue', 'type': 'Short'},
           342: {'group': 'TransferRange', 'type': 'Short'},
           343: {'group': 'ClipPath', 'type': 'Byte'},
           344: {'group': 'XClipPathUnits', 'type': 'Long'},
           345: {'group': 'YClipPathUnits', 'type': 'Long'},
           346: {'group': 'Indexed', 'type': 'Short'},
           347: {'group': 'JPEGTables', 'type': 'Undefined'},
           351: {'group': 'OPIProxy', 'type': 'Short'},
           512: {'group': 'JPEGProc', 'type': 'Long'},
           513: {'group': 'JPEGInterchangeFormat', 'type': 'Long'},
           514: {'group': 'JPEGInterchangeFormatLength', 'type': 'Long'},
           515: {'group': 'JPEGRestartInterval', 'type': 'Short'},
           517: {'group': 'JPEGLosslessPredictors', 'type': 'Short'},
           518: {'group': 'JPEGPointTransforms', 'type': 'Short'},
           519: {'group': 'JPEGQTables', 'type': 'Long'},
           520: {'group': 'JPEGDCTables', 'type': 'Long'},
           521: {'group': 'JPEGACTables', 'type': 'Long'},
           529: {'group': 'YCbCrCoefficients', 'type': 'Rational'},
           530: {'group': 'YCbCrSubSampling', 'type': 'Short'},
           531: {'group': 'YCbCrPositioning', 'type': 'Short'},
           532: {'group': 'ReferenceBlackWhite', 'type': 'Rational'},
           700: {'group': 'XMLPacket', 'type': 'Byte'},
           18246: {'group': 'Rating', 'type': 'Short'},
           18249: {'group': 'RatingPercent', 'type': 'Short'},
           32781: {'group': 'ImageID', 'type': 'Ascii'},
           33421: {'group': 'CFARepeatPatternDim', 'type': 'Short'},
           33422: {'group': 'CFAPattern', 'type': 'Byte'},
           33423: {'group': 'BatteryLevel', 'type': 'Rational'},
           33432: {'group': 'Copyright', 'type': 'Ascii'},
           33434: {'group': 'ExposureTime', 'type': 'Rational'},
           34377: {'group': 'ImageResources', 'type': 'Byte'},
           34665: {'group': 'ExifTag', 'type': 'Long'},
           34675: {'group': 'InterColorProfile', 'type': 'Undefined'},
           34853: {'group': 'GPSTag', 'type': 'Long'},
           34857: {'group': 'Interlace', 'type': 'Short'},
           34858: {'group': 'TimeZoneOffset', 'type': 'Long'},
           34859: {'group': 'SelfTimerMode', 'type': 'Short'},
           37387: {'group': 'FlashEnergy', 'type': 'Rational'},
           37388: {'group': 'SpatialFrequencyResponse', 'type': 'Undefined'},
           37389: {'group': 'Noise', 'type': 'Undefined'},
           37390: {'group': 'FocalPlaneXResolution', 'type': 'Rational'},
           37391: {'group': 'FocalPlaneYResolution', 'type': 'Rational'},
           37392: {'group': 'FocalPlaneResolutionUnit', 'type': 'Short'},
           37393: {'group': 'ImageNumber', 'type': 'Long'},
           37394: {'group': 'SecurityClassification', 'type': 'Ascii'},
           37395: {'group': 'ImageHistory', 'type': 'Ascii'},
           37397: {'group': 'ExposureIndex', 'type': 'Rational'},
           37398: {'group': 'TIFFEPStandardID', 'type': 'Byte'},
           37399: {'group': 'SensingMethod', 'type': 'Short'},
           40091: {'group': 'XPTitle', 'type': 'Byte'},
           40092: {'group': 'XPComment', 'type': 'Byte'},
           40093: {'group': 'XPAuthor', 'type': 'Byte'},
           40094: {'group': 'XPKeywords', 'type': 'Byte'},
           40095: {'group': 'XPSubject', 'type': 'Byte'},
           50341: {'group': 'PrintImageMatching', 'type': 'Undefined'},
           50706: {'group': 'DNGVersion', 'type': 'Byte'},
           50707: {'group': 'DNGBackwardVersion', 'type': 'Byte'},
           50708: {'group': 'UniqueCameraModel', 'type': 'Ascii'},
           50709: {'group': 'LocalizedCameraModel', 'type': 'Byte'},
           50710: {'group': 'CFAPlaneColor', 'type': 'Byte'},
           50711: {'group': 'CFALayout', 'type': 'Short'},
           50712: {'group': 'LinearizationTable', 'type': 'Short'},
           50713: {'group': 'BlackLevelRepeatDim', 'type': 'Short'},
           50714: {'group': 'BlackLevel', 'type': 'Rational'},
           50715: {'group': 'BlackLevelDeltaH', 'type': 'SRational'},
           50716: {'group': 'BlackLevelDeltaV', 'type': 'SRational'},
           50717: {'group': 'WhiteLevel', 'type': 'Short'},
           50718: {'group': 'DefaultScale', 'type': 'Rational'},
           50719: {'group': 'DefaultCropOrigin', 'type': 'Short'},
           50720: {'group': 'DefaultCropSize', 'type': 'Short'},
           50721: {'group': 'ColorMatrix1', 'type': 'SRational'},
           50722: {'group': 'ColorMatrix2', 'type': 'SRational'},
           50723: {'group': 'CameraCalibration1', 'type': 'SRational'},
           50724: {'group': 'CameraCalibration2', 'type': 'SRational'},
           50725: {'group': 'ReductionMatrix1', 'type': 'SRational'},
           50726: {'group': 'ReductionMatrix2', 'type': 'SRational'},
           50727: {'group': 'AnalogBalance', 'type': 'Rational'},
           50728: {'group': 'AsShotNeutral', 'type': 'Short'},
           50729: {'group': 'AsShotWhiteXY', 'type': 'Rational'},
           50730: {'group': 'BaselineExposure', 'type': 'SRational'},
           50731: {'group': 'BaselineNoise', 'type': 'Rational'},
           50732: {'group': 'BaselineSharpness', 'type': 'Rational'},
           50733: {'group': 'BayerGreenSplit', 'type': 'Long'},
           50734: {'group': 'LinearResponseLimit', 'type': 'Rational'},
           50735: {'group': 'CameraSerialNumber', 'type': 'Ascii'},
           50736: {'group': 'LensInfo', 'type': 'Rational'},
           50737: {'group': 'ChromaBlurRadius', 'type': 'Rational'},
           50738: {'group': 'AntiAliasStrength', 'type': 'Rational'},
           50739: {'group': 'ShadowScale', 'type': 'SRational'},
           50740: {'group': 'DNGPrivateData', 'type': 'Byte'},
           50741: {'group': 'MakerNoteSafety', 'type': 'Short'},
           50778: {'group': 'CalibrationIlluminant1', 'type': 'Short'},
           50779: {'group': 'CalibrationIlluminant2', 'type': 'Short'},
           50780: {'group': 'BestQualityScale', 'type': 'Rational'},
           50781: {'group': 'RawDataUniqueID', 'type': 'Byte'},
           50827: {'group': 'OriginalRawFileName', 'type': 'Byte'},
           50828: {'group': 'OriginalRawFileData', 'type': 'Undefined'},
           50829: {'group': 'ActiveArea', 'type': 'Short'},
           50830: {'group': 'MaskedAreas', 'type': 'Short'},
           50831: {'group': 'AsShotICCProfile', 'type': 'Undefined'},
           50832: {'group': 'AsShotPreProfileMatrix', 'type': 'SRational'},
           50833: {'group': 'CurrentICCProfile', 'type': 'Undefined'},
           50834: {'group': 'CurrentPreProfileMatrix', 'type': 'SRational'},
           50879: {'group': 'ColorimetricReference', 'type': 'Short'},
           50931: {'group': 'CameraCalibrationSignature', 'type': 'Byte'},
           50932: {'group': 'ProfileCalibrationSignature', 'type': 'Byte'},
           50934: {'group': 'AsShotProfileName', 'type': 'Byte'},
           50935: {'group': 'NoiseReductionApplied', 'type': 'Rational'},
           50936: {'group': 'ProfileName', 'type': 'Byte'},
           50937: {'group': 'ProfileHueSatMapDims', 'type': 'Long'},
           50938: {'group': 'ProfileHueSatMapData1', 'type': 'Float'},
           50939: {'group': 'ProfileHueSatMapData2', 'type': 'Float'},
           50940: {'group': 'ProfileToneCurve', 'type': 'Float'},
           50941: {'group': 'ProfileEmbedPolicy', 'type': 'Long'},
           50942: {'group': 'ProfileCopyright', 'type': 'Byte'},
           50964: {'group': 'ForwardMatrix1', 'type': 'SRational'},
           50965: {'group': 'ForwardMatrix2', 'type': 'SRational'},
           50966: {'group': 'PreviewApplicationName', 'type': 'Byte'},
           50967: {'group': 'PreviewApplicationVersion', 'type': 'Byte'},
           50968: {'group': 'PreviewSettingsName', 'type': 'Byte'},
           50969: {'group': 'PreviewSettingsDigest', 'type': 'Byte'},
           50970: {'group': 'PreviewColorSpace', 'type': 'Long'},
           50971: {'group': 'PreviewDateTime', 'type': 'Ascii'},
           50972: {'group': 'RawImageDigest', 'type': 'Undefined'},
           50973: {'group': 'OriginalRawFileDigest', 'type': 'Undefined'},
           50974: {'group': 'SubTileBlockSize', 'type': 'Long'},
           50975: {'group': 'RowInterleaveFactor', 'type': 'Long'},
           50981: {'group': 'ProfileLookTableDims', 'type': 'Long'},
           50982: {'group': 'ProfileLookTableData', 'type': 'Float'},
           51008: {'group': 'OpcodeList1', 'type': 'Undefined'},
           51009: {'group': 'OpcodeList2', 'type': 'Undefined'},
           51022: {'group': 'OpcodeList3', 'type': 'Undefined'},
           51041: {'group': 'NoiseProfile', 'type': 'Double'}},
 'Photo': {33434: {'group': 'ExposureTime', 'type': 'Rational'},
           33437: {'group': 'FNumber', 'type': 'Rational'},
           34850: {'group': 'ExposureProgram', 'type': 'Short'},
           34852: {'group': 'SpectralSensitivity', 'type': 'Ascii'},
           34855: {'group': 'ISOSpeedRatings', 'type': 'Short'},
           34856: {'group': 'OECF', 'type': 'Undefined'},
           34864: {'group': 'SensitivityType', 'type': 'Short'},
           34865: {'group': 'StandardOutputSensitivity', 'type': 'Long'},
           34866: {'group': 'RecommendedExposureIndex', 'type': 'Long'},
           34867: {'group': 'ISOSpeed', 'type': 'Long'},
           34868: {'group': 'ISOSpeedLatitudeyyy', 'type': 'Long'},
           34869: {'group': 'ISOSpeedLatitudezzz', 'type': 'Long'},
           36864: {'group': 'ExifVersion', 'type': 'Undefined'},
           36867: {'group': 'DateTimeOriginal', 'type': 'Ascii'},
           36868: {'group': 'DateTimeDigitized', 'type': 'Ascii'},
           37121: {'group': 'ComponentsConfiguration', 'type': 'Undefined'},
           37122: {'group': 'CompressedBitsPerPixel', 'type': 'Rational'},
           37377: {'group': 'ShutterSpeedValue', 'type': 'SRational'},
           37378: {'group': 'ApertureValue', 'type': 'Rational'},
           37379: {'group': 'BrightnessValue', 'type': 'SRational'},
           37380: {'group': 'ExposureBiasValue', 'type': 'SRational'},
           37381: {'group': 'MaxApertureValue', 'type': 'Rational'},
           37382: {'group': 'SubjectDistance', 'type': 'Rational'},
           37383: {'group': 'MeteringMode', 'type': 'Short'},
           37384: {'group': 'LightSource', 'type': 'Short'},
           37385: {'group': 'Flash', 'type': 'Short'},
           37386: {'group': 'FocalLength', 'type': 'Rational'},
           37396: {'group': 'SubjectArea', 'type': 'Short'},
           37500: {'group': 'MakerNote', 'type': 'Undefined'},
           37510: {'group': 'UserComment', 'type': 'Comment'},
           37520: {'group': 'SubSecTime', 'type': 'Ascii'},
           37521: {'group': 'SubSecTimeOriginal', 'type': 'Ascii'},
           37522: {'group': 'SubSecTimeDigitized', 'type': 'Ascii'},
           40960: {'group': 'FlashpixVersion', 'type': 'Undefined'},
           40961: {'group': 'ColorSpace', 'type': 'Short'},
           40962: {'group': 'PixelXDimension', 'type': 'Long'},
           40963: {'group': 'PixelYDimension', 'type': 'Long'},
           40964: {'group': 'RelatedSoundFile', 'type': 'Ascii'},
           40965: {'group': 'InteroperabilityTag', 'type': 'Long'},
           41483: {'group': 'FlashEnergy', 'type': 'Rational'},
           41484: {'group': 'SpatialFrequencyResponse', 'type': 'Undefined'},
           41486: {'group': 'FocalPlaneXResolution', 'type': 'Rational'},
           41487: {'group': 'FocalPlaneYResolution', 'type': 'Rational'},
           41488: {'group': 'FocalPlaneResolutionUnit', 'type': 'Short'},
           41492: {'group': 'SubjectLocation', 'type': 'Short'},
           41493: {'group': 'ExposureIndex', 'type': 'Rational'},
           41495: {'group': 'SensingMethod', 'type': 'Short'},
           41728: {'group': 'FileSource', 'type': 'Undefined'},
           41729: {'group': 'SceneType', 'type': 'Undefined'},
           41730: {'group': 'CFAPattern', 'type': 'Undefined'},
           41985: {'group': 'CustomRendered', 'type': 'Short'},
           41986: {'group': 'ExposureMode', 'type': 'Short'},
           41987: {'group': 'WhiteBalance', 'type': 'Short'},
           41988: {'group': 'DigitalZoomRatio', 'type': 'Rational'},
           41989: {'group': 'FocalLengthIn35mmFilm', 'type': 'Short'},
           41990: {'group': 'SceneCaptureType', 'type': 'Short'},
           41991: {'group': 'GainControl', 'type': 'Short'},
           41992: {'group': 'Contrast', 'type': 'Short'},
           41993: {'group': 'Saturation', 'type': 'Short'},
           41994: {'group': 'Sharpness', 'type': 'Short'},
           41995: {'group': 'DeviceSettingDescription', 'type': 'Undefined'},
           41996: {'group': 'SubjectDistanceRange', 'type': 'Short'},
           42016: {'group': 'ImageUniqueID', 'type': 'Ascii'},
           42032: {'group': 'CameraOwnerName', 'type': 'Ascii'},
           42033: {'group': 'BodySerialNumber', 'type': 'Ascii'},
           42034: {'group': 'LensSpecification', 'type': 'Rational'},
           42035: {'group': 'LensMake', 'type': 'Ascii'},
           42036: {'group': 'LensModel', 'type': 'Ascii'},
           42037: {'group': 'LensSerialNumber', 'type': 'Ascii'}},
 'GPSInfo': {0: {'group': 'GPSVersionID', 'type': 'Byte'},
             1: {'group': 'GPSLatitudeRef', 'type': 'Ascii'},
             2: {'group': 'GPSLatitude', 'type': 'Rational'},
             3: {'group': 'GPSLongitudeRef', 'type': 'Ascii'},
             4: {'group': 'GPSLongitude', 'type': 'Rational'},
             5: {'group': 'GPSAltitudeRef', 'type': 'Byte'},
             6: {'group': 'GPSAltitude', 'type': 'Rational'},
             7: {'group': 'GPSTimeStamp', 'type': 'Rational'},
             8: {'group': 'GPSSatellites', 'type': 'Ascii'},
             9: {'group': 'GPSStatus', 'type': 'Ascii'},
             10: {'group': 'GPSMeasureMode', 'type': 'Ascii'},
             11: {'group': 'GPSDOP', 'type': 'Rational'},
             12: {'group': 'GPSSpeedRef', 'type': 'Ascii'},
             13: {'group': 'GPSSpeed', 'type': 'Rational'},
             14: {'group': 'GPSTrackRef', 'type': 'Ascii'},
             15: {'group': 'GPSTrack', 'type': 'Rational'},
             16: {'group': 'GPSImgDirectionRef', 'type': 'Ascii'},
             17: {'group': 'GPSImgDirection', 'type': 'Rational'},
             18: {'group': 'GPSMapDatum', 'type': 'Ascii'},
             19: {'group': 'GPSDestLatitudeRef', 'type': 'Ascii'},
             20: {'group': 'GPSDestLatitude', 'type': 'Rational'},
             21: {'group': 'GPSDestLongitudeRef', 'type': 'Ascii'},
             22: {'group': 'GPSDestLongitude', 'type': 'Rational'},
             23: {'group': 'GPSDestBearingRef', 'type': 'Ascii'},
             24: {'group': 'GPSDestBearing', 'type': 'Rational'},
             25: {'group': 'GPSDestDistanceRef', 'type': 'Ascii'},
             26: {'group': 'GPSDestDistance', 'type': 'Rational'},
             27: {'group': 'GPSProcessingMethod', 'type': 'Undefined'},
             28: {'group': 'GPSAreaInformation', 'type': 'Undefined'},
             29: {'group': 'GPSDateStamp', 'type': 'Ascii'},
             30: {'group': 'GPSDifferential', 'type': 'Short'}}
}


if __name__ == "__main__":
    dump_sample(os.path.join("samples", "01.jpg"),
                "dump_sample.jpg")
