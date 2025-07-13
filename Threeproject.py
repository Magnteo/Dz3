import sys
def parse_log_line(line:str) -> dict:
    log=[]
    parts=line.split()
    return{
        "date":parts[0],
        "time":parts[1],
        "level":parts[2],
        "message":" ".join(parts[3:])
    }
 
def load_logs(file_path: str) -> list:
    logs=[]
    with  open(file_path,"r",encoding="utf-8") as file:
        for line in file:
            log_dict= parse_log_line(line)
            logs.append(log_dict)
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    level =level.upper()
    filter_log =filter(lambda log:log['level']==level,logs)
    return list(filter_log)

def count_logs_by_level(logs: list) -> dict:
    counts={}
    for log in logs:
        level = log['level']
        if not level in counts:
            counts[level]=1
        else:
            counts[level]+=1
    return counts

def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level , count in counts.items():
        print(level.ljust(16),"|", str(count).rjust(8)) #тут мені  чат допоміг з відступами
    print("Завершено")
# чомусь в завдані небуло сказано зробити  окремо для виведеня тому прийшлось працювати з чатом
if __name__=='__main__':
    if len(sys.argv)<2:
        print("Помилка вкажіть шлях до логів")
        sys.exit(1)
    file_path=sys.argv[1]
    level=sys.argv[2] if len (sys.argv)>2 else None
    try:
        logs = load_logs(file_path)
    except FileNotFoundError:
        print(f'File{file_path} не знайшов')
        sys.exit(1)
    except Exception as eg:
        print(f"Помилка при читанні файлу: {eg}")
        sys.exit(1)

    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if level:
        filtered= filter_logs_by_level(logs,level)
        print(f"\nДеталі логів для рівня '{level.upper()}':")
        for log in filtered:
            print(f"{log['date']} {log['time']} - {log['message']}")
