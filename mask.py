import matplotlib.pyplot as plt
from sdchemotaxis import *
import numpy as np
import getmask as gm

w = 40   #dimensioni maze
h = 50

landscape =     "-------------------------------------#.o"\
                "-------------------------------------#.."\
                "-------------------------------------..."\
                "-------------------------------------..."\
                "-------------------------------------#.."\
                "-------------------------------------#.."\
                "-------------------------------------#.."\
                "-------------------------------------#.."\
                "-------------------------------------#.."\
                "-------------------------------------#.."\
                "-------------------------------------#.."\
                "-------------------------------------#.."\
                "-------------------------------------#.."\
                "-------------------------------------#.."\
                "-------------------------------------#.."\
                "-------------------------------------#.."\
                "-------------------------------------#.."\
                "-------------------------------------#.."\
                "-------------------------------------#.."\
                "-------------------------------------#.."\
                "-------------------------------------#.."\
                "-------------------------------------#.."\
                "-------------------------------------#.."\
                "-------------------------------------#.."\
                "-------------------------------------#.."\
                "-------------------------------------#.."\
                "-------------------------------------#.."\
                "-------------------------------------#.."\
                "-------------------------------------#.."\
                "-------------------------------------#.."\
                "-------------------------------------#.."\
                "-------------------------------------#.."\
                "-------------------------------------#.."\
                "-------------------------------------#.."\
                "-------------------------------------#.."\
                "-------------------------------------#.."\
                "-------------------------------------#.."\
                "-------------------------------------#.."\
                "-------------------------------------#.."\
                "-------------------------------------#.."\
                "-------------------------------------#.."\
                "-------------------------------------#.."\
                "-------------------------------------#.."\
                "-------------------------------------#.."\
                "-------------------------------------#.."\
                "-------------------------------------#.."\
                "-------------------------------------#.."\
                "######################################.."\
                "........................................"\
                "*......................................."

        


output1 = load_output("result\Simple_Rectangle\squared_40x50\exp-squared_40x50")                   #CHIAMATA DEGLI OUTPUT
output2 = load_output("result\Simple_Rectangle\squared_40x50\exp-squared_40x50_2")
# output3 = load_output("result\maze2_500\exp-maze2_101_150")
# output4 = load_output("result\maze2_500\exp-maze2_151_200")
# output5 = load_output("result\maze2_500\exp-maze2_201_250")
# output6 = load_output("result\maze2_500\exp-maze2_251_300")
# output7 = load_output("result\maze2_500\exp-maze2_301_350")
# output8 = load_output("result\maze2_500\exp-maze2_351_400")
# output9 = load_output("result\maze2_500\exp-maze2_401_450")
# output10 = load_output("result\maze2_500\exp-maze2_451_500")


mask = gm.get_mask(landscape, mask_symbol="-") 

def get_med_time(output):                              #DEFINISCO TEMPO SPESO NEL MIRAGGIO,
    times_mirage = []                                  #SUPERFICIE DEL MIRAGGIO, FRAZIONI DI SUPERIFICE 
    val_surf_mirage = []                               #E DI TEMPI
    end_time = []
    time_ratio = []
    surf_ratio = []
    
    for j in range(output.n_runs):                       #CICLO SU SIMULAZIONI
        times = output.times(run_index=j)
        DT = []
        x = [] 
        y = []
        t = []
        
        cell_map = output.build_cell_visit_map(run_index=j)                  #DEFINISCO LA MAPPA SU CUI SI MUOVE
        surf_mirage = mask.reshape((w*h))*cell_map                           #EFFETTIVA SUPERFICIE DEL MIRAGGIO

        
        for i in range(output.n_samples(run_index=j)):                       #CICLO SULLE POSIZIONI PER VEDERE SE ERA
                                                                              #NEL MIRAGGIO O MENO
            _x, _y = output.get_cell_position(i, run_index=j)
            if mask[_x+_y*w] == 1 :
                x.append(_x)
                y.append(_y)
                t.append(times[i])
                if i != 0:  
                    DT.append(times[i]-times[i-1]) 
       
        times_mirage.append(sum(DT))
        
        val_surf_mirage.append(np.count_nonzero(surf_mirage))
  
        end_time.append(times[len(times)-1])
        time_ratio.append(times_mirage[j]/end_time[j])
        surf_ratio.append(val_surf_mirage[j]/((w-3)*(h-3)))

    
    return times_mirage, val_surf_mirage, end_time, time_ratio, surf_ratio



t1, v1, end_time1, time_ratio1, surf_ratio1 = get_med_time(output1)
# print("gruppo 1", "\n")
# print(np.mean(t1),"\n")
# print(np.mean(v1),"\n")
# print(np.mean(end_time1), "\n")
sorted_ratio1 = sorted(time_ratio1)
sorted_surf_ratio1 = sorted(surf_ratio1)
# print(np.mean(sorted_ratio1), "\n")
# print(np.mean(sorted_surf_ratio1), "\n")


