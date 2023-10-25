import numpy as np
import matplotlib.pyplot as plt


Tx_Power_BS = 46
N = 3
Tx_Power_AT = 24
Ant_Gain_bs = 21
Penetrat_M = 15
IM = 1
f = 1.8  # Ghz

Bw_DL = 20 * 10**6
Bw_UL = 10 *10**6
Noise_Figure_Bs = 2.4
Noise_Figure_At = 6
SINR_DL = 2
SINR_UL = 4
MIMO_Gain = 3
Feeder_Loss = 2

Speed_light = 3 * 10**8 

Thermal_Noise_DL = -174 + 10*np.log10(Bw_DL)
Thermal_Noise_UL = -174 + 10*np.log10(Bw_UL)
Rx_Sens_BS = Thermal_Noise_DL + SINR_DL + Noise_Figure_Bs
Rx_Sens_AT = Thermal_Noise_UL + SINR_UL + Noise_Figure_At

ytik = np.arange(0,200)
#рассчет  уровень максимально допустимых потерь сигнала для DL and UL
MAPL_DL = Tx_Power_BS - Feeder_Loss + Ant_Gain_bs + MIMO_Gain - Penetrat_M - IM - Rx_Sens_AT

MAPL_UL = Tx_Power_AT - Feeder_Loss + Ant_Gain_bs + MIMO_Gain - Penetrat_M - IM - Rx_Sens_BS
 
def UMiNLOS():              # зависимость величины входных потерь радиосигнала от расстояния между приемником и передатчиком по UMiNLOS и FSPM
    d = np.arange(1,500)
    PLd = 26 * np.log10(f) + 22.7 + 36.7 * np.log10(d)

    FSPM = 20 * np.log10((4 * np.pi * f * 10**9 * d) / Speed_light )

 
    
    mapl_dl = [MAPL_DL] * len(d)
    mapl_ul = [MAPL_UL] * len(d)
    

    plt.figure(1)
    plt.ylabel("Потери сигнала, Дб")
    plt.xlabel("Расстояние между приемником и передатчиком, м")
    plt.plot(d,PLd)
    plt.plot(d,FSPM, "--")
    plt.plot(d, mapl_dl)
    plt.plot(d, mapl_ul, "--", "r")
    plt.yticks(np.arange(min(ytik), max(ytik)+1, 50))

    plt.legend(["UMiNLOS", "FSPM", "MAPL_DL", "MAPL_UL"], loc = 4)
    plt.grid(linewidth = 0.5)
    plt.show()

def Lclutter(key):           # Параметр для расчета модели cost231, пользователь выбирает местность
    if key == "DU":
        lutter = 3
    elif key == "U":
        lutter = 0
    elif key == "SU":
        lutter = - (2*(np.log10(f*10**3/28))**2 + 5.4)
    elif key == "RURAL":
        lutter = -(4.78 * (np.log10(f*10**3))**2 - 18.33 * np.log10(f*10**3) + 40.94)
    elif key == "ROAD":
        lutter = -(4.78 * (np.log10(f*10**3))**2 - 18.33 * np.log10(f*10**3) + 35.94)
    return lutter


def a(key):# Параметр для расчета модели cost231
    hms = 1
    if key == "DU":
        param_a = 3.2 *np.log10(11.75*hms)**2 - 4.97
    elif key == "SU":
        param_a = (1.1*np.log10(f*10**3) * hms - 1.56 * np.log10(f*10**3) - 0.8)
    return param_a


def s(d,hBS):        # составляющая для расчета модели cost231
    
    if d >= 1:
        param_s = 44.9 - 6.55 * np.log10(f*10**3)
    else:
        param_s =  (47.88 + 13.9 * np.log10(f*10**3) -13.9 * np.log10(hBS)) *  (1/np.log10(50))
    return param_s


