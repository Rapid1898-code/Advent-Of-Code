with open('Advent19Input.txt') as f:
    src = [x.strip().split() for x in f.readlines()]
src_str= 'CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr'
#src_str= 'HOH'
#src_str= 'HOHOHO'

print(len(src_str))


def find_all(str,search):
    result_temp=[]
    for idx,char in enumerate(str):
        if len(search) == 1:
            if str[idx] == search: result_temp.append(idx)
        elif len(search) == 2:
            if str[idx:idx+2] == search: result_temp.append(idx)
        else: print('Error Def find_all')
    return(result_temp)

def check_mol():
    results = {'e'}
    count = 0
    while True:
        temp_result = set ()
        count += 1
        print(len(results))
        for result in results:
            for entry in src:
                pos_list = find_all (result, entry[0])
                for pos in pos_list:
                    if len (entry[0]) == 1:
                        res_str = result[:pos] + entry[2] + result[pos + 1:]
                    elif len (entry[0]) == 2:
                        res_str = result[:pos] + entry[2] + result[pos + 2:]
                    else:
                        print ('Error pos in pos_list')
                    if res_str == src_str: return(count)
                    if len(res_str) <= len(src_str): temp_result.add(res_str)
        results = temp_result

res=check_mol()
print(res)





