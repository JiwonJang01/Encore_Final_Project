from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from diaryapp.views import diarywrite_views, comment_views, wishlist_views, base_views, diary_views, badge_views
from .mongo_queries import get_available_plans

urlpatterns = [
    #### diarywrite_views.py ####
    # 다이어리 생성
    path('api/get_plan_place/<str:plan_id>/', diarywrite_views.get_plan_place, name='get_plan_place'),
    path('write_diary/<str:plan_id>/', diarywrite_views.write_diary, name='write_diary_plan_id'),
    path('generate_diary/<str:plan_id>/', diarywrite_views.generate_diary, name='generate_diary_plan_id'),
    path('write_diary/', diarywrite_views.write_diary, name='write_diary'),
    path('generate_diary/', diarywrite_views.generate_diary, name='generate_diary'),
    path('image/<int:pk>/', diarywrite_views.image_detail, name='image_detail'),
    path('get_available_plans/', get_available_plans, name='get_available_plans'),

    # 다이어리 상세화면
    path('detail_diary/<str:unique_diary_id>/', diarywrite_views.detail_diary_by_id, name='detail_diary_by_id'),
    path('detail_diary/<str:unique_diary_id>/<str:user_email>', diarywrite_views.detail_diary_by_id, name='other_detail_diary_by_id'),

    # 다이어리 업데이트
    path('update_diary/<str:unique_diary_id>/', diarywrite_views.update_diary, name='update_diary'),

    # 다이어리 삭제
    path('delete_diary/<str:unique_diary_id>/', diarywrite_views.delete_diary, name='delete_diary'),

    # 일정 모달창
    path('plan_modal/<str:unique_diary_id>/', diarywrite_views.plan_modal, name='plan_modal'),

    # 일정 찜기능 - 찜 리스트
    path('add_wish/', wishlist_views.add_wish, name='add_wish'),
    path('wishlist_view/', wishlist_views.wishlist_view, name='wishlist_view'),
    path('remove_wish/<str:plan_id>/', wishlist_views.remove_wish, name='remove_wish'),

    #### comment_views.py ####
    # 댓글 달기
    path('create_comment/<str:unique_diary_id>/', comment_views.create_comment, name='create_comment'),

    # 댓글 삭제
    path('comment/delete/<str:diary_id>/<int:comment_id>/', comment_views.delete_comment, name='delete_comment'),

    # 태그된 친구 클릭 시 메인 다이어리 화면 이동 - 사용자 다이어리의 메인 화면 경로
    # path('maindiary', views.delete_diary, name='main_diary'),


    # 리스트 뱃지
    path('list_badge/', badge_views.list_badge, name='list_badge'),
    path('list_badge/set_main_badge/', badge_views.set_main_badge, name='set_main_badge'),
    path('list_badge/unset_main_badge/', badge_views.unset_main_badge, name='unset_main_badge'),


    # Bootstrap 테마 예시 페이지
    path('index', base_views.viewIndex),
    path('elements', base_views.viewElements),
    path('generic', base_views.viewGeneric),

    # 리스트 다이어리
    path('all_list_diary/', diarywrite_views.list_diary, name='list_diary'),
    path('list_diary/', diarywrite_views.list_user_diary, name='list_user_diary'),
    path('list_diary/<str:user_email>', diarywrite_views.list_user_diary, name='other_list_user_diary'),

    # 다이어리 메인
    path('', diary_views.viewDiary, name='user_diary_main'),
    path('<str:user_email>', diary_views.viewDiary, name='other_user_diary_main'),
    path('save_title_diary/', diary_views.save_title_diary, name='save_title_diary'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