t2, v2, end_time2, time_ratio2, surf_ratio2 = get_med_time(output2)
# print("gruppo 2", "\n")
# print(np.mean(t2),"\n")
# print(np.mean(v2),"\n")
# print(np.mean(end_time2), "\n")
sorted_ratio2 = sorted(time_ratio2)
sorted_surf_ratio2 = sorted(surf_ratio2)
# print(np.mean(sorted_ratio2), "\n")
# print(np.mean(sorted_surf_ratio2), "\n")


# t3, v3, end_time3, time_ratio3, surf_ratio3 = get_med_time(output3)
# # print("gruppo 3", "\n")
# # print(np.mean(t3),"\n")
# # print(np.mean(v3),"\n")
# # print(np.mean(end_time3), "\n")
# sorted_ratio3 = sorted(time_ratio3)
# sorted_surf_ratio3 = sorted(surf_ratio3)
# # print(np.mean(sorted_ratio3), "\n")
# # print(np.mean(sorted_surf_ratio3), "\n")


# t4, v4, end_time4, time_ratio4, surf_ratio4 = get_med_time(output4)
# # print("gruppo 4", "\n")
# # print(np.mean(t4),"\n")
# # print(np.mean(v4),"\n")
# # print(np.mean(end_time4), "\n")
# sorted_ratio4 = sorted(time_ratio4)
# sorted_surf_ratio4 = sorted(surf_ratio4)
# # print(np.mean(sorted_ratio4), "\n")
# # print(np.mean(sorted_surf_ratio4), "\n")


# t5, v5, end_time5, time_ratio5, surf_ratio5 = get_med_time(output5)
# # print("gruppo 5", "\n")
# # print(np.mean(t5),"\n")
# # print(np.mean(v5),"\n")
# # print(np.mean(end_time1), "\n")
# sorted_ratio5 = sorted(time_ratio5)
# sorted_surf_ratio5 = sorted(surf_ratio5)
# # print(np.mean(sorted_ratio5), "\n")
# # print(np.mean(sorted_surf_ratio5), "\n")


# t6, v6, end_time6, time_ratio6, surf_ratio6 = get_med_time(output6)
# # print("gruppo 6", "\n")
# # print(np.mean(t6),"\n")
# # print(np.mean(v6),"\n")
# # print(np.mean(end_time6), "\n")
# sorted_ratio6 = sorted(time_ratio6)
# sorted_surf_ratio6 = sorted(surf_ratio6)
# # print(np.mean(sorted_ratio6), "\n")
# # print(np.mean(sorted_surf_ratio6), "\n")


# t7, v7, end_time7, time_ratio7, surf_ratio7 = get_med_time(output7)
# # print("gruppo 7", "\n")
# # print(np.mean(t7),"\n")
# # print(np.mean(v7),"\n")
# # print(np.mean(end_time7), "\n")
# sorted_ratio7 = sorted(time_ratio7)
# sorted_surf_ratio7 = sorted(surf_ratio7)
# # print(np.mean(sorted_ratio7), "\n")
# # print(np.mean(sorted_surf_ratio7), "\n")


# t8, v8, end_time8, time_ratio8, surf_ratio8 = get_med_time(output8)
# # print("gruppo 8", "\n")
# # print(np.mean(t8),"\n")
# # print(np.mean(v8),"\n")
# # print(np.mean(end_time8), "\n")
# sorted_ratio8 = sorted(time_ratio8)
# sorted_surf_ratio8 = sorted(surf_ratio8)
# # print(np.mean(sorted_ratio8), "\n")
# # print(np.mean(sorted_surf_ratio8), "\n")


# t9, v9, end_time9, time_ratio9, surf_ratio9 = get_med_time(output9)
# # print("gruppo 9", "\n")
# # print(np.mean(t9),"\n")
# # print(np.mean(v9),"\n")
# # print(np.mean(end_time9), "\n")
# sorted_ratio9 = sorted(time_ratio9)
# sorted_surf_ratio9 = sorted(surf_ratio9)
# # print(np.mean(sorted_ratio9))
# # print(np.mean(sorted_surf_ratio9))


# t10, v10, end_time10, time_ratio10, surf_ratio10 = get_med_time(output10)
# # print("gruppo 10", "\n")
# # print(np.mean(t10),"\n")
# # print(np.mean(v10),"\n")
# # print(np.mean(end_time10), "\n")
# sorted_ratio10 = sorted(time_ratio10)
# sorted_surf_ratio10 = sorted(surf_ratio10)
# # print(np.mean(sorted_ratio10), "\n")
# print(np.mean(sorted_surf_ratio10), "\n")

m1 = np.mean(sorted_surf_ratio1)
m2 = np.mean(sorted_surf_ratio2)
# m3 = np.mean(sorted_surf_ratio3)
# m4 = np.mean(sorted_surf_ratio4)
# m5 = np.mean(sorted_surf_ratio5)
# m6 = np.mean(sorted_surf_ratio6)
# m7 = np.mean(sorted_surf_ratio7)
# m8 = np.mean(sorted_surf_ratio8)
# m9 = np.mean(sorted_surf_ratio9)
# m10 = np.mean(sorted_surf_ratio10)

