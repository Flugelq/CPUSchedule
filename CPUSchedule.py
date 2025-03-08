import tkinter as tk
from tkinter import ttk

arrival_time = []
burst_time = []
priority = []

def test():
    if C_box.get() == "FCFS":
        FCFS()
    if C_box.get() == "優先權不可搶":
        priority_non()
    if C_box.get() == "SRT":
        SRT()
    if C_box.get() == "RR":
        RR()

def find_min_index(a_list):
    mini = min(a_list)
    count = -1
    for temp in a_list:
        count += 1
        if mini == temp:
            return count

def find_end_time(n_list, t_list, p):
    for temp in range(len(n_list)):
        if p == n_list[temp]:
            return t_list[temp + 1]

def find_end_time_DESC(n_list, t_list, p):
    for temp in range(len(n_list), 0, -1):
        if p == n_list[temp - 1]:
            return t_list[temp]

def update_list(index, value, Mylist):
    del Mylist[index]
    Mylist.insert(index, value)

def find_same_index(value, p_list):
    for i in range(len(p_list)):
        if value == p_list[i]:
            return i

def FCFS():
    count = len(arrival_time)
    arrival = []
    burst = []
    proc = []
    n_arrival = []
    n_burst = []
    n_proc = []
    time = []
    name = []
    tat = 0
    wt = 0
    
    for temp_c in range(count):
        arrival.append(int(arrival_time[temp_c].get()))
        burst.append(int(burst_time[temp_c].get()))
    for pre_t in range (count):
        proc.append(pre_t + 1)
    for temp in range(count):
        inx = find_min_index(arrival)
        n_arrival.append(arrival[inx])
        n_burst.append(burst[inx])
        n_proc.append(proc[inx])
        arrival.pop(inx)
        burst.pop(inx)
        proc.pop(inx)
    
    time.append(n_arrival[0])
    time.append(n_burst[0])
    name.append(n_proc[0])
    
    for i in range(count-1):
        if time[-1] < n_arrival[i + 1]:
            time.append(n_arrival[i + 1])
            time.append(n_arrival[i + 1] + n_burst[i + 1])
            name.append(0)
            name.append(n_proc[i + 1])
        else:
            time.append(time[-1] + n_burst[i + 1])
            name.append(n_proc[i + 1])
    
    end_time = []
    for j in range(count):
        end_time.append(find_end_time(name, time, j + 1))
        tat += end_time[j] - n_arrival[j]
    avg_tat = tat / 5
    wt = time[-1] / 5
    avg_wt = avg_tat - wt

    p_name = []
    for i in range(len(name)):
        p_name.append("P" + str(name[i]))
    
    avgtatVar.set("Average Turnaround Time")
    tat_resultVar.set(str(avg_tat))
    avgwtVar.set("Average Waiting Time")
    wt_resortVar.set(str(avg_wt))
# 圖
    # if name_lab.winfo_exists() or time_lab.winfo_exists():
    #     name_lab.place_forget()
    #     time_lab.place_forget()

    name_lab.config(text = ', '.join(p_name), font= "Helvetica 14 bold")
    time_lab.config(text = str(time), font= "Helvetica 15 bold")

    # for i in range(len(name)):
    #     name_lab = tk.Label(text = "P" + str(name[i]), font= "Helvetica 15 bold")
    #     name_lab.place(x = 100 + i * 55, y = 350)
    
    # for i in range(len(time)):
    #     time_lab = tk.Label(text = str(time[i]), font= "Helvetica 15 bold")
    #     time_lab.place(x= 80 + i * 55 - 10, y = 380)

