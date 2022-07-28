def solution(id_list, report, k):
    # report에서 중복을 제거
    report= set(report)
    report_zip=[]
    reported_time=[]
    
    # 신고된 값을 이름끼리 분리, report_zip에 저장(이용자id, 신고)
    for i in report:
        report_zip.append(i.split())
    
    # reported_time에 각 이름 순서대로 신고당한 횟수를 저장
    for i in range(len(id_list)):
        reported_time.append(0)
    
    for i in range(len(report_zip)):
        reported_name= report_zip[i][1]
        p=id_list.index(reported_name)
        reported_time[p]+=1

    # 신고당한 횟수가 k 이상인 이름을 banned_name에 저장
    banned_name=[]
    for i in range(len(reported_time)):
        if reported_time[i]>=k:
            banned_name.append(id_list[i])

    # banned_name을 신고한 횟수만큼 메일을 보냄
    mail=[0]*len(id_list)
    for i in range(len(report_zip)):
        if report_zip[i][1] in banned_name:
            p= id_list.index(report_zip[i][0])
            mail[p]+=1
        
    return mail
