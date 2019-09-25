#!/usr/bin/env python
from __future__ import absolute_import
import google_images_download as gi
import ssl  # ssl Error 발생 시

ssl._create_default_https_context = ssl._create_unverified_context


def imageCrawling(keyword, dir):
    response = gi.googleimagesdownload()
    format="jpg"
    arguments = {"keywords": keyword,  # 검색 키워드
                 "limit": 500,  # 크롤링 이미지 수
                 "print_urls": True,  # 이미지 url 출력
                 "no_directory": True,  #
                 'output_directory': dir, # 크롤링 이미지를 저장할 폴더
                 'format': format}

    paths = response.download(arguments)
    print(paths)


#2019.09.24 17시 30분 실행
# imageCrawling('김우빈', 'C:\GIGA\GiGAChany\\male_faces')
# imageCrawling('현빈', 'C:\GIGA\GiGAChany\\male_faces')
# imageCrawling('박보검', 'C:\GIGA\GiGAChany\\male_faces')
# imageCrawling('이병헌', 'C:\GIGA\GiGAChany\\male_faces')
# imageCrawling('원빈', 'C:\GIGA\GiGAChany\\male_faces')
# imageCrawling('김무열', 'C:\GIGA\GiGAChany\\male_faces')
# imageCrawling('차은우', 'C:\GIGA\GiGAChany\\male_faces')
# imageCrawling('정국', 'C:\GIGA\GiGAChany\\male_faces')
#
# imageCrawling('조보아', 'C:\GIGA\GiGAChany\\female_faces')
# imageCrawling('문채원', 'C:\GIGA\GiGAChany\\female_faces')
# imageCrawling('수지', 'C:\GIGA\GiGAChany\\female_faces')
# imageCrawling('김태희', 'C:\GIGA\GiGAChany\\female_faces')
# imageCrawling('태현', 'C:\GIGA\GiGAChany\\female_faces')
# imageCrawling('설인아','C:\GIGA\GiGAChany\\female_faces')
# imageCrawling('아이유','C:\GIGA\GiGAChany\\female_faces')
# imageCrawling('사나','C:\GIGA\GiGAChany\\female_faces')

# imageCrawling('채영','C:\Image')
# imageCrawling('나연','C:\Image')
# imageCrawling('정연','C:\Image')
# imageCrawling('모모','C:\Image')
# imageCrawling('미나','C:\Image')
# imageCrawling('다현','C:\Image')
# imageCrawling('쯔위','C:\Image')


#imageCrawling('av 얼굴','C:\GIGA\GiGAChany\\av')
imageCrawling('일반인 남자','C:\GIGA\GiGAChany\Data\\male_face')




