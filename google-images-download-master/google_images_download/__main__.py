#!/usr/bin/env python
from __future__ import absolute_import
import google_images_download as gi



def imageCrawling(keyword, dir):
    response = gi.googleimagesdownload()

    arguments = {"keywords": keyword,  # 검색 키워드
                 "limit": 500,  # 크롤링 이미지 수
                 "print_urls": True,  # 이미지 url 출력
                 "no_directory": True,  #
                 'output_directory': dir}  # 크롤링 이미지를 저장할 폴더

    paths = response.download(arguments)
    print(paths)


imageCrawling('여자얼굴', 'C:\GIGA\GiGAChany\\female_faces')
#imageCrawling('남자얼굴', 'C:\GIGA\GiGAChany\\man_faces')
