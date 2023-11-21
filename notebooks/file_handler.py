ROOT_FILE_PATH = "/opt/spark/work-dir/delta/"
def reader():
    file_path = 
    return df

try:
    (empdf
      .write
      .format("delta")
      .mode("overwrite")
      .save("/opt/spark/work-dir/delta/tables/datq/employee")
    )
    logger.info("write data to the delta table")
except:
    logger.error("cannot write the data as delta table")