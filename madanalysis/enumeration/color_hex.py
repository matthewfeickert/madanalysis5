################################################################################
#  
#  Copyright (C) 2012-2020 Jack Araz, Eric Conte & Benjamin Fuks
#  The MadAnalysis development team, email: <ma5team@iphc.cnrs.fr>
#  
#  This file is part of MadAnalysis 5.
#  Official website: <https://launchpad.net/madanalysis5>
#  
#  MadAnalysis 5 is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#  
#  MadAnalysis 5 is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with MadAnalysis 5. If not, see <http://www.gnu.org/licenses/>
#  
################################################################################


color_hex = {0:'#ffffff',\
1:'#000000',\
2:'#ff0000',\
3:'#00ff00',\
4:'#0000ff',\
5:'#ffff00',\
6:'#ff00ff',\
7:'#00ffff',\
8:'#59d354',\
9:'#5954d8',\
10:'#fefefe',\
11:'#c0b6ac',\
12:'#4c4c4c',\
13:'#666666',\
14:'#7f7f7f',\
15:'#999999',\
16:'#b2b2b2',\
17:'#cccccc',\
18:'#e5e5e5',\
19:'#f2f2f2',\
20:'#ccc6aa',\
21:'#ccc6aa',\
22:'#c1bfa8',\
23:'#bab5a3',\
24:'#b2a596',\
25:'#b7a39b',\
26:'#ad998c',\
27:'#9b8e82',\
28:'#876656',\
29:'#afcec6',\
30:'#84c1a3',\
31:'#89a8a0',\
32:'#829e8c',\
33:'#adbcc6',\
34:'#7a8e99',\
35:'#758991',\
36:'#688296',\
37:'#6d7a84',\
38:'#7c99d1',\
39:'#7f7f9b',\
40:'#aaa5bf',\
41:'#d3ce87',\
42:'#ddba87',\
43:'#bc9e82',\
44:'#c6997c',\
45:'#bf8277',\
46:'#ce5e60',\
47:'#aa8e93',\
48:'#a5777a',\
49:'#936870',\
50:'#d35954',\
51:'#9200ff',\
52:'#7a00ff',\
53:'#6200ff',\
54:'#4a00ff',\
55:'#3300ff',\
56:'#1b00ff',\
57:'#0300ff',\
58:'#0014ff',\
59:'#002cff',\
60:'#0044ff',\
61:'#005bff',\
62:'#0073ff',\
63:'#008bff',\
64:'#00a3ff',\
65:'#00bbff',\
66:'#00d2ff',\
67:'#00eaff',\
68:'#00fffb',\
69:'#00ffe3',\
70:'#00ffcc',\
71:'#00ffb4',\
72:'#00ff9c',\
73:'#00ff84',\
74:'#00ff6c',\
75:'#00ff55',\
76:'#00ff3d',\
77:'#00ff25',\
78:'#00ff0d',\
79:'#0aff00',\
80:'#22ff00',\
81:'#39ff00',\
82:'#51ff00',\
83:'#69ff00',\
84:'#81ff00',\
85:'#99ff00',\
86:'#b0ff00',\
87:'#c8ff00',\
88:'#e0ff00',\
89:'#f8ff00',\
90:'#ffee00',\
91:'#ffd600',\
92:'#ffbe00',\
93:'#ffa600',\
94:'#ff8e00',\
95:'#ff7700',\
96:'#ff5f00',\
97:'#ff4700',\
98:'#ff2f00',\
99:'#ff1700',\
100:'#ff0000',\
110:'#fefefe',\
201:'#5b5b5b',\
202:'#7a7a7a',\
203:'#b7b7b7',\
204:'#d6d6d6',\
205:'#890f0f',\
206:'#b71414',\
207:'#ea4747',\
208:'#ef7575',\
209:'#0f890f',\
210:'#14b714',\
211:'#47ea47',\
212:'#75ef75',\
213:'#0f0f89',\
214:'#1414b7',\
215:'#4747ea',\
216:'#7575ef',\
217:'#89890f',\
218:'#b7b714',\
219:'#eaea47',\
220:'#efef75',\
221:'#890f89',\
222:'#b714b7',\
223:'#ea47ea',\
224:'#ef75ef',\
225:'#0f8989',\
226:'#14b7b7',\
227:'#47eaea',\
228:'#75efef',\
390:'#ffffcc',\
391:'#ffff99',\
392:'#cccc99',\
393:'#ffff66',\
394:'#cccc66',\
395:'#999966',\
396:'#ffff33',\
397:'#cccc33',\
398:'#999933',\
399:'#666633',\
400:'#ffff00',\
401:'#cccc00',\
402:'#999900',\
403:'#666600',\
404:'#333300',\
406:'#ccffcc',\
407:'#99ff99',\
408:'#99cc99',\
409:'#66ff66',\
410:'#66cc66',\
411:'#669966',\
412:'#33ff33',\
413:'#33cc33',\
414:'#339933',\
415:'#336633',\
416:'#00ff00',\
417:'#00cc00',\
418:'#009900',\
419:'#006600',\
420:'#003300',\
422:'#ccffff',\
423:'#99ffff',\
424:'#99cccc',\
425:'#66ffff',\
426:'#66cccc',\
427:'#669999',\
428:'#33ffff',\
429:'#33cccc',\
430:'#339999',\
431:'#336666',\
432:'#00ffff',\
433:'#00cccc',\
434:'#009999',\
435:'#006666',\
436:'#003333',\
590:'#ccccff',\
591:'#9999ff',\
592:'#9999cc',\
593:'#6666ff',\
594:'#6666cc',\
595:'#666699',\
596:'#3333ff',\
597:'#3333cc',\
598:'#333399',\
599:'#333366',\
600:'#0000ff',\
601:'#0000cc',\
602:'#000099',\
603:'#000066',\
604:'#000033',\
606:'#ffccff',\
607:'#ff99ff',\
608:'#cc99cc',\
609:'#ff66ff',\
610:'#cc66cc',\
611:'#996699',\
612:'#ff33ff',\
613:'#cc33cc',\
614:'#993399',\
615:'#663366',\
616:'#ff00ff',\
617:'#cc00cc',\
618:'#990099',\
619:'#660066',\
620:'#330033',\
622:'#ffcccc',\
623:'#ff9999',\
624:'#cc9999',\
625:'#ff6666',\
626:'#cc6666',\
627:'#996666',\
628:'#ff3333',\
629:'#cc3333',\
630:'#993333',\
631:'#663333',\
632:'#ff0000',\
633:'#cc0000',\
634:'#990000',\
635:'#660000',\
636:'#330000',\
791:'#ffcc99',\
792:'#cc9966',\
793:'#996633',\
794:'#996600',\
795:'#cc9933',\
796:'#ffcc66',\
797:'#ff9900',\
798:'#ffcc33',\
799:'#cc9900',\
800:'#ffcc00',\
801:'#ff9933',\
802:'#cc6600',\
803:'#663300',\
804:'#993300',\
805:'#cc6633',\
806:'#ff9966',\
807:'#ff6600',\
808:'#ff6633',\
809:'#cc3300',\
810:'#ff3300',\
811:'#99ff33',\
812:'#66cc00',\
813:'#336600',\
814:'#339900',\
815:'#66cc33',\
816:'#99ff66',\
817:'#66ff00',\
818:'#66ff33',\
819:'#33cc00',\
820:'#33ff00',\
821:'#ccff99',\
822:'#99cc66',\
823:'#669933',\
824:'#669900',\
825:'#99cc33',\
826:'#ccff66',\
827:'#99ff00',\
828:'#ccff33',\
829:'#99cc00',\
830:'#ccff00',\
831:'#99ffcc',\
832:'#66cc99',\
833:'#339966',\
834:'#009966',\
835:'#33cc99',\
836:'#66ffcc',\
837:'#00ff66',\
838:'#33ffcc',\
839:'#00cc99',\
840:'#00ffcc',\
841:'#33ff99',\
842:'#00cc66',\
843:'#006633',\
844:'#009933',\
845:'#33cc66',\
846:'#66ff99',\
847:'#00ff99',\
848:'#33ff66',\
849:'#00cc33',\
850:'#00ff33',\
851:'#99ccff',\
852:'#6699cc',\
853:'#336699',\
854:'#003399',\
855:'#3366cc',\
856:'#6699ff',\
857:'#0066ff',\
858:'#3366ff',\
859:'#0033cc',\
860:'#0033ff',\
861:'#3399ff',\
862:'#0066cc',\
863:'#003366',\
864:'#006699',\
865:'#3399cc',\
866:'#66ccff',\
867:'#0099ff',\
868:'#33ccff',\
869:'#0099cc',\
870:'#00ccff',\
871:'#cc99ff',\
872:'#9966cc',\
873:'#663399',\
874:'#660099',\
875:'#9933cc',\
876:'#cc66ff',\
877:'#9900ff',\
878:'#cc33ff',\
879:'#9900cc',\
880:'#cc00ff',\
881:'#9933ff',\
882:'#6600cc',\
883:'#330066',\
884:'#330099',\
885:'#6633cc',\
886:'#9966ff',\
887:'#6600ff',\
888:'#6633ff',\
889:'#3300cc',\
890:'#3300ff',\
891:'#ff3399',\
892:'#cc0066',\
893:'#660033',\
894:'#990033',\
895:'#cc3366',\
896:'#ff6699',\
897:'#ff0066',\
898:'#ff3366',\
899:'#cc0033',\
900:'#ff0033',\
901:'#ff99cc',\
902:'#cc6699',\
903:'#993366',\
904:'#990066',\
905:'#cc3399',\
906:'#ff66cc',\
907:'#ff0099',\
908:'#cc0099',\
909:'#ff33cc',\
910:'#ff0099',\
920:'#cccccc',\
921:'#999999',\
922:'#666666',\
923:'#333333'\
}

