import sys 
import traceback
from typing import Optional, cast 

class ResearchAnalystException(Exception): 
        def __init__(self, error_message, error_detail: Optional[object] = None):
            # Normalize the error message to ensure it's a string
            if isinstance(error_message, Exception):
                norm_msg = str(error_message)
            else:
                norm_msg = cast(str, error_message)

            # Resolve exc_info (suppors: sys module, Exception object, or current context)
            exc_type = exc_value = exc_tb = None 
            if error_detail is None:
                exc_type, exc_value, exc_tb = sys.exc_info()
            else: 
                if hasattr(error_detail, "exc_info"):
                    exc_info_obj = cast(sys, error_detail)
                    exc_type, exc_value, exc_tb = exc_info_obj.exc_info()
                elif isinstance(error_detail, Exception):
                    exc_value = error_detail
                    exc_type = type(error_detail)
                    exc_tb = error_detail.__traceback__
                else:
                    exc_type, exc_value, exc_tb = sys.exc_info()

            # Walk to the last frame to report the most relevant location
            last_tb = exc_tb 
            while last_tb and last_tb.tb_next:
                last_tb = last_tb.tb_next

            self.file_name = last_tb.tb_frame.f_code.co_filename if last_tb else "<unknown>"
            self.lineno = last_tb.tb_lineno if last_tb else -1
            self.error_message = norm_msg

            # Full pretty traceback (if available)
            if exc_type and exc_tb:
                self.traceback_str = ''.join(traceback.format_exception(exc_type, exc_value, exc_tb))
            else:
                self.traceback_str = "" 

            super().__init__(self.__str__())

        def __str__(self):
            # compact message representation 
            base = f'Error in [{self.file_name}] at line [{self.lineno}] | Message: {self.error_message}'
            if self.traceback_str:
                return f"{base}\nTraceback:\n{self.traceback_str}"
            
        def __repr__(self):
            return f'ResearchAnalystException({self.error_message!r}, {self.file_name!r}, {self.lineno!r})'
        
# if __name__ == "__main__":
#     # Demo # 1: Basic usage
#     try:
#         a = 1 / 0 
#     except Exception as e:
#         raise ResearchAnalystException("Division Failed", e) from e 
    
#     # Demo # 2: With custom message and exc_info
#     try:
#         a = int('abc')
#     except Exception as e:
#         raise ResearchAnalystException(e,sys)
    