import sys

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_no = exc_tb.tb_lineno
    error_msg = 'Error Occured in python script [{0}] line number [{1}] error_message [{2 }]'.format(file_name,line_no,str(error))

    return error_msg





    class CustomException(Exception):
        def __init__(self, error_msg,error_detail:sys):
            super().__init__(error_msg)
        self.error_msg=error_message_detail(error_msg,error_detail=error_detail)
    
        def __str__(self):
            return self.error_message
