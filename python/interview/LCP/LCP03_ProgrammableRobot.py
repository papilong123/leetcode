from typing import List


# 不断循环检查满足的条件
class Solution:
    def robot(self, command: str, obstacles: List[List[int]], x: int, y: int) -> bool:
        s = {(a, b) for a, b in obstacles}
        i = j = 0
        while True:
            for c in command:
                if c == 'U':
                    j += 1
                elif c == 'R':
                    i += 1
                if i == x and j == y:
                    return True
                if (i, j) in s:
                    return False
                if i > x:
                    return False
                if j > y:
                    return False


command = "URUURUUUURUURRURUUURRRURRRUUUURUUUUUUUURRRRRUURURUURURUURURRRRRURRURRURUURUUUURURRRURURRRRURUUURURURUURUURURUURURRRRRUUUUURURRURRRURRURRUUUURURUUURRRURRURURURUURUUUURUUURUUURURUUURURUUURURRRUUUURRURURUUURUURRRUUUURUURRRURUURRUUURUUUUUUURUUUURURURRURUURRRURUUUUURRRRUURURRRRURRRRUUUURRRUUUURURRURRRURUURUUUURRRRURUURURUUURUURURURURUURURRRRURRUURUUURRUUURUUUUUUUURUUUURRUURRRUUUURUUUUURURURRUURRURRRRURRRRURRRURURUUURRRRURRRURUUURRUURRUUURRRRRUURRUURRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR"
obstacles = [[59895649, 19122366], [40108998, 12805415], [40110687, 12805914], [40105332, 12804220],
             [40109679, 12805572], [40105736, 12804220], [40109092, 12805430], [40112692, 12806506],
             [40110524, 12805905], [63226343, 20185759], [40108954, 12805359], [40107761, 12804946],
             [40106391, 12804462], [40110424, 12805790], [40105225, 12804218], [40106640, 12804588],
             [40106794, 12804704], [40109012, 12805426], [40113272, 12806640], [40106801, 12804704],
             [40109269, 12805430], [40112004, 12806354], [40112006, 12806361], [69546512, 22203518],
             [53674780, 17136309], [40105150, 12804134], [40105706, 12804220], [40109670, 12805552],
             [40105872, 12804334], [69539684, 22201335], [40106172, 12804462], [40112800, 12806635],
             [40110229, 12805672], [40105590, 12804220], [40106523, 12804462], [40107534, 12804946],
             [40108612, 12805188], [40113161, 12806640], [40111988, 12806329], [40109111, 12805430],
             [40112004, 12806353], [40110198, 12805672], [40107091, 12804704], [40110875, 12805914],
             [40105285, 12804220], [40109036, 12805430], [40110825, 12805914], [40110873, 12805914],
             [40112240, 12806398], [40113326, 12806640], [40110781, 12805914], [40106321, 12804462],
             [40108214, 12805139], [40105832, 12804281], [40105632, 12804220], [40110461, 12805834],
             [40112675, 12806478], [40111280, 12806147], [40106594, 12804528], [40112812, 12806640],
             [40112304, 12806398], [40109970, 12805672], [40111912, 12806232], [40112983, 12806640],
             [40105986, 12804462], [40105921, 12804390], [40105647, 12804220], [40111007, 12805914],
             [40105353, 12804220], [40109109, 12805430], [40111176, 12806023], [41574787, 13273224],
             [40109736, 12805640], [67612118, 21585958], [40109309, 12805430], [40110884, 12805914],
             [75225449, 24016583], [40107457, 12804906], [40111160, 12805995], [40105137, 12804126],
             [40108599, 12805188], [40111996, 12806340], [40111195, 12806055], [40105101, 12804071],
             [40109299, 12805430], [40110314, 12805672], [40109856, 12805672], [40111813, 12806156],
             [40106516, 12804462], [40113084, 12806640], [40113238, 12806640], [40110223, 12805672],
             [40113132, 12806640], [40107611, 12804946], [40107735, 12804946], [40111149, 12805983],
             [40106086, 12804462], [40111255, 12806131], [40110634, 12805914], [40108128, 12805027],
             [40112707, 12806535], [40111948, 12806290], [40111199, 12806062], [40108263, 12805188],
             [40108573, 12805188], [40112338, 12806398], [40111190, 12806050], [40113200, 12806640],
             [40106640, 12804586], [40111276, 12806142], [40105287, 12804220], [40107929, 12804946],
             [40108869, 12805254], [40112525, 12806398], [40109289, 12805430], [40105133, 12804120],
             [40105645, 12804220], [40108552, 12805188], [40112208, 12806398], [40112083, 12806398],
             [40112047, 12806394], [66683573, 21289513], [40105947, 12804434], [40111217, 12806075],
             [56057136, 17896877], [40112547, 12806398], [54506276, 17401752], [40108447, 12805188],
             [40110456, 12805828], [40111024, 12805914], [40110565, 12805914], [40107031, 12804704],
             [40108385, 12805188], [40105626, 12804220], [40113029, 12806640], [40107030, 12804704],
             [40106374, 12804462], [51600101, 16473922], [40105728, 12804220], [40112187, 12806398],
             [65132692, 20794369], [40110646, 12805914], [40107105, 12804704], [40109974, 12805672],
             [40399139, 12897898], [40106515, 12804462], [40106520, 12804462], [40111242, 12806100],
             [40112761, 12806589], [40108780, 12805188], [40107681, 12804946], [40107456, 12804898],
             [40109620, 12805489], [40105281, 12804220], [73396414, 23432656], [40107501, 12804946],
             [40109483, 12805430], [40106348, 12804462], [40107848, 12804946], [40107407, 12804846],
             [40112473, 12806398], [73833797, 23572309], [40108248, 12805177], [40106071, 12804462],
             [40112000, 12806341], [40106347, 12804462], [40108294, 12805188], [40105746, 12804220],
             [40107580, 12804946], [40108735, 12805188], [56389183, 18002917], [40109657, 12805534],
             [40110714, 12805914], [40106651, 12804606], [40105947, 12804433], [40108950, 12805357],
             [40112805, 12806636], [40109637, 12805505], [40109696, 12805585], [40109094, 12805430],
             [40110393, 12805742], [40110327, 12805672], [40105131, 12804120], [40109678, 12805569],
             [40106336, 12804462], [40111939, 12806274], [40112987, 12806640], [40106161, 12804462],
             [59421156, 18970895], [40106137, 12804462], [40109340, 12805430], [40108977, 12805395],
             [74863113, 23900889], [40108929, 12805338], [40112052, 12806398], [40106597, 12804530],
             [46886103, 14968936], [62659314, 20004693], [40113133, 12806640], [40111199, 12806061],
             [40105729, 12804220], [40109851, 12805672], [40107766, 12804946], [65144835, 20798253],
             [40111940, 12806275], [40106782, 12804704], [40106150, 12804462], [40106724, 12804689],
             [40112235, 12806398], [40107087, 12804704], [40105088, 12804052], [40112496, 12806398],
             [40109078, 12805430], [40108767, 12805188], [40106012, 12804462], [40108254, 12805184],
             [40113098, 12806640], [40107473, 12804926], [40111296, 12806156], [40108894, 12805287],
             [40110157, 12805672], [40106646, 12804601], [40113344, 12806640], [40113324, 12806640],
             [40106255, 12804462], [40107351, 12804765], [40112679, 12806484], [40113110, 12806640],
             [40108265, 12805188], [40108972, 12805389], [62976172, 20105870], [40109745, 12805651],
             [40107374, 12804794], [40107962, 12804946], [63089137, 20141949], [40107433, 12804869],
             [40112146, 12806398], [40110953, 12805914], [40109194, 12805430], [40106405, 12804462],
             [40107821, 12804946], [40110800, 12805914], [40109965, 12805672], [40108915, 12805320],
             [40110705, 12805914], [40112765, 12806603], [40112054, 12806398], [40106706, 12804679],
             [40107945, 12804946], [40109366, 12805430], [40109421, 12805430], [40105941, 12804421],
             [40108123, 12805024], [40109401, 12805430], [40111684, 12806156], [40108935, 12805340],
             [40110690, 12805914], [40105179, 12804167], [40106473, 12804462], [40113359, 12806640],
             [40109306, 12805430], [40107276, 12804704], [40112247, 12806398], [40108997, 12805412],
             [40106865, 12804704], [40105104, 12804076], [40106144, 12804462], [40109750, 12805652],
             [40111497, 12806156], [40110762, 12805914], [40108201, 12805126], [40109300, 12805430],
             [63888064, 20397011], [40108157, 12805078], [40106050, 12804462], [40108505, 12805188],
             [40108543, 12805188], [40113350, 12806640], [40110508, 12805894], [40108184, 12805106],
             [40111824, 12806156], [40109665, 12805547], [40106049, 12804462], [40105774, 12804220],
             [40110161, 12805672], [40109388, 12805430], [40105700, 12804220], [40110482, 12805856],
             [40111404, 12806156], [40110569, 12805914], [68270798, 21796230], [40106938, 12804704],
             [40107232, 12804704], [55478032, 17711995], [40109724, 12805615], [40106734, 12804696],
             [40109079, 12805430], [40108210, 12805132], [40111508, 12806156], [40106198, 12804462],
             [40112893, 12806640], [40112453, 12806398], [40111749, 12806156], [40109343, 12805430],
             [40105974, 12804452], [40105633, 12804220], [40105517, 12804220], [40111013, 12805914],
             [40112003, 12806347], [40107726, 12804946], [63746304, 20351747], [40112332, 12806398],
             [40112102, 12806398], [40110560, 12805914], [47939733, 15305325], [40107363, 12804779],
             [40112929, 12806640], [40111175, 12806021], [40108867, 12805249], [40110550, 12805914],
             [40108369, 12805188], [40113226, 12806640], [40108104, 12805006], [54407763, 17370322],
             [40109410, 12805430], [40109134, 12805430], [40106263, 12804462], [40106346, 12804462],
             [40108191, 12805111], [40107469, 12804924], [40107101, 12804704], [40110079, 12805672],
             [68247323, 21788756], [40106283, 12804462], [40111656, 12806156], [40105777, 12804220],
             [40112717, 12806546], [40107712, 12804946], [40112331, 12806398], [40112669, 12806473],
             [40112057, 12806398], [43491767, 13885237], [40111285, 12806152], [57911977, 18489071],
             [40109796, 12805672], [40110989, 12805914], [40107201, 12804704], [40112755, 12806582],
             [40106697, 12804654], [40109359, 12805430], [40111281, 12806147], [40108466, 12805188],
             [40108428, 12805188], [40109729, 12805620], [40108131, 12805033], [73098535, 23337565],
             [40107677, 12804946], [40113347, 12806640], [40106647, 12804603], [40107433, 12804871],
             [50435058, 16101969], [40111775, 12806156], [40110385, 12805738], [70394715, 22474317],
             [40105126, 12804115], [40111191, 12806051], [40107993, 12804946], [40105159, 12804144],
             [51867707, 16559381], [68922672, 22004344], [40111923, 12806250], [40108201, 12805125],
             [40111708, 12806156], [40110384, 12805735], [40113349, 12806640], [40109084, 12805430],
             [40113261, 12806640], [40106641, 12804595], [40112082, 12806398], [40107399, 12804832],
             [40105256, 12804220], [40106353, 12804462], [52259558, 16684461], [40106069, 12804462],
             [62077170, 19818835], [40107278, 12804704], [40112723, 12806549], [40105381, 12804220],
             [40108899, 12805291], [40108167, 12805090], [40108469, 12805188], [52457433, 16747657],
             [40109723, 12805614], [40109220, 12805430], [40107968, 12804946], [40108969, 12805375],
             [40112242, 12806398], [40113329, 12806640], [73384262, 23428759], [40105208, 12804206],
             [54420613, 17374398], [40106844, 12804704], [40105130, 12804118], [40109494, 12805430],
             [40107469, 12804925], [40111249, 12806120], [40108141, 12805050], [40109358, 12805430],
             [40112210, 12806398], [40106617, 12804556], [40109544, 12805430], [40109225, 12805430],
             [40113053, 12806640], [40110407, 12805765], [40109644, 12805510], [40110406, 12805763],
             [40105220, 12804216], [40106304, 12804462], [40106946, 12804704], [40109344, 12805430],
             [40110788, 12805914], [40107869, 12804946], [70325744, 22452307], [40107421, 12804856],
             [40107243, 12804704], [40113262, 12806640], [40106705, 12804673], [40111815, 12806156],
             [40110206, 12805672], [57503409, 18358628], [40110080, 12805672], [64835548, 20699498],
             [69576094, 22212976], [40106673, 12804624], [40107489, 12804933], [40109658, 12805537],
             [40113177, 12806640], [40109282, 12805430], [40108981, 12805406], [45506565, 14528515],
             [40108658, 12805188], [40106521, 12804462], [40108694, 12805188], [40112776, 12806619],
             [40108547, 12805188], [40105984, 12804460], [40110735, 12805914], [61483702, 19629401],
             [40110514, 12805900], [40106609, 12804540], [40108634, 12805188], [40110066, 12805672],
             [40109442, 12805430], [40108368, 12805188], [40110005, 12805672], [40110499, 12805890],
             [40111197, 12806056], [40108322, 12805188], [40105472, 12804220], [40112569, 12806398],
             [40112004, 12806357], [49740754, 15880327], [54581334, 17425730], [40111935, 12806265],
             [40107405, 12804844], [40108924, 12805330], [40113343, 12806640], [40108013, 12804946],
             [40109626, 12805494], [40110662, 12805914], [72960541, 23293481], [40107263, 12804704],
             [40112769, 12806610], [40111654, 12806156], [40105595, 12804220], [40108734, 12805188],
             [40106990, 12804704], [40112335, 12806398], [40106175, 12804462], [40106244, 12804462],
             [40110566, 12805914], [40110070, 12805672], [40112698, 12806518], [40107459, 12804911],
             [40106672, 12804624], [40106974, 12804704], [40106904, 12804704], [40108217, 12805151],
             [40112047, 12806396], [40110522, 12805904], [40107226, 12804704], [40110183, 12805672],
             [40105673, 12804220], [40112673, 12806477], [40111265, 12806136], [40113203, 12806640],
             [46655664, 14895352], [63093686, 20143401], [40112017, 12806376], [40105940, 12804420],
             [40112038, 12806388], [40108452, 12805188], [40105966, 12804447], [40110098, 12805672],
             [40107213, 12804704], [40105857, 12804306], [40105876, 12804339], [50729929, 16196123],
             [40107501, 12804944], [40105312, 12804220], [62068842, 19816184], [40111238, 12806098],
             [40111246, 12806115], [40108384, 12805188], [40110487, 12805865], [40105884, 12804356],
             [65643571, 20957461], [40106894, 12804704], [40110951, 12805914], [40106820, 12804704],
             [40108635, 12805188], [40113015, 12806640], [40112786, 12806622], [40110488, 12805872],
             [40108712, 12805188], [75331602, 24050497], [40108005, 12804946], [40111922, 12806245],
             [40109562, 12805430], [40105951, 12804438], [69889886, 22313140], [40110494, 12805881],
             [40111416, 12806156], [40107980, 12804946], [40109249, 12805430], [40106858, 12804704],
             [40106700, 12804667], [40109276, 12805430], [40109996, 12805672], [40107404, 12804843],
             [40107693, 12804946], [40110473, 12805850], [41436118, 13228987], [40111939, 12806270],
             [64044979, 20447111], [40112063, 12806398], [40110925, 12805914], [40112715, 12806544],
             [59997250, 19154825], [40107773, 12804946], [40108172, 12805096], [40107004, 12804704],
             [40105721, 12804220], [40112409, 12806398], [40108397, 12805188], [40106921, 12804704],
             [40106942, 12804704], [40106625, 12804565], [40107138, 12804704], [40109939, 12805672],
             [40108934, 12805340], [40107352, 12804766], [40111354, 12806156], [40109386, 12805430],
             [40113097, 12806640], [40110668, 12805914], [40110275, 12805672], [40112698, 12806516],
             [40107823, 12804946], [40110268, 12805672], [40107699, 12804946], [59414358, 18968735],
             [57176728, 18254339], [40111428, 12806156], [40109217, 12805430], [40109266, 12805430],
             [40112589, 12806398], [40111552, 12806156], [40108956, 12805362], [40110959, 12805914],
             [40106924, 12804704], [40107858, 12804946], [40107975, 12804946], [40113236, 12806640],
             [40110642, 12805914], [40110390, 12805740], [47760084, 15247966], [40105518, 12804220],
             [40110099, 12805672], [40108180, 12805102], [40106697, 12804652], [40111157, 12805992],
             [40111911, 12806231], [40107442, 12804883], [40108362, 12805188], [40105609, 12804220],
             [40110495, 12805883], [41428502, 13226527], [40110669, 12805914], [40110533, 12805913],
             [40109657, 12805533], [40108454, 12805188], [40110684, 12805914], [40105149, 12804134],
             [40105689, 12804220], [40111539, 12806156], [40111947, 12806289], [40108220, 12805154],
             [60407337, 19285754], [40109292, 12805430], [56404318, 18007736], [40106731, 12804692],
             [40112853, 12806640], [62176497, 19850571], [40108871, 12805255], [40106824, 12804704],
             [40105253, 12804220], [40109979, 12805672], [55462880, 17707170], [40107445, 12804887],
             [40105634, 12804220], [40109937, 12805672], [40109424, 12805430], [40106022, 12804462],
             [40110048, 12805672], [40111167, 12806012], [56577884, 18063132], [40113339, 12806640],
             [40113058, 12806640], [40109650, 12805525], [40106451, 12804462], [40105212, 12804206],
             [40106418, 12804462], [40105883, 12804353], [40112788, 12806623], [40109941, 12805672],
             [40109037, 12805430], [52176188, 16657854], [40105710, 12804220], [42219855, 13479182],
             [40107473, 12804925], [40108364, 12805188], [40111747, 12806156], [40111772, 12806156],
             [40112714, 12806540], [40106192, 12804462], [40108393, 12805188], [40109416, 12805430],
             [40105845, 12804290], [40106997, 12804704], [40105354, 12804220], [40111154, 12805991],
             [40110940, 12805914], [40111630, 12806156], [40112657, 12806459], [40106635, 12804582],
             [40112886, 12806640], [40112996, 12806640], [40106184, 12804462], [40105130, 12804117],
             [40108464, 12805188], [40105215, 12804207], [40110990, 12805914], [40111970, 12806309],
             [40111505, 12806156], [40109829, 12805672], [40112002, 12806346], [40109719, 12805612],
             [40110227, 12805672], [40111637, 12806156], [40110385, 12805739], [40108915, 12805318],
             [40108167, 12805094], [40105195, 12804198], [40111257, 12806134], [40108405, 12805188],
             [40109149, 12805430], [40107492, 12804938], [40109546, 12805430], [40105163, 12804148],
             [40110792, 12805914], [40108256, 12805184], [40106512, 12804462], [40106592, 12804523],
             [40110174, 12805672], [40111399, 12806156], [40112682, 12806493], [40107002, 12804704],
             [40105526, 12804220], [57329069, 18302962], [40113157, 12806640], [40110715, 12805914],
             [40112346, 12806398], [40111282, 12806147], [40111169, 12806015], [40108864, 12805249],
             [40110380, 12805733], [40107855, 12804946], [40105707, 12804220], [40106932, 12804704],
             [40112287, 12806398], [40108810, 12805188], [40109039, 12805430], [40110158, 12805672],
             [70009682, 22351412], [40108279, 12805188], [40107042, 12804704], [40108027, 12804946],
             [55211996, 17627078], [40109775, 12805672], [40106020, 12804462], [64145764, 20479276],
             [40113234, 12806640], [40105889, 12804362], [66265157, 21155928], [40109477, 12805430],
             [40110697, 12805914], [69913373, 22320629], [40112387, 12806398], [40106469, 12804462], [3017103, 963402],
             [40111023, 12805914], [40112779, 12806620], [40111989, 12806333], [40106650, 12804605],
             [40107190, 12804704], [40110405, 12805759], [40109692, 12805582], [40112390, 12806398],
             [40111770, 12806156], [40109692, 12805581], [40105261, 12804220], [40112706, 12806534],
             [40105251, 12804220], [40111565, 12806156], [40108226, 12805166], [40105188, 12804189],
             [56841680, 18147366], [40109761, 12805659], [40105392, 12804220], [40109834, 12805672],
             [40106257, 12804462], [40108993, 12805410], [40109923, 12805672], [40106754, 12804704],
             [53044128, 16934970], [40113116, 12806640], [40112099, 12806398], [40111246, 12806113],
             [40105232, 12804220], [40105970, 12804449], [40111188, 12806039], [40112479, 12806398],
             [40108291, 12805188], [40105943, 12804425], [40112702, 12806521], [40105978, 12804457],
             [42743643, 13646414], [40107111, 12804704], [40108941, 12805346], [40112361, 12806398],
             [40110938, 12805914], [40105292, 12804220], [40105310, 12804220], [40112590, 12806398],
             [54237942, 17316082], [40111621, 12806156], [40105685, 12804220], [40107896, 12804946],
             [40108921, 12805330], [40106684, 12804640], [40105941, 12804424], [40110415, 12805775],
             [40105340, 12804220], [40112273, 12806398], [66680551, 21288556], [40106253, 12804462],
             [40110401, 12805751], [40110492, 12805879], [56019250, 17884795], [40107203, 12804704],
             [40106716, 12804684], [40106952, 12804704], [40108909, 12805308], [40105676, 12804220],
             [40109511, 12805430], [40108695, 12805188], [40109018, 12805430], [40105461, 12804220],
             [40109218, 12805430], [40108141, 12805053], [40108222, 12805163], [40111948, 12806291],
             [40112115, 12806398], [40110108, 12805672], [40111932, 12806263], [67578012, 21575072],
             [40109076, 12805430], [40108652, 12805188], [40112731, 12806558], [40112312, 12806398],
             [40105723, 12804220], [71984263, 22981817], [40105834, 12804281], [40108747, 12805188],
             [40112026, 12806379], [40106001, 12804462], [40109635, 12805500], [40108993, 12805411],
             [40111002, 12805914], [40110999, 12805914], [40112455, 12806398], [40113195, 12806640],
             [40109715, 12805606], [40112568, 12806398], [40106621, 12804564], [56048067, 17894001],
             [40105923, 12804393], [40113066, 12806640], [40106636, 12804582], [40109624, 12805491],
             [40110431, 12805799], [40108459, 12805188], [40109498, 12805430], [40107838, 12804946],
             [60848468, 19426578], [40109991, 12805672], [40108879, 12805263], [40107682, 12804946],
             [40107715, 12804946], [40110829, 12805914], [65794403, 21005608], [74227952, 23698143],
             [40106242, 12804462], [40110396, 12805750], [40109493, 12805430], [40111577, 12806156],
             [53162354, 16972705], [40110217, 12805672], [40105148, 12804131], [40113118, 12806640],
             [40106364, 12804462], [40106314, 12804462], [40109638, 12805506], [40109538, 12805430],
             [40110384, 12805738], [40106915, 12804704], [40112303, 12806398], [45480044, 14520050],
             [40108997, 12805413], [40107352, 12804767], [40105686, 12804220], [40105079, 12804045],
             [40108143, 12805053], [40109879, 12805672], [40108485, 12805188], [57106982, 18232067],
             [40112255, 12806398], [40108160, 12805084], [40108327, 12805188], [40107609, 12804946],
             [40108969, 12805376], [40105235, 12804220], [67729582, 21623439], [40105351, 12804220],
             [40105886, 12804358], [40107069, 12804704], [43661608, 13939500], [40109711, 12805599],
             [40106659, 12804613], [40112516, 12806398], [40107283, 12804704], [40105644, 12804220],
             [74783527, 23875488], [40110887, 12805914], [40111647, 12806156], [40107350, 12804765],
             [40107425, 12804861], [40112415, 12806398], [40109975, 12805672], [40110419, 12805782],
             [40113179, 12806640], [40109647, 12805514], [40112762, 12806595], [40108699, 12805188],
             [40109907, 12805672], [40108988, 12805409], [40107373, 12804788], [40107051, 12804704],
             [40112570, 12806398], [40109905, 12805672], [73423688, 23441358], [40112795, 12806628],
             [40111367, 12806156], [40113155, 12806640], [40112585, 12806398], [40109524, 12805430],
             [40107606, 12804946], [40110025, 12805672], [67314206, 21490836], [40107824, 12804946],
             [40105861, 12804315], [40106281, 12804462], [40107897, 12804946], [40113258, 12806640],
             [75526380, 24112664], [40105390, 12804220], [40110618, 12805914], [40112962, 12806640],
             [40113044, 12806640], [40109081, 12805430], [40110379, 12805732], [40106769, 12804704],
             [56125378, 17918683], [40105755, 12804220], [40105446, 12804220], [47706295, 15230811],
             [40111659, 12806156], [40109547, 12805430], [40105088, 12804048], [40107843, 12804946],
             [40109332, 12805430], [40109984, 12805672], [40106620, 12804561], [40112285, 12806398],
             [40105220, 12804213], [40112508, 12806398], [40111501, 12806156], [40112685, 12806500],
             [40108221, 12805159], [40113312, 12806640], [40109492, 12805430], [40112011, 12806371],
             [40105245, 12804220], [40111955, 12806298], [53076696, 16945355], [40110770, 12805914],
             [40108704, 12805188], [40112162, 12806398], [40112762, 12806598], [40109131, 12805430],
             [40106615, 12804550], [40106618, 12804556], [40109419, 12805430], [40106425, 12804462],
             [40108806, 12805188], [63664448, 20325615], [40108486, 12805188], [40111706, 12806156],
             [40105183, 12804183]]
x = 40105072
y = 12804036
res = Solution().robot(command, obstacles, x, y)
print(res)