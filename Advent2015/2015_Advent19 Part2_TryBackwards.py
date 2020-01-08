import re

with open('Advent19Input.txt') as f:
    src = [x.strip().split() for x in f.readlines()]
#src_str= 'CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr'
#src_str= 'HOH'
#src_str= 'HOHOHO'

def find_all(str,search):
    result_temp = []
    for match in re.finditer(search,str):
        result_temp.append(match.start())
    return(result_temp)

def check_mol():
    results = {'CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr'}
    #results = {'HOH'}
    #results = {'HOHOHO'}

    count = 0
    while True:
        temp_result = set ()
        count += 1
        print(len(results), count)
        for result in results:
            for entry in src:
                pos_list = find_all (result, entry[2])

                pos_list = pos_list[:1]

                for pos in pos_list:
                    res_str = result[:pos] + entry[0] + result[pos+len(entry[2]):]
                    if entry[0] == 'e':
                        if res_str == 'e': return(count)
                        else: continue
                    temp_result.add(res_str)

        temp_result = list(temp_result)
        temp_result.sort(key=len)
        results = temp_result[:10]
        results = set(results)


res=check_mol()
print(res)





