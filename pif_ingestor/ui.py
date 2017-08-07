from argparse import ArgumentParser
import json


def get_cli():
    """Construct a CLI parser for pif-ingestor"""
    parser = ArgumentParser(description="Ingest data files to Citrination")

    # Required:
    parser.add_argument('path',
                        help='Location of the file or directory to import')
    parser.add_argument('format',
                        help='Format of data to import, coresponding to the name of the converter extension')

    # Optional
    parser.add_argument('-d', '--dataset', type=int, default=None,
                        help='ID of the dataset into which to upload PIFs')
    parser.add_argument('--tags', nargs='+', default=None,
                        help='Tags to add to PIFs')
    parser.add_argument('-l', '--license', default=None,
                        help='License to attach to PIFs (string)')
    parser.add_argument('-c', '--contact', default=None,
                        help='Contact information (string)')
    # parser.add_argument('--log', default="WARN", dest="log_level",
    #                    help='Logging level')
    parser.add_argument('--args', dest="converter_arguments", default={}, type=json.loads,
                        help='Arguments to pass to converter (as JSON dictionary)')

    return parser
