import sys
from src.logger import logging
#print the custom exception whenever the class CustomException is raised in try catch block.
# outcome -> print the script name, line number, error detail in a format.

def err_msg_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "error raised in script [{0}] in the line [{1}] and the error is [{2}]".format(file_name, exc_tb.tb_lineno,str(error))
    
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = err_msg_detail(error_message, error_detail=error_detail)
    def __str__(self):
        self.error_message


