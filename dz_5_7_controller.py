import dz_5_7_inp
import dz_5_7_import
import dz_5_7_exp
import dz_5_7_logger

def do_it():
    if dz_5_7_inp.mod() == '1':
        info = dz_5_7_inp.exp_data()
        dz_5_7_exp.exp_contact(info)
        dz_5_7_logger.log_info(info)
    else:
        info = dz_5_7_inp.inp_data()
        dz_5_7_import.imp_contact(info)
        dz_5_7_logger.log_info(info)