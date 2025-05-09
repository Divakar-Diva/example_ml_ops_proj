import sys
import traceback

class CustomException(Exception):
    def __init__(self,error_message:str):
        super().__init__(error_message)
        self.error_message=CustomException.get_details_of_error(error_message)
    @staticmethod
    def get_details_of_error(error_message):
        exc_typ,exc_val,exc_tb=sys.exc_info() 
        tb=traceback.extract_tb(exc_tb)  
        filename,line,func,_=tb[-1] 
        return f"Error: {error_message} | File: {filename}, Line: {line}, Function: {func}"
    def __str__(self):
        return self.error_message