g1 = np.mean(sorted_ratio1)
g2 = np.mean(sorted_ratio2)
# g3 = np.mean(sorted_ratio3)
# g4 = np.mean(sorted_ratio4)
# g5 = np.mean(sorted_ratio5)
# g6 = np.mean(sorted_ratio6)
# g7 = np.mean(sorted_ratio7)
# g8 = np.mean(sorted_ratio8)
# g9 = np.mean(sorted_ratio9)
# g10 = np.mean(sorted_ratio10)


Media_ratio_tempo = (g1+g2)/2
Media_ratio_superficie = (m1+m2)/2
print(Media_ratio_superficie, "\n")
print(Media_ratio_tempo, "\n")
#print(m1, "\n")
#print(g1, "\n")

plt.scatter(sorted_ratio1, sorted_surf_ratio1)
plt.scatter(sorted_ratio2, sorted_surf_ratio2)
# plt.scatter(sorted_ratio2, sorted_surf_ratio3)
# plt.scatter(sorted_ratio2, sorted_surf_ratio4)
# plt.scatter(sorted_ratio2, sorted_surf_ratio5)
# plt.scatter(sorted_ratio2, sorted_surf_ratio6)
# plt.scatter(sorted_ratio2, sorted_surf_ratio8)
# plt.scatter(sorted_ratio2, sorted_surf_ratio9)
# plt.scatter(sorted_ratio2, sorted_surf_ratio10)
plt.show()


# plt.plot(sorted_surf_ratio1, S1)
# plt.plot(sorted_surf_ratio2, S2)
# plt.plot(sorted_surf_ratio2, S3)
# plt.plot(sorted_surf_ratio2, S4)
# plt.plot(sorted_surf_ratio2, S5)
#plt.plot(sorted_surf_ratio2, S6)
# plt.plot(sorted_surf_ratio2, S7)
# plt.plot(sorted_surf_ratio2, S8)
# plt.plot(sorted_surf_ratio2, S9)
# plt.plot(sorted_surf_ratio2, S10)
# plt.show()

# mediaR = []
# mediaS = []
# media_sorted_ratio = []
# media_sorted_surf_ratio = []


# for i in range(len(R1)):
#     mediaR.append((R1[i] + R2[i] + R3[i]+ R4[i]+ R5[i]+ R6[i]+ R7[i]+ R8[i]+ R9[i]+ R10[i]) / 10)




# for i in range(len(S1)):
#     mediaS.append((S1[i] + S2[i] + S3[i]+ S4[i]+ S5[i]+ S6[i]+ S7[i]+ S8[i]+ S9[i]+ S10[i]) / 10)




# for i in range(len(sorted_ratio1)):
#     media_sorted_ratio.append((sorted_ratio1[i] + sorted_ratio2[i] + sorted_ratio3[i]+ sorted_ratio4[i]+ sorted_ratio5[i]+ sorted_ratio6[i]+ sorted_ratio7[i]+ sorted_ratio8[i]+ sorted_ratio9[i]+ sorted_ratio10[i]) / 10)



# for i in range(len(sorted_surf_ratio1)):
#     media_sorted_surf_ratio.append((sorted_surf_ratio1[i] + sorted_surf_ratio2[i] + sorted_surf_ratio3[i]+ sorted_surf_ratio4[i]+ sorted_surf_ratio5[i]+ sorted_surf_ratio6[i]+ sorted_surf_ratio7[i]+ sorted_surf_ratio8[i]+ sorted_surf_ratio9[i]+ sorted_surf_ratio10[i]) / 10)




# plt.plot(media_sorted_ratio, mediaR)                                                     #PLOT 
# plt.show()


# plt.plot(media_sorted_surf_ratio, mediaS)
# plt.show()

for j in range (output1.n_runs):
    for i in range(output1.n_samples()):
        output1.plot_chem_state(j, i);
        plt.show()

# output3.plot_cell_path()
# plt.show()

# output4.plot_cell_path()
# plt.show()

# output5.plot_cell_path()
# plt.show()

# #output6.plot_cell_path()
# #plt.show()

# output7.plot_cell_path()
# plt.show()

# output8.plot_cell_path()
# plt.show()

# output9.plot_cell_path()
# plt.show()

# output10.plot_cell_path()
# plt.show()


output1.plot_cell_visit_frequency_map()
output2.plot_cell_visit_frequency_map()
# output3.plot_cell_visit_frequency_map()
# output5.plot_cell_visit_frequency_map()
# output6.plot_cell_visit_frequency_map()
# output7.plot_cell_visit_frequency_map()
# output8.plot_cell_visit_frequency_map()
# output9.plot_cell_visit_frequency_map()
# output10.plot_cell_visit_frequency_map()
plt.colorbar(im, label="visit frequency")
plt.show()
mask.py
Visualizzazione di mask.py.