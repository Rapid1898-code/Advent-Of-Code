with open('Advent19Input.txt') as f:
    src = [x.strip().split() for x in f.readlines()]
src_str= 'CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr'
#src_str= 'HOH'
#src_str= 'HOHOHO'

result_mol = []
print(src)

def find_all(str,search):
    result_temp=[]
    for idx,char in enumerate(str):
        if len(search) == 1:
            if str[idx] == search: result_temp.append(idx)
        elif len(search) == 2:
            if str[idx:idx+2] == search: result_temp.append(idx)
        else: print('Error Def find_all')
    return(result_temp)

for entry in src:
    pos_list = find_all(src_str,entry[0])
    for pos in pos_list:
        if len(entry[0]) == 1:
            res_str = src_str[:pos] + entry[2] + src_str[pos + 1:]
        elif len(entry[0]) == 2:
            res_str = src_str[:pos] + entry[2] + src_str[pos + 2:]
        else: print('Error pos in pos_list')
        result_mol.append(res_str)

result_set = set(result_mol)
print(result_set)
print(len(result_set))