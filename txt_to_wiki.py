with open('src.txt') as f:
    lines = f.readlines()
    
res_line = '{| class="wikitable sortable" style="text-align:center; font-size:90%" width="65%"\n'
# res_line += '!Place\n!Driver\n!Car\n!STAGE\n!DIFF\n!TOTAL\n!DIFF\n'
#res_line += '!POS\n!Driver\n!01\n!PTS\n'

head_formed = False

for line in lines:
    rest_str = line
    if head_formed:
        res_line += '|- \n'

    while len(rest_str) > 0:
        pos = rest_str.find('\t')
        if pos < 0:
            pos = len(rest_str)-1
        tab = rest_str[:pos] 
        rest_str = rest_str[pos+1:]
        if head_formed:
            res_line += f'| {tab}'
        else:
            res_line += f'!{tab}'
        res_line += "\n"
    
    if not head_formed:
        head_formed = True
         
res_line += '|}\n'

with open("Output.txt", "w") as text_file:
    text_file.write(res_line)