def priority_non():
    count = len(arrival_time)
    arrival = []
    burst = []
    proc = []
    pri = []
    
    n_arrival = []
    n_burst = []
    n_proc = []
    n_pri = []
    time = []
    name = []
    tat = 0
    wt = 0
    
    for temp_c in range(count):
        arrival.append(int(arrival_time[temp_c].get()))
        burst.append(int(burst_time[temp_c].get()))
        pri.append(int(priority[temp_c].get()))
    for pre_t in range (count):
        proc.append(pre_t + 1)
    for temp in range(count):
        p_inx = find_min_index(pri)
        n_arrival.append(arrival[p_inx])
        n_burst.append(burst[p_inx])
        n_proc.append(proc[p_inx])
        n_pri.append(pri[p_inx])
        arrival.pop(p_inx)
        burst.pop(p_inx)
        proc.pop(p_inx)
        pri.pop(p_inx)
    
    n_arrival1 = []
    n_burst1 = []
    n_pri1 = []
    n_proc1 = []
    flag = 1
    while n_arrival:
        inx = find_min_index(n_arrival)
        n_arrival1.append(n_arrival[inx])
        n_burst1.append(n_burst[inx])
        n_pri1.append(n_pri[inx])
        n_proc1.append(n_proc[inx])
        n_arrival.pop(inx)
        n_burst.pop(inx)
        n_pri.pop(inx)
        n_proc.pop(inx)
    
    cp_arrival = n_arrival1.copy()       
    while n_arrival1: 
        p_inx = find_min_index(n_pri1)
        if flag:
            time.append(n_arrival1[0])
            time.append(n_arrival1[0] + n_burst1[0])
            name.append(n_proc1[0])
            n_arrival1.pop(0)
            n_burst1.pop(0)
            n_pri1.pop(0)
            n_proc1.pop(0)
            flag = 0
        else:
            if time[-1] < n_arrival1[p_inx] and time[-1] < n_arrival1[0]:
                time.append(n_arrival1[0])
                time.append(n_arrival1[0] + n_burst1[0])
                name.append(0)
                name.append(n_proc1[0])
                n_arrival1.pop(0)
                n_burst1.pop(0)
                n_pri1.pop(0)
                n_proc1.pop(0)
            elif time[-1] < n_arrival1[p_inx]:
                time.append(time[-1] + n_burst1[0])
                name.append(n_proc1[0])
                n_arrival1.pop(0)
                n_burst1.pop(0)
                n_pri1.pop(0)
                n_proc1.pop(0)
            else:
                time.append(time[-1] + n_burst1[p_inx])
                name.append(n_proc1[p_inx])
                n_arrival1.pop(p_inx)
                n_burst1.pop(p_inx)
                n_pri1.pop(p_inx)
                n_proc1.pop(p_inx)
    end_time = []
    for j in range(count):
        end_time.append(find_end_time(name, time, j + 1))
        tat += end_time[j] - cp_arrival[j]
    avg_tat = tat / 5
    wt = time[-1] / 5
    avg_wt = avg_tat - wt

    p_name = []
    for i in range(len(name)):
        p_name.append("P" + str(name[i]))

    avgtatVar.set("Average Turnaround Time")
    tat_resultVar.set(str(avg_tat))
    avgwtVar.set("Average Waiting Time")
    wt_resortVar.set(str(avg_wt))
# 圖

    name_lab.config(text = ', '.join(p_name), font= "Helvetica 14 bold")
    time_lab.config(text = str(time), font= "Helvetica 15 bold")

    # for i in range(len(name)):
    #     name_lab = tk.Label(text = "P" + str(name[i]), font= "Helvetica 15 bold")
    #     name_lab.place(x = 100 + i * 55, y = 350)
    
    # for i in range(len(time)):
    #     time_lab = tk.Label(text = str(time[i]), font= "Helvetica 15 bold")
    #     time_lab.place(x= 80 + i * 55 - 10, y = 380)

def SRT():
    count = len(arrival_time)
    arrival = []
    burst = []
    proc = []
    n_arrival = []
    n_burst = []
    n_proc = []
    time = []
    name = []
    tat = 0
    wt = 0
    
    for temp_c in range(count):
        arrival.append(int(arrival_time[temp_c].get()))
        burst.append(int(burst_time[temp_c].get()))
    for pre_t in range (count):
        proc.append(pre_t + 1)
    for temp in range(count):
        inx = find_min_index(arrival)
        n_arrival.append(arrival[inx])
        n_burst.append(burst[inx])
        n_proc.append(proc[inx])
        arrival.pop(inx)
        burst.pop(inx)
        proc.pop(inx)

    cp_arrival = n_arrival.copy()

    available = []
    proc_available = []
    time.append(0)
    p = 0
    for i in range(count):
        if time[-1] >= n_arrival[i]:
            available.append(n_burst[i])
            proc_available.append(n_proc[i])
    while any(n_burst):
        min_bur = find_min_index(available)
        if any(n_arrival): #確認是否還有行程
            for i in range(count):
                if available[min_bur] >= (n_arrival[i] - time[-1]) and n_arrival[i] != 0: #到達等於0的行程表示已進入
                    if available[min_bur] - (n_arrival[i] - time[-1]) > n_burst[i]:
                        available.append(n_burst[i])
                        proc_available.append(n_proc[i])
                        update_list(min_bur, available[min_bur] - (n_arrival[i] - time[-1]),available)
                        time.append(time[-1] + (n_arrival[i] - time[-1]))
                        name.append(proc_available[min_bur])
                        update_list(i, 0, n_arrival)#將已經進入的行程時間變為0
                        break #如有行程搶先跳出迴圈
                    else:#都沒有搶先的情況 將以到的行程加入ava串列
                        available.append(n_burst[i])
                        proc_available.append(n_proc[i])
                        update_list(i, 0, n_arrival)#將已經進入的行程時間變為0
                if i == count - 1: 
                    time.append(time[-1] + available[min_bur])
                    name.append(proc_available[min_bur])
                    temp = find_same_index(proc_available[min_bur], n_proc)
                    update_list(temp, 0, n_burst)
                    available.pop(min_bur)
                    proc_available.pop(min_bur)
        else: #行程都進入ava串列從最小的執行時間開始
            time.append(time[-1] + available[min_bur])
            name.append(proc_available[min_bur])
            temp = find_same_index(proc_available[min_bur], n_proc)
            update_list(temp, 0, n_burst)
            available.pop(min_bur)
            proc_available.pop(min_bur)
    
    end_time = []
    for j in range(count):
        end_time.append(find_end_time_DESC(name, time, j + 1))
        tat += end_time[j] - cp_arrival[j]
    avg_tat = tat / 5
    wt = time[-1] / 5
    avg_wt = avg_tat - wt

    p_name = []
    for i in range(len(name)):
        p_name.append("P" + str(name[i]))

    avgtatVar.set("Average Turnaround Time")
    tat_resultVar.set(str(avg_tat))
    avgwtVar.set("Average Waiting Time")
    wt_resortVar.set(str(avg_wt))
