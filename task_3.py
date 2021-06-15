def brackets(line):
    
    open_br = ['(', '[', '{']
    close_br = [')', ']', '}']
    dict_br = {'(': ')', '[': ']', '{': '}', ')': '(', ']': '[', '}': '{'}  
    
    last_open = []
    
    for i in line:
        if i not in dict_br:
            continue  
        
        elif i in open_br:
            last_open.append(i)
        
        elif i in close_br:
        
            if dict_br[i] != last_open[-1] or not last_open:
                return 'false'
            
            last_open.pop(-1)
                
    return 'true' if not last_open else 'false'

#brackets('[({})(o)) 0]()')
#get_ipython().run_line_magic('timeit', "brackets('[({})(o) 0]()')")