def  COST_231():           # зависимость величины входных потерь радиосигнала от расстояния между приемником и передатчиком по UMiNLOS и COST_231
    d = np.arange(1,1000)
    
  
    
    mapl_dl = [MAPL_DL] * len(d)
    mapl_ul = [MAPL_UL] * len(d)
    A = 46.3
    B = 33.9 
    hBS = 50
    PLd = []
    for i in range(len(d)):
        PLd.append(A + B * np.log10(f*10**3) - 13.82 * np.log10(hBS) - a("DU") + s(d[i]*10**-3,hBS) * np.log10(d[i]*10**-3) + Lclutter("DU")) # urban

    FSPM = 20 * np.log10((4 * np.pi * f * 10**9 * d) / Speed_light )
    plt.figure(2)
    plt.ylabel("Потери сигнала, Дб")
    plt.xlabel("Расстояние между приемником и передатчиком, м")
    plt.plot(d,PLd)
    plt.plot(d,FSPM, "--")
    plt.plot(d, mapl_dl)
    plt.plot(d, mapl_ul, "--", "r")
    plt.yticks(np.arange(min(ytik), max(ytik)+1, 50))

    plt.legend(["COST_231", "FSPM", "MAPL_DL", "MAPL_UL"], loc = 4)
    plt.grid(linewidth = 0.5)
    plt.show()


def COST_231_UMiNLOS_Walfish(): # зависимость величины входных потерь радиосигнала от расстояния между приемником и передатчиком по UMiNLOS и FSPM и Walfish
    d = np.arange(1,7000)
    PLd_u = 26 * np.log10(f) + 22.7 + 36.7 * np.log10(d)
    PLd_w = 42.6 + 20 * np.log10(f*10**3) + 26*np.log10(d*10**-3)
   
    A = 46.3
    B = 33.9 
    hBS = 50
    PLd_c = []
    stem_radius = [0]*len(d)
    stem_radius[410] = MAPL_UL
    stem_radius[5500] = MAPL_UL
    
    for i in range(len(d)):
        PLd_c.append(A + B * np.log10(f*10**3) - 13.82 * np.log10(hBS) - a("DU") + s(d[i]*10**-3,hBS) * np.log10(d[i]*10**-3) + Lclutter("U")) # ROAD
   
   
    plt.figure(1)
    plt.ylabel("Потери сигнала, Дб")
    plt.xlabel("Расстояние между приемником и передатчиком, м")
    #plt.stem(d,stem_radius,"m" )
    plt.plot(d,PLd_c)
    plt.plot(d,PLd_u)
    plt.plot(d,PLd_w)
    plt.axhline (y=MAPL_DL, color='r', linestyle='--')
    plt.axhline (y=MAPL_UL, color='y', linestyle='--')
    plt.legend(["COST_231", "UMiNLOS", "Walfish-Ikegami" ,"MAPL_DL", "MAPL_UL"], loc = 4)
    plt.grid(linewidth = 0.5)
    plt.show()
Radius_U=410*10**-3
Radius_cost=5500*10**-3
UMiNLOS()
COST_231()

COST_231_UMiNLOS_Walfish()

S_big = 1.95 * Radius_cost**2
S_small = 1.95 * Radius_U**2
print("Уровень максимально допустимых потерь сигнала MAPL_UL = ", MAPL_UL, "dB")

print("Уровень максимально допустимых потерь сигнала MAPL_DL = ", MAPL_DL, "dB")

print("Радиус Базовой станции для модели UMiNLOS = ",Radius_U, "км" )

print("Радиус Базовой станции для модели COST_231 = ",Radius_cost, "км" )

print("Площадь одной базовой станции для модели UMiNLOS = ", S_small, "км кв" )

print("Площадь одной базовой станции для модели COST_231 = ", S_big, "км кв" )

S_usl_1 = 100
S_usl_2 = 4

count_sait_U= S_usl_2/S_small
count_sait_cost= S_usl_1/S_big
print("Необходимое количество базовых станций для модели UMiNLOS ",count_sait_U )

print("Необходимое количество базовых станций для модели COST_231 ",count_sait_cost )