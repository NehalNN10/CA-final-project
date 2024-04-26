# x = input().strip().split()
# print(x)

# x = ['{inst_mem[3],', 'inst_mem[2],', 'inst_mem[1],', 'inst_mem[0]}', '=', "32'h000000b3;", '{inst_mem[7],', 'inst_mem[6],', 'inst_mem[5],', 'inst_mem[4]}', '=', "32'h00400793;", '{inst_mem[11],', 'inst_mem[10],', 'inst_mem[9],', 'inst_mem[8]}', '=', "32'h00300813;", '{inst_mem[15],', 'inst_mem[14],', 'inst_mem[13],', 'inst_mem[12]}', '=', "32'h00500893;", '{inst_mem[19],', 'inst_mem[18],', 'inst_mem[17],', 'inst_mem[16]}', '=', "32'h00200913;", '{inst_mem[23],', 'inst_mem[22],', 'inst_mem[21],', 'inst_mem[20]}', '=', "32'h00100993;", '{inst_mem[27],', 'inst_mem[26],', 'inst_mem[25],', 'inst_mem[24]}', '=', "32'h00400513;", '{inst_mem[31],', 'inst_mem[30],', 'inst_mem[29],', 'inst_mem[28]}', '=', "32'h00500593;", '{inst_mem[35],', 'inst_mem[34],', 'inst_mem[33],', 'inst_mem[32]}', '=', "32'h00f53023;", '{inst_mem[39],', 'inst_mem[38],', 'inst_mem[37],', 'inst_mem[36]}', '=', "32'h01053423;", '{inst_mem[43],', 'inst_mem[42],', 'inst_mem[41],', 'inst_mem[40]}', '=', "32'h01153823;", '{inst_mem[47],', 'inst_mem[46],', 'inst_mem[45],', 'inst_mem[44]}', '=', "32'h01253c23;", '{inst_mem[51],', 'inst_mem[50],', 'inst_mem[49],', 'inst_mem[48]}', '=', "32'h03353023;", '{inst_mem[55],', 'inst_mem[54],', 'inst_mem[53],', 'inst_mem[52]}', '=', "32'h00000313;", '{inst_mem[59],', 'inst_mem[58],', 'inst_mem[57],', 'inst_mem[56]}', '=', "32'h04b30263;", '{inst_mem[63],', 'inst_mem[62],', 'inst_mem[61],', 'inst_mem[60]}', '=', "32'h406283b3;", '{inst_mem[67],', 'inst_mem[66],', 'inst_mem[65],', 'inst_mem[64]}', '=', "32'h00000413;", '{inst_mem[71],', 'inst_mem[70],', 'inst_mem[69],', 'inst_mem[68]}', '=', "32'h02740263;", '{inst_mem[75],', 'inst_mem[74],', 'inst_mem[73],', 'inst_mem[72]}', '=', "32'h00341493;", '{inst_mem[79],', 'inst_mem[78],', 'inst_mem[77],', 'inst_mem[76]}', '=', "32'h00950e33;", '{inst_mem[83],', 'inst_mem[82],', 'inst_mem[81],', 'inst_mem[80]}', '=', "32'h004e0e93;", '{inst_mem[87],', 'inst_mem[86],', 'inst_mem[85],', 'inst_mem[84]}', '=', "32'h000e3f03;", '{inst_mem[91],', 'inst_mem[90],', 'inst_mem[89],', 'inst_mem[88]}', '=', "32'h000ebf83;", '{inst_mem[95],', 'inst_mem[94],', 'inst_mem[93],', 'inst_mem[92]}', '=', "32'h01ff5a63;", '{inst_mem[99],', 'inst_mem[98],', 'inst_mem[97],', 'inst_mem[96]}', '=', "32'h00140413;", '{inst_mem[103],', 'inst_mem[102],', 'inst_mem[101],', 'inst_mem[100]}', '=', "32'hfe0000e3;", '{inst_mem[107],', 'inst_mem[106],', 'inst_mem[105],', 'inst_mem[104]}', '=', "32'h00130313;", '{inst_mem[111],', 'inst_mem[110],', 'inst_mem[109],', 'inst_mem[108]}', '=', "32'hfc0006e3;", '{inst_mem[115],', 'inst_mem[114],', 'inst_mem[113],', 'inst_mem[112]}', '=', "32'h01eeb023;", '{inst_mem[119],', 'inst_mem[118],', 'inst_mem[117],', 'inst_mem[116]}', '=', "32'h01fe3023;", '{inst_mem[123],', 'inst_mem[122],', 'inst_mem[121],', 'inst_mem[120]}', '=', "32'hfe0004e3;"]
# print(len(x))
# print(x)

# y = []
# for i in range(len(x)):
#     if i % 6 == 5:
#         y.append(x[i])

# y = ["32'h000000b3;", "32'h00400793;", "32'h00300813;", "32'h00500893;", "32'h00200913;", "32'h00100993;", "32'h00400513;", "32'h00500593;", "32'h00f53023;", "32'h01053423;", "32'h01153823;", "32'h01253c23;", "32'h03353023;", "32'h00000313;", "32'h04b30263;", "32'h406283b3;", "32'h00000413;", "32'h02740263;", "32'h00341493;", "32'h00950e33;", "32'h004e0e93;", "32'h000e3f03;", "32'h000ebf83;", "32'h01ff5a63;", "32'h00140413;", "32'hfe0000e3;", "32'h00130313;", "32'hfc0006e3;", "32'h01eeb023;", "32'h01fe3023;", "32'hfe0004e3;"]

# print(y)
# print(len(y))

# x = []
# for i in y:
#     x.append(i[4:12])
    
# print(x)

# x = ['00400513', '00500593', '00400793', '00300813', '00500893', '00200913', '00100993', '00f53023', '01053423', '01153823', '01253c23', '03353023', '00000313', '04b30263', '406283b3', '00000413', '02740263', '00341493', '00950e33', '004e0e93', '000e3f03', '000ebf83', '01ff5a63', '00140413', 'fe0000e3', '00130313', 'fc0006e3', '01eeb023', '01fe3023', 'fe0004e3']
# for i in range(len(x)):
#     print('{' + f"inst_mem[{4*i + 3}], inst_mem[{4*i + 2}], inst_mem[{4*i + 1}], inst_mem[{4*i}]" + "}" + f" = 32'h{x[i]};")
