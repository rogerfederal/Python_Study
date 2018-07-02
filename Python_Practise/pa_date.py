import datetime
def main():
    begin = datetime.date(2018,7,2)
    end = datetime.date(2018,12,31)
    for i in range((end - begin).days+1):
        day = begin + datetime.timedelta(days=i)
        print(str(day))

if __name__ == '__main__':
    main()