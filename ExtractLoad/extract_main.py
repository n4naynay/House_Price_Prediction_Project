from ExtractLoad.utils.utils import ReadWriteFromS3, get_data
from general_utils import load_yaml
import botocore
import logging
import yaml
import pandas as pd
from datetime import datetime
logging.basicConfig(level = logging.INFO)

########    Data Extraction   ##################


def get_and_write_to_s3(bucket_name, key, url, filename):
    pass
    """
    This function extract the data from the url and write to s3
    :return: None
    """
    logging.info("Creating an S3 bucket")
    try:
        createbucket = ReadWriteFromS3.create_con_string(bucket_name, key)
        createbucket.create_s3_bucket()
        logging.info("Created s3 successfully")
    except:
        print("Bucket name already exist!!!")


    logging.info("Extracting the data from the URL")

    url = load_yaml("param.yaml")["url"]
    df = get_data(url)

    logging.info("Done with data extraction")

    logging.info("Writing the dataframe to s3 bucket")
    writetos3 = ReadWriteFromS3.create_con_string(bucket_name,key)

    writetos3.writeToS3(df=df,
                       file_name="house_price")

    logging.info("Writing To S3 Bucket")

    logging.info("Reading from S3 bucket")
    bucket_name = "uk-naija-datascience-21032023"
    key = "uk-gdp-countries.parquet"
    logging.info(f"Reading file with name {key} from S3 bucket")
    readfroms3 = ReadWriteFromS3.create_con_string(bucket_name=bucket_name,
                                                   key=key)
    readfile = readfroms3.read_s3_file()
    print(readfile)