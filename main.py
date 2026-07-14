import csv

def read_csv_to_list(file_path):
    data = []
    try:
        with open(file_path, mode='r', encoding='utf-8', newline='') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                data.append(row)
    except FileNotFoundError:
        print(f"שגיאה! הקובץ לא נמצא בנתיב {file_path}")
    except Exception as e:
        print(f"התרחשה שגיאה בזמן קריאת הקובץ{e}")
    return data

