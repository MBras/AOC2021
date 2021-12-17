# transmission
#t = "D2FE28"
#t = "38006F45291200"
#t = "EE00D40C823060"
#t = "8A004A801A8002F478"
#t = "620080001611562C8802118E34"
#t = "C0015000016115A2E0802F182340"
#t = "A0016C880162017C3686B18A3D4780"
t = "C20D7900A012FB9DA43BA00B080310CE3643A0004362BC1B856E0144D234F43590698FF31D249F87B8BF1AD402389D29BA6ED6DCDEE59E6515880258E0040A7136712672454401A84CE65023D004E6A35E914BF744E4026BF006AA0008742985717440188AD0CE334D7700A4012D4D3AE002532F2349469100708010E8AD1020A10021B0623144A20042E18C5D88E6009CF42D972B004A633A6398CE9848039893F0650048D231EFE71E09CB4B4D4A00643E200816507A48D244A2659880C3F602E2080ADA700340099D0023AC400C30038C00C50025C00C6015AD004B95002C400A10038C00A30039C0086002B256294E0124FC47A0FC88ACE953802F2936C965D3005AC01792A2A4AC69C8C8CA49625B92B1D980553EE5287B3C9338D13C74402770803D06216C2A100760944D8200008545C8FB1EC80185945D9868913097CAB90010D382CA00E4739EDF7A2935FEB68802525D1794299199E100647253CE53A8017C9CF6B8573AB24008148804BB8100AA760088803F04E244480004323BC5C88F29C96318A2EA00829319856AD328C5394F599E7612789BC1DB000B90A480371993EA0090A4E35D45F24E35D45E8402E9D87FFE0D9C97ED2AF6C0D281F2CAF22F60014CC9F7B71098DFD025A3059200C8F801F094AB74D72FD870DE616A2E9802F800FACACA68B270A7F01F2B8A6FD6035004E054B1310064F28F1C00F9CFC775E87CF52ADC600AE003E32965D98A52969AF48F9E0C0179C8FE25D40149CC46C4F2FB97BF5A62ECE6008D0066A200D4538D911C401A87304E0B4E321005033A77800AB4EC1227609508A5F188691E3047830053401600043E2044E8AE0008443F84F1CE6B3F133005300101924B924899D1C0804B3B61D9AB479387651209AA7F3BC4A77DA6C519B9F2D75100017E1AB803F257895CBE3E2F3FDE014ABC"

# part 2
#t = "C200B40A82" 
#t = "04005AC33890"
#t = "880086C3E88112"
#t = "CE00C43D881120" 
#t = "D8005AC2A8F0"
#t = "F600BC2D8F"
#t = "9C005AC2F8F0"
#t = "9C0141080250320F1802104A08"

print("Input: " + t)

# score store to add all version numbers
score = 0

# binary representation of the transmission
h_size = len(t) * 4
tb = (bin(int(t, 16))[2:]).zfill(h_size)
# prepad to a multip,le of 4 bits
tb = "0" * (-len(tb) % 4) + tb

# returns the number of bits processed this run
def pt(t): 
    # to keep track of the part 1 score
    global score

    print("\nProcessing " + t)

    #packet version
    pv = int(t[0:3], 2)
    print("Packet version: " + str(pv))
    score += pv

    # type id
    tid = int(t[3:6], 2)
    print("Type ID: " + str(tid))

    if tid == 4:
        # type id 4 -> literal value
        done = False
        bc = 0 # block counter to calculate padding
        binval = ""
        while not(done):
            # read block of 5 bits
            block = t[6 + bc * 5:6 + bc * 5 + 5]
            binval += block[1:5]
            bc += 1

            # if first bit is 0 than we're done
            if block[0] == "0":
                done = True

        val = int(binval,2)
        print("Literal value: " + str(val))

        # return the number of bits processed
        return (6 + bc * 5, val)

        # make sure to deal with possible padding
    else:
        # type id != 4 means operator
        
        # length type id
        ltid = t[6]
        print("Lenght type ID: "  + str(ltid))


        bits = 0
        val = []
        if ltid == "0":
            l = int(t[7:7 + 15], 2)
            print("Read " + str(l) + " bits for the subpackets.")

            while bits < l:
                [b, v] = pt(t[22 + bits:])
                bits += b
                val.append(v)  
            rval = 22 + l
        else:
            l = int(t[7:7 + 11], 2)
            print("Read " + str(l) + " subpackets")
            
            for i in range(l):
                [b, v] = pt(t[18 + bits:])
                bits += b
                val.append(v)
            # return all processed bits
            rval = 18 + bits
        
        # base on type id, perform an operation
        if tid == 0:
            print("SUM")
            print(val)
            print(sum(val))
            tv = sum(val)
        elif tid == 1:
            print("PRODUCT")
            print(val)
            tv = 1
            for v in val:
                tv *= v
        elif tid == 2:
            print("MIN")
            print(val)
            print(min(val))
            tv = min(val)
        elif tid == 3:
            print("MAX")
            print(val)
            print(max(val))
            tv = max(val)
        elif tid == 5:
            print("GT")
            print(val)
            tv = 1 if val[0] > val[1] else 0
        elif tid == 6:
            print("LT")
            print(val)
            tv = 1 if val[0] < val[1] else 0
        elif tid == 7:
            print("EQUAL")
            print(val)
            tv = 1 if val[0] == val[1] else 0
        
        return rval, tv

[notused, value] = pt(tb)

print("\nScore: " + str(score))
print("Value: " + str(value))
