input_signal = '03036732577212944063491565474664'
#input_signal = '59769638638635227792873839600619296161830243411826562620803755357641409702942441381982799297881659288888243793321154293102743325904757198668820213885307612900972273311499185929901117664387559657706110034992786489002400852438961738219627639830515185618184324995881914532256988843436511730932141380017180796681870256240757580454505096230610520430997536145341074585637105456401238209187118397046373589766408080120984817035699228422366952628344235542849850709181363703172334788744537357607446322903743644673800140770982283290068502972397970799328249132774293609700245065522290562319955768092155530250003587007804302344866598232236645453817273744027537630'
pattern = [0,1,0,-1]

def calc_digit (string, count):
    tmp_calc = []; tmp_sum = 0; idx = 0; j = 0; first = 0
    while j < len(string):         # calc of 1 digit of the signal
        if idx == 0 and j == 0:     # Ausnahme für das erste Element
            if count == 0: idx = 1
            else:
                count -= 1
                first = True
        for k in range (count+1):         # calc with the pattern logic
            tmp_calc.append(int(string[j])*pattern[idx])
            j += 1
            if j >= len(string): break
        if first == True:
            count += 1
            first = False
        if idx == 3: idx = 0
        else: idx += 1
    for j in tmp_calc:
        tmp_sum += j
    erg = str(tmp_sum)[-1]
    return (erg)

act_signal = input_signal*10000
for phase in range (101):     # count of the rounds of calculation
    tmp_signal = ''
    print ('Signal after ',phase,' rounds: ', act_signal)
    for i in range(len(act_signal)):        # for one whole calculation of the signal
        tmp_digit = calc_digit(act_signal, i)
        tmp_signal += tmp_digit
    act_signal = tmp_signal




