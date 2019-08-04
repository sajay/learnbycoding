import csv
import json
import pathlib

empDict = {}
LOG_TYPE_MAIN    = 0
LOG_TYPE_SUCCESS = 1
LOG_TYPE_ERROR   = 2
CONSOLE_OUTPUT_TRUE  = True
CONSOLE_OUTPUT_FALSE = False

class Employee:
    def __init__(self):
        self.emp_521 = ""
        self.emp_email       = ""
        self.emp_country_code = ""
        self.emp_org_division =""
        self.emp_id_status=""
        self.emp_mgr_521 =""
        self.emp_mgr_521_opm=""
        self.emp_email_mgr=""
        self.emp_mgr_email_opm=""
        self.emp_personnel_no= ""
    
    def __repr__(self):
        return repr(self.emp_521)

    def to_json(self):
        return(json.dumps(self.__dict__))

def out(line, log_type=LOG_TYPE_MAIN, do_console_output=CONSOLE_OUTPUT_TRUE):
    if do_console_output and log_type == LOG_TYPE_MAIN:
        print (line)        
       
def main():
    global empDict
    out("  Reading  Envison File " )
    emp_file_location= "//Users//smithaajay//projects//learnbycoding//learnpy//envision.csv"
    out(emp_file_location)
    try:
        with open(emp_file_location) as emp_file:
            reader = csv.reader(emp_file, delimiter='|')
            row_num   = 1
            for delimited_row in reader:
#                out(delimited_row)
                emp = Employee()
                emp.emp_521           = delimited_row[0].lower()
                emp.emp_email         = delimited_row[1].lower()
                emp.emp_country_code  = delimited_row[2].lower()
                emp.emp_org_division  = delimited_row[3].lower()
                emp.emp_id_status     = delimited_row[4].lower()
                emp.emp_mgr_521       = delimited_row[5].lower()
                emp.emp_mgr_521_opm   = delimited_row[6].lower()
                emp.emp_email_mgr     = delimited_row[7].lower()
                emp.emp_mgr_email_opm = delimited_row[8].lower()
                emp.emp_personnel_no  = delimited_row[9].lower()
                empDict[emp.emp_email] = emp
                row_num+=1
            #print(f'Processed {row_num} lines.')
            #out(str(len(empDict)))
            #for k,v in empDict.items():
            #    print(k,v)
    except Exception as e:
        out("File read failed: " + str(e))
        exit(0)

def retreive_employee(email):
    out("In retreive emp")
    if(len(empDict) > 0):
        try:
            empl = empDict[email.lower()]
        except KeyError:
            out('"%s" not found in dictionary' % email)
            empl = "Null"
        return empl

if __name__ == "__main__":
    main()        
    emp = retreive_employee('IVETA.ZARUPSKA@ALCON.COM')
    #emp = retreive_employee('test')
    #print(emp.__repr__())
    #print(emp.__dict__)
    print(emp.to_json())