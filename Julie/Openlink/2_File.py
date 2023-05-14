import csv

links = ['https://google.com/', 
        'https://naver.com/',
        'https://nate.com/',
        'https://amazon.com/',
        'https://discord.com/',
        'https://google.com/']

with open("save.csv", 'w', newline='') as f:
    linkst = csv.writer(f)    
    linkst.writerow(links)

f.close()

with open("C:\\Users\\visio\\OneDrive\\Desktop\\Julie\\save.csv", 'r', encoding='utf-8') as fi:
    reader = csv.reader(fi)
    for row in reader: 
        print(row)

#print(new_link)

fi.close()

#save = open("save.txt", 'r') # r = read, w = read/write
#save_datas = save.readlines()


#for save_data in save_datas:
#    clear = save_data.strip()
#    save_datas[save_data] = clear

# print(save_datas)
#for save_data in save_datas:
 #   print(save_data)
 #save.write("Hello \n World \n I'm so tired")

#f.close()
