import string

key = [3, 4, 24, 32, 81, 98, 108, 168, 192, 228, 256, 312, 375, 500, 525, 588, 648, 671, 784, 847, 864, 1014, 1029, 1183, 1225, 1261, 1323, 1344, 1372, 1536, 1824, 2048, 2187, 2496, 2646, 2888, 2916, 3000, 3993, 4000, 4200, 4225, 4536, 4563, 4644, 4704, 5184, 5324, 5368, 6156, 6272, 6292, 6371, 6591, 6696, 6776, 6877, 6912, 8112, 8214, 8232, 8281, 8424, 8775, 8788, 9310, 9464, 9548, 9747, 9765, 9800, 10088, 10125, 10584, 10752, 10976, 11596, 12250, 12288, 12348, 12844, 13500, 14175, 14592, 14739, 14792, 15075, 15876, 16384, 17150, 17496, 17689, 17956, 18117, 19652, 19968, 20577, 21000, 21168, 21900, 22200, 22869, 23104, 23328, 23660, 24000, 25137, 26011, 27075, 27300, 27378, 27436, 27783, 28500, 31941, 31944, 32000, 32193, 33075, 33124, 33489, 33600, 33614, 33800, 34047, 35113, 35721, 35928, 36288, 36501, 36504, 37044, 37152, 37544, 37632, 37905, 39000, 39312, 39546, 40380, 40401, 40432, 41013, 41472, 41643, 42592, 42944, 44208, 46875, 47089, 47961, 48668, 49248, 50176, 50336, 50813, 50968, 52728, 53568, 54208, 55016, 55296, 57036, 57624, 59049, 61128, 62500, 64896, 65596, 65625, 65712, 65856, 66248, 66599, 67392, 70200, 70304, 71442, 71736, 72075, 73167, 73500, 74480, 74529, 75712, 75716, 76384, 77284, 77976, 78120, 78204, 78400, 78732, 80704, 81000, 81733, 83875, 84672, 86016, 87808, 89373, 92768, 95481, 95823, 95844, 97556, 98000, 98304, 98784, 99099, 102752, 103544, 103788, 105875, 107016, 107811, 107911, 108000, 112245, 113400, 113925, 114075, 116281, 116736, 117912, 118336, 119164, 120600, 120879, 122472, 123201, 123245, 124501, 125388, 126750, 127008, 127499, 127896, 128625, 130438, 131072, 132845, 136900, 137200, 139968, 141512, 141855, 143648, 143748, 144936, 147875, 151959, 153125, 156663, 157216, 157625, 158025, 159201, 159744, 160003, 164616, 165375, 165649, 166212, 166800, 167160, 168000, 169344, 169884, 171500, 172017, 172494, 175200, 177600, 177957, 178084, 179056, 180075, 180792, 182952, 184832, 185679, 186245, 186624, 189280, 191771, 192000, 196080, 197173, 198600, 199692, 201096, 201243, 201684, 202612, 205209, 205485, 206763, 208088, 215306, 216600, 218400, 219024, 219488, 221725, 221778, 222264, 223587, 223608, 224812, 225816, 226625, 227448, 228000, 230153, 235445, 236925, 237276, 238521, 245388, 247009, 251370, 255528, 255552, 255626, 255720, 256000, 257544, 257796, 260400, 263169, 263655, 264600, 264992, 267912, 268800, 268912, 270400, 271803, 272376, 273375, 275684, 279075, 280904, 284715, 285768, 287424, 290304, 290521, 292008, 292032, 296227, 296352, 297037, 297216, 300352, 301056, 303240, 303468, 305045, 311469, 312000, 312481, 313092, 314496, 316368, 318028, 323040, 323208, 323456, 328104, 330750, 331776, 333144, 333396, 334036, 335241, 340736, 343552, 345933, 346788, 347802, 352947, 353664, 361000, 364500, 364896, 368186, 369096, 371469, 375000, 376712, 377567, 382725, 383688, 386232, 389344, 393984, 397953, 399384, 400445, 401408, 402688, 405769, 406504, 407025, 407744, 415272, 415292, 420175, 421824, 423801, 428544, 428652, 432523, 432964, 433664, 438501, 440076, 440128, 442368, 444675, 446631, 446988, 448305, 453789, 456288, 460992, 463050, 469567, 470596, 472392, 473928, 477603, 480519, 481474, 484812, 487484, 489024, 489159, 490599, 496272, 499125, 500000, 500916, 506447, 519168, 524768, 525000, 525696, 526848, 528125, 529984, 530450, 530604, 532392, 532792, 532900, 539136, 543169, 546013, 555579, 561600, 562432, 565068, 566832, 567000, 570375, 570780, 571536, 573888, 574920, 576600, 578700, 580500, 585336, 588000, 589323, 591300, 595508, 595840, 596232, 599400, 601426, 602547, 605696, 605728, 611072, 616137, 616437, 617400, 617463, 618272, 623808, 624960, 625632, 627200, 628849, 629856, 638820, 641574, 645632, 647569, 648000, 650349, 653864, 654875, 659883, 665500, 671000, 672182, 677376, 678699, 680943, 681285, 685464, 685800, 686857, 688128, 695645, 696972, 698775, 702297, 702464, 714984, 717405, 718200, 720954, 729316, 731025, 737100, 739206, 740772, 742144, 749580, 750141, 760627, 763848, 766584, 766752, 769500, 773175, 780448, 782628, 784000, 786432, 786500, 790272, 791640, 792792, 796027, 796375, 806341, 806450, 812340, 816893, 821516, 821681, 822016, 823875, 825384, 828352, 830304, 837000, 847000, 856128, 859625, 862407, 862488, 863288, 864000, 869211, 871248, 893025, 893101, 894348, 897623, 897960, 902289, 904203, 907200, 907578, 907924, 911400, 911645, 912600, 917427, 918873, 919269, 919828, 930248, 933888, 943296, 945459, 946688, 948051, 953312, 955206, 964467, 964800, 967032, 970056, 979776, 983609, 985527, 985608, 985960, 987480, 990584, 992852, 996008, 997228, 1000188, 1002001, 1003104, 1013688, 1014000, 1015493, 1016064, 1019992, 1023168, 1023435, 1025661, 1026750, 1029000, 1035125, 1041859, 1043469, 1043504, 1048383, 1048576, 1053000, 1054729, 1061424, 1062760, 1067742, 1073296, 1073733, 1080107, 1090260, 1090827, 1091664, 1094275, 1094608, 1095200, 1096875, 1097600, 1098500, 1101772, 1107351, 1119744, 1120164, 1124361, 1125683, 1127357, 1132096, 1134840, 1136863, 1146380, 1149184, 1149984, 1152312, 1153425, 1159488, 1163750, 1167051, 1168716, 1175628, 1177813, 1180851, 1183000, 1185845, 1191729, 1192366, 1193500, 1193616, 1201883, 1203052, 1215672, 1218375, 1220625, 1225000, 1233537, 1253304, 1257728, 1261000, 1261491, 1264200, 1265625, 1267084, 1271403, 1273608, 1277952, 1280024, 1281424, 1282708, 1291836, 1294300, 1294947, 1295385, 1314036, 1316928, 1323000, 1325192, 1329696, 1331046, 1334400, 1335250, 1337280, 1344000, 1349634, 1354472, 1354752, 1354850, 1355719, 1359072, 1364656, 1369599, 1371951, 1372000, 1376136, 1379952, 1391520, 1401600, 1407133, 1420800, 1423656, 1424672, 1431644, 1431793, 1432448, 1433040, 1440600, 1446336, 1449175, 1449500, 1451190, 1463616, 1464463, 1474187, 1478656, 1479117, 1480437, 1485432, 1489960, 1492777, 1492992, 1513575, 1514240, 1520532, 1529045, 1531250, 1532856, 1534168, 1536000, 1536416, 1539972, 1540081, 1543500, 1548792, 1555848, 1556068, 1563852, 1565109, 1568640, 1574573, 1577384, 1580712, 1583064, 1584828, 1588800, 1592892, 1592956, 1594323, 1597536, 1605500, 1607151, 1608768, 1609944, 1613472, 1616955, 1620896, 1630475, 1641672, 1641916, 1643880, 1650456, 1654104, 1661688, 1664704, 1678391, 1687500, 1699992, 1715361, 1722448, 1732800, 1746507, 1747200, 1752192, 1752976, 1755831, 1755904, 1760913, 1771092, 1771788, 1771875, 1773800, 1774224, 1774560, 1778112, 1783067, 1788696, 1788864, 1792921, 1797576, 1798173, 1798496, 1803649, 1806528, 1811628, 1813000, 1817904, 1819584, 1824000, 1826132, 1830777, 1832061, 1836471, 1841224, 1842375, 1844164, 1849000, 1854944, 1860859, 1872300, 1877421, 1883560, 1884375, 1895400, 1898208, 1908168, 1910951, 1925781, 1928934, 1930838, 1936872, 1946025, 1953809, 1962597, 1963104, 1972156, 1972425, 1975509, 1976072, 1984009, 1984500, 1988623, 2010960, 2011373, 2012283, 2019108, 2044056, 2044224, 2044332, 2044416, 2045008, 2045760, 2048000, 2051199, 2060352, 2062368, 2083200, 2086668, 2087725, 2105352, 2107391, 2109240, 2111508, 2113244, 2114907, 2116800, 2119936, 2125764, 2140008, 2141748, 2143296, 2143750, 2150400, 2151296, 2158156, 2163200, 2174424, 2179008, 2185253, 2187000, 2196324, 2201651, 2205472, 2206791, 2211125, 2227758, 2228941, 2232600, 2244500, 2245509, 2247232, 2260713, 2264625, 2277720, 2286144, 2287148, 2296728, 2299392, 2312205, 2322432, 2324168, 2334280, 2336064, 2336256, 2345235, 2355353, 2358811, 2360232, 2369816, 2370816, 2370963, 2372903, 2376296, 2377728, 2390122, 2393209, 2402816, 2408448, 2413071, 2414916, 2425920, 2427744, 2440360, 2440893, 2456500, 2464965, 2472414, 2480016, 2484300, 2484469, 2491752, 2496000, 2499848, 2502643, 2503228, 2504736, 2515968, 2528407, 2530944, 2538847, 2544224, 2545452, 2548557, 2555956, 2572125, 2577987, 2579143, 2579325, 2580123, 2581656, 2584320, 2585664, 2587221, 2587648, 2587788, 2598544, 2599051, 2603349, 2616159, 2623796, 2624832, 2625000, 2634012, 2637600, 2646000, 2654208, 2665152, 2667168, 2672288, 2675673, 2681928, 2682127, 2684073, 2691325, 2705233, 2707132, 2725888, 2737500, 2738019, 2748416, 2757261, 2759484, 2766099, 2767464, 2770417]

def rot(let, amt):
    if let not in string.ascii_letters:
        return let
    k = ord(let)
    if k > 96:
        k -= 97
        return chr((k - amt) % 26 + 97)
    k -= 65
    return chr((k - amt) % 26 + 65)

ciphertext = open('psychic050801', 'r').readline()
print ''.join(rot(ciphertext[i], key[i]) for i in range(len(ciphertext)))
a = raw_input()