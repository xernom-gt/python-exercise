def convert_second(seconds):
    # 1 hari = 86400
    days = seconds // 86400
    seconds = seconds % 86400 #sisa detik setelah di hitung hari

    #1 jam = 3600
    hours = seconds // 3600
    seconds = seconds % 3600 # sisa detik setelah di hitung jam

    # 1 menit = 60
    minutes = seconds // 60
    seconds = seconds % 60 # sisa detik setelah di hitung menit
    return days,hours,minutes,seconds

input_seconds = int(input(" masukan ingin berapa detik lek : "))

days, hours, minutes, seconds = convert_second(input_seconds)

print (f'{days} hari, {hours} jam, {minutes} menit, {seconds} detik')
