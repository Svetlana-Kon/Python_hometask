import inp
import imprt
import exp
import log

def do_it():
    if inp.mod() == '1':
        info = inp.exp()
        exp.expp(info)
        log.log_info(info)
    else:
        info = inp.inpp()
        imprt.impo(info)
        log.log_info(info)