# 圖
    name_lab.config(text = ', '.join(p_name), font= "Helvetica 14 bold")
    time_lab.config(text = str(time), font= "Helvetica 15 bold")

    # for i in range(len(name)):
    #     name_lab = tk.Label(text = "P" + str(name[i]), font= "Helvetica 15 bold")
    #     name_lab.place(x = 100 + i * 55, y = 350)
    
    # for i in range(len(time)):
    #     time_lab = tk.Label(text = str(time[i]), font= "Helvetica 15 bold")
    #     time_lab.place(x= 80 + i * 55 - 10, y = 380)

def RR():
    count = len(arrival_time)
    quantum = int(RR_en.get())
    arrival = []
    burst = []
    proc = []
    n_arrival = []
    n_burst = []
    n_proc = []
    time = []
    name = []
    tat = 0
    wt = 0
    
    for temp in range(count):
        arrival.append(int(arrival_time[temp].get()))
        burst.append(int(burst_time[temp].get()))
    for pre_t in range (count):
        proc.append(pre_t + 1)
    for temp in range(count):
        inx = find_min_index(arrival)
        n_arrival.append(arrival[inx])
        n_burst.append(burst[inx])
        n_proc.append(proc[inx])
        arrival.pop(inx)
        burst.pop(inx)
        proc.pop(inx)

    available = []
    proc_available = []
    cp_arrival = n_arrival.copy()
    time.append(0)

    for i in range(count):
        if time[-1] >= n_arrival[i] and n_burst[i] != 0:
            available.append(n_burst[i])
            proc_available.append(n_proc[i])
    while any(n_burst):
        if available[0] > quantum:
            time.append(time[-1] + quantum)
            name.append(proc_available[0])
            temp = find_same_index(proc_available[0], n_proc)
            update_list(temp, n_burst[temp] - quantum, n_burst)
            available.pop(0)
            proc_available.pop(0)
            if any(n_arrival):
                for i in range(count):
                    if time[-1] >= n_arrival[i] and n_burst[i] != 0 and n_arrival[i] != 0:
                        available.append(n_burst[i])
                        proc_available.append(n_proc[i])
                        update_list(i, 0, n_arrival)
            available.append(n_burst[temp])
            proc_available.append(n_proc[temp])
        else:
            time.append(time[-1] + available[0])
            name.append(proc_available[0])
            temp = find_same_index(proc_available[0], n_proc)
            update_list(temp, 0, n_burst)
            available.pop(0)
            proc_available.pop(0)
            if any(n_arrival):
                for i in range(count):
                    if time[-1] >= n_arrival[i] and n_burst[i] != 0 and n_arrival[i] != 0:
                        available.append(n_burst[i])
                        proc_available.append(n_proc[i])
                        update_list(i, 0, n_arrival)
    end_time = []
    for j in range(count):
        end_time.append(find_end_time_DESC(name, time, j + 1))
        tat += end_time[j] - cp_arrival[j]
    avg_tat = tat / 5
    wt = time[-1] / 5
    avg_wt = avg_tat - wt

    p_name = []
    for i in range(len(name)):
        p_name.append("P" + str(name[i]))

    avgtatVar.set("Average Turnaround Time")
    tat_resultVar.set(str(avg_tat))
    avgwtVar.set("Average Waiting Time")
    wt_resortVar.set(str(avg_wt))
# 圖
    name_lab.config(text = ', '.join(p_name), font= "Helvetica 14 bold")
    time_lab.config(text = str(time), font= "Helvetica 15 bold")

    # for i in range(len(name)):
    #     name_lab = tk.Label(text = "P" + str(name[i]), font= "Helvetica 15 bold")
    #     name_lab.place(x = 100 + i * 55, y = 350)
    
    # for i in range(len(time)):
    #     time_lab = tk.Label(text = str(time[i]), font= "Helvetica 15 bold")
    #     time_lab.place(x= 80 + i * 55 - 10, y = 380)

