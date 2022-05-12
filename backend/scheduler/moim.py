import datetime
from greenmates.models import Moim, Mate

now = datetime.datetime.now()

def update_status():
    '''
    1. 모임 시간 2시간 전 & 인원부족: 모집 취소 
    2. 모임 시간 이후 & 인원 충족: 모집 종료 
    '''
    two_hrs = now + datetime.timedelta(hours=2)
    # 1. 모임 2시간 전인데, 모임 모집이 안된 경우 => moim status 0(모집중) -> 2(모집취소)
        ## mate_status 1(합류) -> 3(취소)
    Moim.objects.filter(time__lte=two_hrs, status=0).update(status=2)
    Mate.objects.filter(mate_status=1, moim__status=2).update(mate_status=3)

    # 2. 모임 시간 후, moim status가 1(모집 완료)인 모임 => moim status 1(모집완료) -> 3(모임 종료)
        ## mate_status 1(합류) -> 4(완료)
    Moim.objects.filter(time__lte=now, status=1).update(status=3)
    Mate.objects.filter(mate_status=1, moim__status=3).update(mate_status=4)
