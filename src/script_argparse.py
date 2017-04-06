import argparse
    
"""
This is the docstring for a module named 'tutorial'.
Note that this file has to be in your current dir or
in a path listed in sys.path
"""

def my_print(msg="This is a script"):
    """
    This is the docstring for the my_print() method
    This will appear when you call help(my_print) or 
    if you type my_print? in ipython
    """
    print(msg)
    return None

def get_inputs():
    """Build input arg parser"""
   
    # Create defaults and help strings
    help_arg_d = 'days, int,    default = %(default)s'
    help_arg_p = 'path, string, default = %(default)s'
    default_arg_d = 7
    default_arg_p = "tmp"

    # Create a parse object
    parser = argparse.ArgumentParser( description='Tutorial Module' )

    # add args to parser object
    parser.add_argument('-d', '--days', dest='num_days',  help=help_arg_d, default=default_arg_d, type=int)
    parser.add_argument('-p', '--path', dest='file_path', help=help_arg_p, default=default_arg_p, type=str)

    args  = parser.parse_args()

    return args


def main():
    """
    This is the docstring for the main() method in the tutorial.py module
    """

    # Build parser and parse input args
    inputs = get_inputs()
    
    # Unpack the args (optional)
    num_days  = inputs.num_days
    file_path = inputs.file_path

    # Use input args
    my_msg = "Number of days = " + str(num_days) + "\n"
    my_msg += "File path = "     + file_path
    my_print(my_msg)

    return None

if __name__ == "__main__":
    main()
