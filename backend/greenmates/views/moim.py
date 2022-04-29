from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Prefetch
from ..models import Moim, Mate
from ..serializers.moim import (
    MoimSimpleKrSerializer,
    MoimSimpleEnSerializer,
    MoimDetailKrSerializer, 
    MoimDetailEnSerializer,
    MoimAllKrSerializer,
    MoimAllEnSerializer,
    MoimTransSerializer,
    MoimPostPutSerializer,
)

from django.contrib.auth import get_user_model
User = get_user_model()
user = User.objects.filter(pk=2)   # TODO: request.user로 변경 (현재 pk=2로 TEST중)
# TODO: 유저정보
# 1. request.user 언어정보
# 2. login_required
# 3. 

@api_view(['GET', 'POST'])
def get_create_moim_list(request):
    '''
    GET: 모집 중인 모든 모임 글을 조회
    POST: 새로운 모임 글을 작성
    '''
    def moim_list():
        moims = Moim.objects.filter(status=0)
        serializer = MoimSimpleKrSerializer(moims, many=True)
        # if user.language: # En
        #     serializer = MoimSimpleEnSerializer(moims, many=True)
        return Response(serializer.data)

    def moim_create():
        pass
    
    if request.method == 'GET':
        return moim_list()

    elif request.method =="POST":
        moim_create()

@api_view(['GET', 'PUT'])
def get_update_moim_detail(request, moim_id):
    '''
    GET : 해당 모임 글의 상세 조회
    PUT : 해당 모임 글의 날짜, 시간 수정 (2시간 전까지)
    '''
    def moim_detail():
        moim = get_object_or_404(Moim, pk=moim_id)
        serializer = MoimDetailKrSerializer(moim)
        # if user.language: # En
        #     serializer = MoimDetailEnSerializer(moim)
        return Response(serializer.data)

    def moim_update():
        pass
    
    if request.method == 'GET':
        return moim_detail()
    
    elif request.method == 'PUT':
        moim_update()

@api_view(['GET'])
def get_trans_moim(request, moim_id):
    '''
    GET: 해당 모임글의 번역글을 조회
    '''
    if request.method == 'GET':
        moim = get_object_or_404(Moim, pk=moim_id)
        serializer = MoimTransSerializer(moim)
        return Response(serializer.data)

@api_view(['GET'])
def get_waiting_moim(request):
    '''
    GET: 유저가 게스트로 대기중인 모임 리스트 조회
    '''
    # TODO: author_id를 request.user에서 가져오기. 현재 2번 user로 TEST 중.
    if request.method == 'GET':
        moims = get_list_or_404(Moim.objects.filter(mate__user=2, mate__mate_status=0))
        serializer = MoimDetailKrSerializer(moims, many=True)
        # if user.language:
        #     serializer = MoimDetailEnSerializer(moims)
        return Response(serializer.data)

@api_view(['GET'])
def get_joined_moim(request):
    '''
    GET: 유저가 게스트로 합류중인 모임 리스트 조회
    ''' 
    if request.method == 'GET':
        moims = get_list_or_404(Moim.objects.filter(mate__user=2, mate__mate_status=1).exclude(author_id=2))
        serializer = MoimDetailKrSerializer(moims, many=True)
        # if user.language:
        #     serializer = MoimDetailEnSerializer(moims)
        return Response(serializer.data)

@api_view(['GET'])
def get_opened_moim(request):
    '''
    GET: 유저가 호스트로 개설한 모임 리스트 조회
    '''
    if request.method == 'GET':
        moims = get_list_or_404(Moim.objects.filter(author_id=2, status__lt=2))
        serializer = MoimAllEnSerializer(moims, many=True)
        # if user.language:
        #     serializer = MoimAllKrSerializer(moims, many=True)
            
        return Response(serializer.data)

@api_view(['GET'])
def get_finished_moim(request):
    '''
    GET: 유저가 호스트 / 게스트로 참여한 종료된 모임 리스트 조회
    '''
    if request.method == 'GET':
        moims = get_list_or_404(Moim.objects.filter(mate__user=2, mate__mate_status=4))
        serializer = MoimDetailKrSerializer(moims, many=True)
        # if user.language:
        #     serializer = MoimDetailEnSerializer(moims)
        return Response(serializer.data)