win = tk.Tk()
win.title("schedule calculator")
win.geometry("900x550+400+100")
win.minsize(width= "900", height= "550")

name_lab = tk.Label(text="")
name_lab.place(x = 100, y = 350)
time_lab = tk.Label(text="")
time_lab.place(x = 80, y = 400)

RR_labVar = tk.StringVar()
avgtatVar = tk.StringVar()
avgwtVar = tk.StringVar()
tat_resultVar = tk.StringVar()
wt_resortVar = tk.StringVar()

#RR
RR_en = tk.Entry(borderwidth= "3", width= 12, justify= "center")

def algo(self):
    if  C_box.get() == "RR":
        RR_labVar.set("分時")
        RR_en.grid(row= 8, column= 1, sticky= "e")
    elif C_box != "RR" and RR_en.winfo_exists():
        RR_labVar.set("")
        RR_en.grid_forget()
RR_lab = tk.Label(textvariable = RR_labVar, font= "Helvetica 15 bold")
RR_lab.grid(row= 8, column= 0, padx= 5, sticky= "w")

C_box = ttk.Combobox(values= ["FCFS", "優先權不可搶", "SRT", "RR"])
C_box.bind("<<ComboboxSelected>>", algo)
C_box.grid(row= 1, column= 4, sticky="e")

I_lab = tk.Label(text= "Input", font= "Helvetica 20 bold")
I_lab.grid(row= 1, column= 0, columnspan= 2, padx= 40)

pro_lab = tk.Label(text= "順序", font= "Helvetica 15 bold")
pro_lab.grid(row = 2, column= 0, padx= 5)

a_lab = tk.Label(text= "到達時間", font= "Helvetica 15 bold")
a_lab.grid(row= 2, column= 1, padx= 5, sticky= "w")

b_lab = tk.Label(text= "執行時間", font= "Helvetica 15 bold")
b_lab.grid(row= 2, column= 2, padx= 5, sticky= "w")

pri_lab = tk.Label(text= "優先級", font= "Helvetica 15 bold")
pri_lab.grid(row = 2, column= 3, padx= 5, sticky= "w")

#Job lable
J_lab1 = tk.Label(text= "P1", font= "Helvetica 15 bold")
J_lab1.grid(row= 3, column= 0, padx= 5, sticky= "w")

J_lab2 = tk.Label(text= "P2", font= "Helvetica 15 bold")
J_lab2.grid(row= 4, column= 0, padx= 5, sticky= "w")

J_lab3 = tk.Label(text= "P3", font= "Helvetica 15 bold")
J_lab3.grid(row= 5, column= 0, padx= 5, sticky= "w")

J_lab4 = tk.Label(text= "P4", font= "Helvetica 15 bold")
J_lab4.grid(row= 6, column= 0, padx= 5, sticky= "w")

J_lab5 = tk.Label(text= "P5", font= "Helvetica 15 bold")
J_lab5.grid(row= 7, column= 0, padx= 5, sticky= "w")

#Job Arrival

for i in range(5):
    arr_en = tk.Entry(borderwidth= "3", width= 12, justify= "center")
    arr_en.grid(row= 3+i, column= 1, sticky= "e")
    arrival_time.append(arr_en)

#CPU burst
for i in range(5):
    bur_en = tk.Entry(borderwidth= "3", width= 12, justify= "center")
    bur_en.grid(row= 3+i, column= 2, sticky= "e")
    burst_time.append(bur_en)

#Job priority
for i in range(5):
    pri_en = tk.Entry(borderwidth= "3", width= 8, justify= "center")
    pri_en.grid(row= 3+i, column= 3, sticky= "e")
    priority.append(pri_en)
#button
result_btn = tk.Button(text = "Calculate", font= "Helvetica 15 bold" , command=test)
result_btn.grid(row= 9, column= 4)

#result
avgtat_lab = tk.Label(textvariable = avgtatVar, font= "Helvetica 10 bold")
avgtat_lab.grid(row= 9, column= 1, columnspan= 2, sticky= "e")
avgtat_lab_result = tk.Label(textvariable = tat_resultVar, font= "Helvetica 15 bold")
avgtat_lab_result.grid(row= 9, column= 3, sticky= "e")

avgwt_lab = tk.Label(textvariable = avgwtVar, font= "Helvetica 10 bold")
avgwt_lab.grid(row= 10, column= 1, columnspan= 2, sticky= "e")
avgwt_lab_result = tk.Label(textvariable = wt_resortVar, font= "Helvetica 15 bold")
avgwt_lab_result.grid(row= 10, column= 3, sticky= "e")

win.mainloop()